"""Render the print-ready CV and check its two-page layout.

Run from any directory with Python, Playwright Chromium and PyMuPDF installed.
"""
from pathlib import Path
import json

import fitz
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Teodor_Chirileanu_CV_BT.pdf"
QA = ROOT / ".qa"


def main():
    QA.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1000, "height": 1250}, device_scale_factor=1)
        page.goto((ROOT / "pager.html").as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.evaluate("document.fonts.ready")
        layout = page.evaluate("""() => [...document.querySelectorAll('.page')].map((p, i) => {
            const r = p.getBoundingClientRect();
            const content = p.querySelector('.content').getBoundingClientRect();
            const footer = p.querySelector('footer').getBoundingClientRect();
            const bad = [...p.querySelectorAll('*')].filter(e => {
                const b = e.getBoundingClientRect();
                return b.left < r.left - 1 || b.right > r.right + 1 || b.bottom > r.bottom + 1;
            }).map(e => e.className || e.tagName);
            return {page: i + 1, contentBottom: content.bottom - r.top,
                footerTop: footer.top - r.top, clearance: footer.top - content.bottom,
                overflowing: bad};
        })""")
        print(json.dumps(layout, indent=2))
        assert all(x["clearance"] > 8 and not x["overflowing"] for x in layout), "Page content overflows or touches footer"
        assert page.locator(".photo").evaluate("img => img.complete && img.naturalWidth > 0"), "Photo missing"
        page.pdf(path=str(OUTPUT), prefer_css_page_size=True, print_background=True,
                 display_header_footer=False, tagged=True, outline=True)
        browser.close()

    doc = fitz.open(OUTPUT)
    assert len(doc) == 2, f"Expected two pages, got {len(doc)}"
    assert len(doc[0].get_images()) > 0, "PDF photo missing"
    margin_pt = 36  # Narrow margins: 12.7 mm on all four sides.
    for i, page in enumerate(doc):
        assert abs(page.rect.width - 595.276) < .5 and abs(page.rect.height - 841.890) < .5, "Page must be A4"
        for block in page.get_text("dict")["blocks"]:
            x0, y0, x1, y1 = block["bbox"]
            assert x0 >= margin_pt - .5 and y0 >= margin_pt - .5, "Content crosses top/left narrow margin"
            assert x1 <= page.rect.width - margin_pt + .5 and y1 <= page.rect.height - margin_pt + .5, "Content crosses bottom/right narrow margin"
        page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5)).save(QA / f"page-{i + 1}.png")
    text = "\n".join(page.get_text() for page in doc)
    (QA / "extracted-text.txt").write_text(text, encoding="utf-8")
    spans = [s for page in doc for block in page.get_text("dict")["blocks"]
             if "lines" in block for line in block["lines"] for s in line["spans"]]
    result = {"pdf": str(OUTPUT), "pages": len(doc),
              "paper": "A4", "minimum_margins_mm": 12.7,
              "body_font_pt": 11, "smallest_font_pt": round(min(s["size"] for s in spans), 2),
              "photo_images_page_1": len(doc[0].get_images()),
              "links": sum(len(page.get_links()) for page in doc), "layout": layout}
    (QA / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
