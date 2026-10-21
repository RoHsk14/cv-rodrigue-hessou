import subprocess
import fitz

html_letter = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Lettre de Motivation - Rodrigue HESSOU - Apple Retail</title>
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
    padding: 19mm 22mm 18mm 22mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    line-height: 1.45;
  }

  /* HEADER EXPEDITEUR / DESTINATAIRE */
  .header-block {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 5.5mm;
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
    width: 74mm;
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
    margin-bottom: 4mm;
  }

  .date-line {
    text-align: right;
    font-size: 9.2pt;
    color: #64748b;
    margin-bottom: 2.8mm;
  }

  .object-line {
    font-size: 10.2pt;
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
    gap: 3.4mm;
    font-size: 9.4pt;
    color: #262626;
    text-align: justify;
    line-height: 1.43;
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
    margin-top: 4.5mm;
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
        <div class="sender-subtitle">Candidat Spécialiste Apple Retail — Job Étudiant</div>
        <div class="sender-detail">429 Cours Émile Zola</div>
        <div class="sender-detail">69100 Villeurbanne – Lyon</div>
        <div class="sender-detail">+33 7 44 11 75 73</div>
        <div class="sender-detail">rodriguehessou14@gmail.com</div>
      </div>

      <div class="recipient-card">
        <div class="recipient-name">APPLE RETAIL FRANCE</div>
        <div class="recipient-detail">À l'attention de l'équipe Recrutement</div>
        <div class="recipient-detail">Apple Store Lyon (Part-Dieu / Confluence)</div>
        <div class="recipient-detail">Lyon, France</div>
      </div>
    </div>

    <!-- META: DATE & OBJET -->
    <div class="meta-block">
      <div class="date-line">À Lyon, le 21 octobre 2026</div>
      <div class="object-line">
        <strong>Objet :</strong> Candidature au poste de Spécialiste Apple Retail (Job Étudiant / Temps Partiel) — Réf. 114438069
      </div>
    </div>

    <!-- BODY -->
    <div class="letter-content">
      <div class="salutation">Madame, Monsieur,</div>

      <p>
        Passionné par l'univers Apple et profondément inspiré par l'expérience client unique offerte dans vos Apple Stores, je souhaite vous présenter avec enthousiasme ma candidature pour le poste de <strong>Spécialiste Apple Retail</strong>. Actuellement étudiant en Master à SUPINFO Lyon et résidant dans la métropole lyonnaise, je suis à la recherche d'un <strong>job étudiant à temps partiel</strong> et dispose d'une flexibilité horaire complète (soirées, samedis, dimanches et périodes de vacances).
      </p>

      <p>
        Ce qui m'attire particulièrement chez Apple Retail, c'est la volonté d'enrichir la vie des gens en créant une véritable relation de confiance, bien au-delà de la simple vente. Mes expériences dans le commerce et les services m'ont appris à être <strong>naturellement curieux</strong> : poser les bonnes questions, écouter activement chaque visiteur et comprendre son mode de vie afin de lui proposer une recommandation sur-mesure. Lors de mon parcours comme <strong>Employé Polyvalent au Supermarché Champion</strong>, j'ai développé une grande réactivité dans l'accueil, le conseil et l'orientation des clients, ainsi qu'une parfaite gestion des encaissements lors des pics de forte affluence, toujours avec sourire et sang-froid.
      </p>

      <p>
        Par ailleurs, mon expérience en <strong>préparation de commandes et relation client</strong> a renforcé ma rigueur logistique, mon sens du détail et mon aisance dans le closing et le suivi personnalisé. Dans le cadre de mon activité chez <strong>Nataan Group</strong>, j'ai également mené avec succès la prospection et l'accompagnement de 100 professionnels, tout en collaborant au déploiement d'une application sur l'App Store, ce qui m'a permis de maîtriser les critères d'excellence et d'accessibilité chers à Apple.
      </p>

      <p>
        À l'aise dans les environnements rythmés, j'aime m'occuper de plusieurs personnes avec la même attention et soutenir mes collègues sur le terrain. L'<strong>inclusion, l'entraide et le respect des différences</strong> sont des valeurs que je porte au quotidien. Mon aisance relationnelle ainsi que mon niveau d'anglais me permettront d'accueillir chaleureusement une clientèle variée et internationale.
      </p>

      <p>
        Rejoindre l'équipe de l'Apple Store de Lyon représente pour moi l'opportunité de partager ma passion pour vos produits et services (iPhone, Mac, iPad, Apple Watch, iCloud, AppleCare) et de faire vivre à chaque visiteur une expérience humaine inoubliable.
      </p>

      <p>
        Je me tiens à votre entière disposition pour échanger lors d'un entretien et vous faire part de ma motivation.
      </p>

      <p>
        Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.
      </p>
    </div>
  </div>

  <!-- CLOSING / SIGNATURE -->
  <div class="closing-block">
    <div class="signature-box">
      <div class="signature-name">Rodrigue HESSOU</div>
      <div class="signature-title">Candidat Spécialiste Apple Retail · SUPINFO Lyon</div>
    </div>
  </div>

</body>
</html>
"""

with open('Lettre_de_Motivation_Apple_Retail_Rodrigue_HESSOU.html', 'w', encoding='utf-8') as f:
    f.write(html_letter)

print("Lettre_de_Motivation_Apple_Retail_Rodrigue_HESSOU.html written successfully!")
