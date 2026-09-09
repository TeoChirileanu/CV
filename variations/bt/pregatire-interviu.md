# Pregătire pentru interviu — Senior .NET Backend Developer

Pune în față experiența bancară, integrarea și modernizarea controlată. Surse: [CV-ul existent](../../index.html), captura LinkedIn pentru CFP Energy și precizările tale despre Oracle/Kubernetes. Cerințe: [fișa rolului](Senior_NET_Backend_Developer_JD.docx). P indică paragrafele Word, inclusiv cele goale. Rolul exclude people management și ownership-ul suportului de producție (P7–8).

## Prezentare de 45–60 de secunde

„Sunt dezvoltator .NET cu experiență la ING, Société Générale și American Express, în aplicații bancare și de plăți. La ING am lucrat cu C#, Visual Basic și WCF, am mutat sesiunile în Redis și am coordonat upgrade-uri la .NET 8. La Société Générale am implementat cerințe Basel III și am optimizat procesări SSIS. La Amex am lucrat pe un sistem legacy, certificarea plăților și teste automate. La CFP Energy am lucrat cu microservicii .NET, Kafka și SignalR pentru trading de energie și carbon. Mă adaptez la codul existent și la constrângerile businessului, abordând modernizarea gradual, cu verificarea comportamentului.”

## Șase povești de pregătit

Pentru fiecare: context, contribuția proprie, decizia, alternativa respinsă și verificarea rezultatului. Nu adăuga volume sau procente neverificate.

1. **ING — platformă existentă și .NET 8.** Context documentat: C#, Visual Basic, WCF, aplicații pentru lending, business banking și card issuing. Ai migrat sesiunile din memorie în Redis și ai coordonat upgrade-ul mai multor aplicații la .NET 8. Explică dependențele vechi, compatibilitatea, testarea și pașii de migrare executați efectiv.

2. **Société Générale — SQL, SSIS și raportare.** Ai implementat metrici Basel III în Liqor și ai optimizat scripturi SSIS; CV-ul indică o îmbunătățire de 35%. Ai modernizat și pipeline-ul TeamCity 2008–2018. Pregătește contextul măsurătorii, validarea calculelor financiare și modul de păstrare a comportamentului existent.

3. **American Express — legacy și testare.** Stackul include C#, Visual Basic și WCF. Ai menținut un sistem legacy critic, ai contribuit la NGS și ai introdus Playwright pentru certificarea plăților, fără echipă QA dedicată. Explică relația dintre nou și existent, criteriile de acceptare și automatizarea build/package/deploy cu PowerShell și Cake.

4. **CFP Energy — Kafka și operațiuni în timp real.** Proiectul din martie–octombrie 2025 documentează backend pentru trading de energie și carbon, microservicii .NET, SignalR și Kafka. Pregătește un flux concret: ce date circulau, contribuția ta și tratarea erorilor. Explică producătorii, consumatorii și garanțiile numai în măsura experienței reale. Captura menționează Molecule API, dar textul trunchiat nu justifică detalii suplimentare.

5. **RTGS.global — audit și retry.** Serviciu central de audit imuabil, fail-closed, cu Service Bus, dead-lettering și retenție de șapte ani; retry SQL la nivel de activity, deadlock-uri și politici Polly v8. Explică reacția la erori și testarea, plus duplicatele și consistența, fără a inventa mecanisme.

6. **Deloitte — integrare și recuperarea mesajelor.** Ai extins API-uri de integrare și ai implementat „Resend Broken Messages” / „Poison Message” în Azure Service Bus. Descrie traseul unui mesaj eșuat, condițiile de retrimitere și testele pentru sincronizări complexe. Leagă exemplul de recuperarea controlată cerută în JD (P22–25, P48).

## Clarificări înainte de discuție

Kafka are acum dovadă practică la CFP Energy; perioada proiectului nu dovedește doi ani de Kafka. Oracle a fost folosit la facultate: prezintă-l ca experiență academică, fără a pretinde producție sau doi ani de experiență profesională. Kubernetes are experiență practică și este alternativa acceptată în JD; nu pretinde experiență OpenShift. Autorizarea EUAA nu dovedește OAuth 2.0/JWT. Pentru IIS, pregătește un exemplu de configurare, deployment sau diagnosticare; clarifică versiunile .NET Framework. Nu inventa durate și nu însuma proiectele suprapuse. JD-ul nu stabilește că infrastructura BT este veche.

## Întrebări pentru intervievator

1. Care sunt primele servicii sau integrări pe care le-ar prelua persoana aleasă și ce rezultat așteptați în primele trei luni?
2. Cum sunt gestionate contractele API și evenimentele Kafka: versionare, compatibilitate și recuperarea mesajelor eșuate?
3. Care este mixul real dintre .NET Framework, VB, WCF, IIS, SQL/SSIS și stackul modern din JD? Ce modernizări sunt planificate?
4. Ce teste, verificări de securitate și criterii de observabilitate trebuie îndeplinite înainte de livrare?
