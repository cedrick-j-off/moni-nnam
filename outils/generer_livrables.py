"""Produit les fichiers à déposer pour l'épreuve, dans livrables/depot/ :

- Groupe_<N>_Document.pdf  : description + note technique + identification linguistique,
  à partir de livrables/1-description.md, 2-note-technique.md et 3-langues-et-validation.md ;
- Groupe_<N>_Prototype.zip : le dossier extension/ et une notice d'installation.

Usage : python outils/generer_livrables.py ["<chemin de msedge.exe ou chrome.exe>"]

Le numéro du groupe, le nom de l'équipe, le représentant et le nom du locuteur se règlent dans
livrables/identite.json (à créer en copiant identite.exemple.json ; non publié). Une valeur laissée vide garde la mention « à compléter » dans le PDF.
Demande les bibliothèques Python « markdown » et « pypdf », et Edge ou Chrome pour l'impression en PDF.
"""
import html
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import zipfile

import markdown
from pypdf import PdfReader

RACINE = pathlib.Path(__file__).resolve().parent.parent
LIVRABLES = RACINE / "livrables"
DEPOT = LIVRABLES / "depot"
NAVIGATEURS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]
navigateur = sys.argv[1] if len(sys.argv) > 1 else next((n for n in NAVIGATEURS if os.path.exists(n)), None)
assert navigateur, "Edge ou Chrome introuvable : donner son chemin en argument."

# identite.json contient des coordonnées personnelles : il n'est pas publié. Sans lui, le modèle vide sert.
fichier_identite = LIVRABLES / "identite.json"
if not fichier_identite.exists():
    fichier_identite = LIVRABLES / "identite.exemple.json"
identite = json.loads(fichier_identite.read_text(encoding="utf-8"))
groupe = str(identite.get("groupe") or "X").strip()
# Dans les noms de fichiers, le nom du groupe s'écrit sans espace : « Moni Nnam » -> « Moni_Nnam ».
nom_fichier = re.sub(r"\s+", "_", groupe)
A_COMPLETER = "à compléter"
equipe = identite.get("equipe") or A_COMPLETER
representant = identite.get("representant") or A_COMPLETER
locuteur = identite.get("locuteur_basaa") or A_COMPLETER
version = json.loads((RACINE / "extension" / "manifest.json").read_text(encoding="utf-8"))["version"]

PARTIES = [
    ("1-description.md", "Description de la solution"),
    ("2-note-technique.md", "Note technique"),
    ("3-langues-et-validation.md", "Identification linguistique"),
]
FIGURE = f"""
<figure>
  <div class="captures">
    <div><img src="{(LIVRABLES / 'images' / 'page-origine.png').as_uri()}" alt=""><p>La page de test, telle que le service l'affiche.</p></div>
    <div><img src="{(LIVRABLES / 'images' / 'page-basaa.png').as_uri()}" alt=""><p>La même page avec Moni Nnam, en bàsàa. Le solde et le numéro de compte sont identiques.</p></div>
  </div>
</figure>
"""


def partie(fichier, numero, titre):
    texte = (LIVRABLES / fichier).read_text(encoding="utf-8")
    # Le titre et les deux lignes d'en-tête de chaque document sont remplacés par la page de garde.
    texte = re.sub(r"\A# .*\n\n\*\*SAFINUM.*\n.*\n", "", texte)
    texte = texte.replace("[nom du locuteur bàsàa]", locuteur).replace("[nom de l'équipe]", equipe)
    # Dans le PDF, les trois documents sont les parties d'un seul : les renvois le disent.
    texte = texte.replace("(voir « Langues et validation linguistique »)", "(voir la partie 3)")
    # Les sections déjà numérotées (« ## 1. Architecture ») perdent leur numéro : la partie porte le sien.
    texte = re.sub(r"^## \d+\. ", "## ", texte, flags=re.M)
    texte = re.sub(r"voir section \d+", "voir plus bas", texte)
    corps = markdown.markdown(texte, extensions=["tables", "fenced_code", "sane_lists"])
    if fichier.startswith("1-"):
        corps = corps.replace("<h2>La bonne intonation</h2>", FIGURE + "<h2>La bonne intonation</h2>", 1)
        assert "<figure>" in corps, "titre de section introuvable pour placer les captures"
    return f'<section class="partie"><h1>{numero}. {html.escape(titre)}</h1>{corps}</section>'


CSS = """
@page { size: A4; margin: 25mm 25mm 22mm 25mm; @bottom-center { content: counter(page); font: 10pt "Times New Roman", Times, serif; } }
@page :first { @bottom-center { content: none; } }
* { box-sizing: border-box; }
body { margin: 0; font: 12pt/1.45 "Times New Roman", Times, serif; color: #000; }
.garde { height: 240mm; display: flex; flex-direction: column; justify-content: space-between; text-align: center; page-break-after: always; }
.garde p { text-align: center; }
.garde .haut { font-size: 13pt; font-weight: bold; }
.garde h1 { font-size: 34pt; margin: 0 0 6mm; }
.garde .accroche { font-size: 14pt; font-style: italic; margin: 0 auto; max-width: 120mm; }
.garde .contenu { margin: 12mm auto 0; font-size: 12pt; }
.garde .bas { font-size: 12pt; line-height: 1.6; }
.partie { page-break-before: always; }
.partie:first-of-type { page-break-before: auto; }
h1 { font-size: 18pt; margin: 0 0 6mm; }
h2 { font-size: 14pt; margin: 7mm 0 2.5mm; page-break-after: avoid; }
p { margin: 0 0 3mm; text-align: justify; }
ul, ol { margin: 0 0 3mm; padding-left: 7mm; } li { margin-bottom: 1.5mm; text-align: justify; }
table { width: 100%; border-collapse: collapse; margin: 3mm 0 5mm; font-size: 11pt; }
th, td { padding: 1.8mm 2.2mm; border: 1px solid #000; vertical-align: top; text-align: left; }
th { font-weight: bold; }
tr { page-break-inside: avoid; }
code { font: 10pt "Courier New", monospace; }
figure { margin: 5mm 0 3mm; page-break-inside: avoid; }
.captures { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; }
.captures img { width: 100%; display: block; border: 1px solid #888; }
.captures p { font-size: 10pt; font-style: italic; margin: 1.5mm 0 0; text-align: left; }
"""

document = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Moni Nnam</title><style>{CSS}</style></head><body>
<div class="garde">
  <div class="haut">SAFINUM Innovate Challenge<br>Épreuve de présélection</div>
  <div>
    <h1>Moni Nnam</h1>
    <p class="accroche">Une extension de navigateur qui affiche et fait entendre un service financier en bàsàa, sans modifier le service</p>
    <p class="contenu">Description de la solution, note technique et identification linguistique</p>
  </div>
  <div class="bas">
    Équipe : {html.escape(equipe)}<br>
    Représentant : {'<br>'.join(html.escape(x.strip()) for x in representant.split(','))}<br>
    Prototype : version {html.escape(version)}<br>
    {html.escape(identite.get("date") or "")}
  </div>
</div>
{''.join(partie(f, i, t) for i, (f, t) in enumerate(PARTIES, 1))}
</body></html>"""

DEPOT.mkdir(exist_ok=True)
pdf = DEPOT / f"Groupe_{nom_fichier}_Document.pdf"
with tempfile.TemporaryDirectory() as tmp:
    page = pathlib.Path(tmp) / "document.html"
    page.write_text(document, encoding="utf-8")
    if pdf.exists():
        pdf.unlink()
    subprocess.run([navigateur, "--headless=new", "--disable-gpu", f"--user-data-dir={tmp}/profil", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", page.as_uri()], check=True, capture_output=True, timeout=120)
assert pdf.exists(), "le navigateur n'a pas produit le PDF"
print(f"{pdf.name} : {len(PdfReader(str(pdf)).pages)} pages, {pdf.stat().st_size // 1024} Ko")

NOTICE = f"""Moni Nnam - prototype (version {version})
Équipe {equipe}

Extension pour Chrome et Edge. Elle affiche et fait entendre en bàsàa la page de test
https://safinum.cm/hackathon-test, sans modifier cette page.

INSTALLATION
1. Extraire cette archive.
2. Ouvrir chrome://extensions ou edge://extensions et activer le mode développeur.
3. Cliquer sur « Charger l'extension non empaquetée » et choisir le dossier « extension ».
4. Ouvrir https://safinum.cm/hackathon-test.

UTILISATION
- Cliquer sur le bouton rond de l'extension (un globe), en haut à droite de la page.
- Choisir « Bàsàa » : les textes et l'habillage de la page changent aussitôt.
- Survoler un texte puis cliquer sur le haut-parleur pour l'écouter,
  ou cliquer sur « Lire toute la page » dans le panneau.
- « Page d'origine » rend à la page son apparence et ses textes.

Tout s'exécute dans le navigateur : aucun serveur, aucun compte, aucun appel réseau.
Le détail technique est dans extension/README.md et dans le document du groupe.
"""
archive = DEPOT / f"Groupe_{nom_fichier}_Prototype.zip"
dossier = f"Groupe_{nom_fichier}_Prototype"
fichiers = sorted(p for p in (RACINE / "extension").rglob("*") if p.is_file())
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr(f"{dossier}/LISEZ-MOI.txt", NOTICE)
    for p in fichiers:
        z.write(p, f"{dossier}/extension/{p.relative_to(RACINE / 'extension').as_posix()}")
print(f"{archive.name} : {len(fichiers)} fichiers, {archive.stat().st_size / 1e6:.1f} Mo")
