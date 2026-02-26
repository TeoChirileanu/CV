# CV Repository — Teodor Chirileanu

## Purpose
Personal CV repository containing both an HTML version and a Word (docx) version formatted for rinf.tech's template.

## File Structure
- `index.html` — Main CV, self-contained (HTML + inline CSS). A4 page layout, print-friendly. Source of truth for all experience data.
- `cv-rinf.docx` — CV in rinf.tech's company template (green sidebar, two-column layout). Generated/updated via python-docx scripts (not checked in). Currently tailored for a treasury system architect role.
- `jd-*.md` — Job descriptions used to tailor the docx CV for specific roles.
- `style.css` — Legacy standalone stylesheet (now inlined in index.html).
- `Profile.pdf` — Profile document.
- `ai-profile.jpeg` — Profile image (hosted on GitHub, referenced by URL in index.html).

## Key Conventions
- The HTML CV uses a two-column CSS grid for detailed experiences (left: tech environment + project description, right: key achievements).
- The summary section on page 1 groups experiences by domain (Crypto, Financial Services, Energy, Other).
- Recommendations section contains LinkedIn-style quotes.
- All experiences are listed in reverse chronological order in the HTML version.
- The docx version may reorder experiences to prioritize relevance to the target JD.

## Updating the docx
When creating a python-docx update script:
- The docx has 3 tables: Table 0 (name + title), Table 1 (About Me left column + first Work Experience right column), Table 2 (rinf.tech footer).
- Body paragraphs after the tables contain the remaining experiences, skills, certifications, languages, and disclaimer.
- Text in the left column (About Me) uses white color (FFFFFF) on a green background.
- Title sizes: 14pt (177800 EMU) for role titles/dates, 10pt (127000 EMU) for body text.
- Always save to a new filename first to avoid PermissionError if Word has the file open.

## Owner
Teodor Chirileanu — .NET/Azure Solution Architect, 8+ years experience in financial services, treasury systems, banking, and regulated environments.
