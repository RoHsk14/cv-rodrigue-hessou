import subprocess
import fitz

html_letter = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Lettre de Motivation - Rodrigue HESSOU - Conseiller de Vente & Vendeur Polyvalent</title>
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
    border-left: 3px solid #2e75b6;
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
    color: #2e75b6;
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
        <div class="sender-subtitle">Conseiller de Vente & Relation Client — Vendeur Polyvalent</div>
        <div class="sender-detail">429 Cours Émile Zola</div>
        <div class="sender-detail">69100 Villeurbanne – Lyon</div>
        <div class="sender-detail">+33 7 44 11 75 73</div>
        <div class="sender-detail">rodriguehessou14@gmail.com</div>
      </div>

      <div class="recipient-card">
        <div class="recipient-name">Direction du Magasin / Recrutement Retail</div>
        <div class="recipient-detail">À l'attention de l'équipe Recrutement</div>
        <div class="recipient-detail">Boutique / Point de Vente</div>
        <div class="recipient-detail">Lyon, France</div>
      </div>
    </div>

    <!-- META: DATE & OBJET -->
    <div class="meta-block">
      <div class="date-line">À Lyon, le 22 octobre 2026</div>
      <div class="object-line">
        <strong>Objet :</strong> Candidature au poste de Conseiller de Vente / Vendeur Polyvalent (Réf. / Rôle Magasin)
      </div>
    </div>

    <!-- CORPS DE LA LETTRE -->
    <div class="letter-content">
      <div class="salutation">Madame, Monsieur,</div>

      <p>
        Particulièrement sensible à l'excellence de l'expérience client, au rayonnement des marques de référence et aux univers de vente dynamiques, c'est avec une vive motivation que je vous propose ma candidature pour le poste de <strong>Conseiller de Vente / Vendeur Polyvalent</strong> au sein de votre point de vente lyonnais. Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, je combine rigueur méthodologique, grand sens du relationnel et passion pour le contact direct avec le public.
      </p>

      <p>
        Mes expériences sur le terrain m'ont permis de développer une réelle maîtrise des métiers du commerce de détail. Au <strong>Supermarché Champion en 2024</strong>, j'ai assuré au quotidien l'accueil chaleureux des clients, l'orientation personnalisée en rayon, l'encaissement rapide et fiable durant les pics de forte affluence, ainsi que la tenue soignée des linéaires (réassort, facing et gestion des stocks). Cette expérience m'a appris à gérer le rythme avec calme, efficacité et un sens permanent du sourire.
      </p>

      <p>
        Par ailleurs, mon travail en <strong>plateforme logistique et distribution en 2025</strong> a renforcé mon sens de l'organisation, mon respect des flux et la rigueur du contrôle qualité jusqu'à la remise au client final. Chez <strong>Nataan Group</strong>, j'ai également prospecté et conseillé plus de <strong>100 commerçants de proximité</strong> pour l'adoption d'une solution d'encaissement et de gestion de caisse, ce qui m'a sensibilisé aux <strong>indicateurs de performance commerciale (KPI retail)</strong> tels que le panier moyen, la vente complémentaire et le taux de fidélisation.
      </p>

      <p>
        Devenir ambassadeur de votre enseigne représente pour moi l'opportunité de mettre mon enthousiasme et ma polyvalence au service de votre clientèle. De la réception des livraisons jusqu'à la conclusion de la vente, j'aime comprendre les envies de chaque visiteur pour lui apporter un conseil personnalisé et valoriser l'histoire ainsi que les standards de qualité de votre maison.
      </p>

      <p>
        Reconnu pour mon esprit d'équipe, ma curiosité, ma ponctualité et mon respect bienveillant de la diversité, je m'adapte avec aisance à vos contraintes de plannings (disponible immédiatement, en semaine comme le week-end).
      </p>

      <p>
        Je serais honoré d'échanger avec vous lors d'un prochain entretien pour vous démontrer ma motivation à contribuer au succès de votre équipe. En vous remerciant de l'attention portée à ma candidature, je vous prie d'agréer, Madame, Monsieur, mes salutations respectueuses.
      </p>
    </div>
  </div>

  <!-- CLOSING & SIGNATURE -->
  <div class="closing-block">
    <div class="signature-box">
      <div class="signature-name">Rodrigue HESSOU</div>
      <div class="signature-title">Candidat Conseiller de Vente & Vendeur Polyvalent</div>
    </div>
  </div>

</body>
</html>
"""

with open('Lettre_de_Motivation_Retail_Polyvalent.html', 'w', encoding='utf-8') as f:
    f.write(html_letter)

print("Lettre_de_Motivation_Retail_Polyvalent.html written!")

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
pdf_path = "Lettre_de_Motivation_Retail_Polyvalent.pdf"

cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    "Lettre_de_Motivation_Retail_Polyvalent.html"
]

subprocess.run(cmd, check=True)
print(f"PDF generated: {pdf_path}")

doc = fitz.open(pdf_path)
page_count = len(doc)
print(f"Page count: {page_count}")
assert page_count == 1, f"Expected 1 page, got {page_count}"

page = doc[0]
pix = page.get_pixmap(dpi=150)
preview_path = "Lettre_de_Motivation_Retail_Polyvalent_preview.png"
pix.save(preview_path)
print(f"Preview image saved: {preview_path}")
