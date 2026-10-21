import subprocess
import fitz

html_letter = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Lettre de Motivation - Rodrigue HESSOU - Vendeur Polyvalent adidas</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Carlito:ital,wght@0,400;0,700;1,400;1,700&display=swap');

  @page {
    size: A4 portrait;
    margin: 0;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Carlito', 'Calibri', 'Segoe UI', Arial, sans-serif;
    background-color: #ffffff;
    color: #262626;
    width: 210mm;
    height: 297mm;
    margin: 0 auto;
    padding: 18mm 22mm 16mm 22mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    line-height: 1.44;
  }

  /* HEADER EXPEDITEUR / DESTINATAIRE */
  .header-block {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 5mm;
  }

  .sender-info {
    display: flex;
    flex-direction: column;
    gap: 1.1mm;
  }

  .sender-name {
    font-size: 16pt;
    font-weight: 700;
    color: #1e293b;
    letter-spacing: -0.2px;
  }

  .sender-subtitle {
    font-size: 10pt;
    font-weight: 700;
    color: #2e75b6;
    margin-bottom: 1.2mm;
  }

  .sender-detail {
    font-size: 9.2pt;
    color: #475569;
    line-height: 1.35;
  }

  .recipient-card {
    background-color: #f8fafc;
    border-left: 3px solid #1e293b;
    padding: 3.5mm 5mm;
    border-radius: 0 4px 4px 0;
    width: 76mm;
    display: flex;
    flex-direction: column;
    gap: 1.1mm;
  }

  .recipient-name {
    font-size: 10pt;
    font-weight: 700;
    color: #1e293b;
  }

  .recipient-detail {
    font-size: 9.2pt;
    color: #475569;
    line-height: 1.35;
  }

  /* DATE & OBJET */
  .meta-block {
    margin-bottom: 3.8mm;
  }

  .date-line {
    text-align: right;
    font-size: 9.2pt;
    color: #64748b;
    margin-bottom: 2.5mm;
  }

  .object-line {
    font-size: 10pt;
    color: #1e293b;
    padding: 2.2mm 3.5mm;
    background-color: #f1f5f9;
    border-radius: 4px;
  }

  .object-line strong {
    color: #1e293b;
    font-weight: 700;
  }

  /* LETTER BODY */
  .letter-content {
    display: flex;
    flex-direction: column;
    gap: 3.2mm;
    font-size: 9.35pt;
    color: #262626;
    text-align: justify;
    line-height: 1.42;
  }

  .salutation {
    font-size: 9.8pt;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 0.5mm;
  }

  .letter-content p strong {
    color: #1e293b;
    font-weight: 700;
  }

  /* CLOSING & SIGNATURE */
  .closing-block {
    margin-top: 4mm;
    display: flex;
    justify-content: flex-end;
  }

  .signature-box {
    text-align: right;
    display: flex;
    flex-direction: column;
    gap: 1.2mm;
  }

  .signature-name {
    font-size: 11pt;
    font-weight: 700;
    color: #1e293b;
  }

  .signature-title {
    font-size: 8.8pt;
    color: #64748b;
  }
</style>
</head>
<body>

  <div>
    <!-- HEADER -->
    <div class="header-block">
      <div class="sender-info">
        <div class="sender-name">Rodrigue HESSOU</div>
        <div class="sender-subtitle">Candidat Vendeur Polyvalent — adidas Lyon Part-Dieu</div>
        <div class="sender-detail">429 Cours Émile Zola</div>
        <div class="sender-detail">69100 Villeurbanne – Lyon</div>
        <div class="sender-detail">+33 7 44 11 75 73</div>
        <div class="sender-detail">rodriguehessou14@gmail.com</div>
      </div>

      <div class="recipient-card">
        <div class="recipient-name">ADIDAS FRANCE</div>
        <div class="recipient-detail">À l'attention de l'équipe Recrutement Retail</div>
        <div class="recipient-detail">Magasin adidas Lyon Part-Dieu</div>
        <div class="recipient-detail">CC Westfield La Part-Dieu, 17 Rue Dr Bouchut</div>
        <div class="recipient-detail">69003 Lyon</div>
      </div>
    </div>

    <!-- META: DATE & OBJET -->
    <div class="meta-block">
      <div class="date-line">À Lyon, le 22 octobre 2026</div>
      <div class="object-line">
        <strong>Objet :</strong> Candidature au poste de Vendeur Polyvalent adidas (H/F/D) — CDI 35H — Lyon Part-Dieu
      </div>
    </div>

    <!-- CORPS DE LA LETTRE -->
    <div class="letter-content">
      <div class="salutation">Madame, Monsieur,</div>

      <p>
        Passionné par l'univers du sport, l'énergie du lifestyle urbain et les marques qui inspirent le dépassement de soi, c'est avec un enthousiasme sincère que je vous propose ma candidature pour le poste de <strong>Vendeur Polyvalent au sein du magasin adidas Lyon Part-Dieu</strong>. La vision d'adidas — celle d'une communauté de rebelles optimistes qui changent la vie à travers le sport tout en innovant pour la durabilité et l'inclusion — résonne profondément avec mon dynamisme personnel et mon goût du collectif.
      </p>

      <p>
        Mon parcours m'a permis d'acquérir une solide expérience opérationnelle du commerce et du contact client direct. Lors de mon activité au <strong>Supermarché Champion en 2024</strong>, j'ai développé une grande réactivité sur le terrain : accueil chaleureux, orientation immédiate, gestion d'encaissements rapides et sans erreur lors de forts pics d'affluence, et maintien rigoureux de la propreté et du facing des rayons. Cette immersion m'a appris à garder le sourire, le sang-froid et une écoute active bienveillante en toutes circonstances.
      </p>

      <p>
        Complétée par une expérience en <strong>plateforme logistique et distribution en 2025</strong>, où j'ai assuré la réception, le contrôle qualité et la remise client avec une rigueur exemplaire, j'ai également piloté chez <strong>Nataan Group</strong> la prospection terrain de plus de <strong>100 commerçants</strong> pour le déploiement d'une solution de point de vente. Cette dernière mission m'a sensibilisé aux <strong>indicateurs clés de performance retail (KPI)</strong> : optimisation du panier moyen, indice de vente, taux de transformation et fidélisation par une expérience client personnalisée.
      </p>

      <p>
        Rejoindre l'équipe adidas de Lyon Part-Dieu, c'est l'opportunité de devenir un <strong>ambassadeur passionné de la marque</strong>, d'accompagner chaque consommateur de l'accueil jusqu'à l'encaissement, et de contribuer activement à toutes les étapes du magasin (réception des livraisons, mise en rayon, conseil technique et closing). Curieux et résilient, je suis impatient de suivre votre programme certifiant et d'approfondir mes connaissances sur vos innovations produits (technologies running, textile durable, gammes Originals et Performance).
      </p>

      <p>
        Fidèle aux valeurs de diversité et d'égalité portées par adidas, j'ai à cœur d'apporter mon esprit d'équipe, ma rigueur et ma motivation communicative au service de vos objectifs collectifs. Je suis disponible immédiatement pour un contrat 35H et m'adapte aisément aux plannings du magasin.
      </p>

      <p>
        Dans l'attente d'un échange lors duquel je serai ravi de vous faire partager mon énergie et mes motivations, je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations sportives et respectueuses.
      </p>
    </div>
  </div>

  <!-- CLOSING & SIGNATURE -->
  <div class="closing-block">
    <div class="signature-box">
      <div class="signature-name">Rodrigue HESSOU</div>
      <div class="signature-title">Candidat Vendeur Polyvalent · adidas Lyon Part-Dieu</div>
    </div>
  </div>

</body>
</html>
"""

with open('Lettre_de_Motivation_Adidas_Rodrigue_HESSOU.html', 'w', encoding='utf-8') as f:
    f.write(html_letter)

print("Lettre_de_Motivation_Adidas_Rodrigue_HESSOU.html written!")

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
pdf_path = "Lettre_de_Motivation_Adidas_Rodrigue_HESSOU.pdf"

cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    "Lettre_de_Motivation_Adidas_Rodrigue_HESSOU.html"
]

subprocess.run(cmd, check=True)
print(f"PDF generated: {pdf_path}")

doc = fitz.open(pdf_path)
page_count = len(doc)
print(f"Page count: {page_count}")
assert page_count == 1, f"Expected 1 page, got {page_count}"

page = doc[0]
pix = page.get_pixmap(dpi=150)
preview_path = "Lettre_de_Motivation_Adidas_Rodrigue_HESSOU_preview.png"
pix.save(preview_path)
print(f"Preview image saved: {preview_path}")
