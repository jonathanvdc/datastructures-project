Toepassingsopdracht gegevensabstractie en datastructuren:
- Sibert Aerts
- Olivier Bloch
- Othman Nahhas
- Jonathan Van der Cruysse

=========================================================
Inhoud:
- Contracts: bevat contracten voor de klassen in 'Implementations'.
- Implementations: implementaties van de contracten in 'Contracts', i.e. de datastructuren en het reservatiesysteem.
- Test: testbestanden en een console-UI voor het project
--> CLI: bevat het command-line interface voor het project.
----> Tests: bevat geautomatiseerde tests voor het CLI

=========================================================
Tests:
- ProjectTest.py (Test/ProjectTest.py): tests voor de verschillende datastructuren die geimplementeerd zijn
- TheaterTests.py (Test/TheaterTests.py): tests voor het reservatiesysteem: 
  genereert films, auditoria, klanten en vertoningen, reserveert tickets en laat klanten binnengaan in de zaal.
- CommandLineInterface.py (Test/CLI/CommandLineInterface.py - manuele modus): 
  geeft een command-line interface waarmee het reservatiesysteem en de onderliggende ADTs gemanipuleerd kunnen worden.
- CommandLineInterface.py (Test/CLI/CommandLineInterface - automatische mode: python CommandLineInterface.py Tests/input.txt Tests/output.txt):
  laat toe het voorgaande UI te automatiseren door middel van een input file (Tests/input.txt) en een output file (Tests/output.txt).
  Een gelijkaardig effect kan bereikt worden door 'python CommandLineInterface.py < Tests/input.txt > Tests/output.txt', maar dit zorgt voor een verschillende output:
  Alle output die geklassificeerd is als een 'query', i.e. een vraag naar de gebruiker toe, wordt getoond door de 'ConsoleOutputStream, 
  maar genegeerd door 'FileOutputStream', de output stream implementatie voor files.
  Dit omwille van de redenering dat een input file alvast alle antwoorden bevat op de vragen die normaalgezien gesteld worden,
  waardoor het vertonen van vragen en opties in de output strikt overbodig zou zijn.