import subprocess
import fitz

html_letter = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Lettre de Motivation - Rodrigue HESSOU</title>
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
    padding: 22mm 22mm 20mm 22mm;
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
    margin-bottom: 7mm;
  }

  .sender-info {
    display: flex;
    flex-direction: column;
    gap: 1.2mm;
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
    margin-bottom: 1.5mm;
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
    width: 72mm;
    display: flex;
    flex-direction: column;
    gap: 1.2mm;
  }

  .recipient-name {
    font-size: 9.8pt;
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
    margin-bottom: 5mm;
  }

  .date-line {
    text-align: right;
    font-size: 9.2pt;
    color: #64748b;
    margin-bottom: 3.5mm;
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
    gap: 3.8mm;
    font-size: 9.5pt;
    color: #262626;
    text-align: justify;
    line-height: 1.44;
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
    margin-top: 5mm;
    display: flex;
    justify-content: flex-end;
  }

  .signature-box {
    text-align: right;
    display: flex;
    flex-direction: column;
    gap: 1.5mm;
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
        <div class="sender-subtitle">Développeur Logiciel — Étudiant en Master (Bac+5)</div>
        <div class="sender-detail">429 Cours Émile Zola</div>
        <div class="sender-detail">69100 Villeurbanne – Lyon</div>
        <div class="sender-detail">+33 7 44 11 75 73</div>
        <div class="sender-detail">rodriguehessou14@gmail.com</div>
      </div>

      <div class="recipient-card">
        <div class="recipient-name">À l'attention du Responsable du Recrutement</div>
        <div class="recipient-detail">Service des Ressources Humaines / Équipe Technique</div>
        <div class="recipient-detail">[Nom de l'entreprise]</div>
        <div class="recipient-detail">[Adresse de l'entreprise]</div>
        <div class="recipient-detail">[Code postal / Ville]</div>
      </div>
    </div>

    <!-- META: DATE & OBJET -->
    <div class="meta-block">
      <div class="date-line">À Lyon, le 20 octobre 2026</div>
      <div class="object-line">
        <strong>Objet :</strong> Candidature au poste de Développeur Logiciel (Java / Back-End & Environnements Complexes)
      </div>
    </div>

    <!-- BODY -->
    <div class="letter-content">
      <div class="salutation">Madame, Monsieur,</div>

      <p>
        Actuellement étudiant en <strong>Master en Informatique (Bac+5) à SUPINFO Lyon</strong> et titulaire d'une Licence en Génie Logiciel, je vous soumets avec enthousiasme ma candidature pour le poste de <strong>Développeur Logiciel</strong> au sein de votre équipe. Fortement attiré par la rigueur de vos solutions logicielles et par les défis techniques liés aux architectures complexes, je souhaite mettre ma solide pratique du développement et de la qualité logicielle au service de vos projets.
      </p>

      <p>
        Mon parcours technique et mes récentes expériences en ESN et en entreprise m'ont permis de développer des compétences directement transférables aux exigences de votre poste. Récemment chez <strong>Nataan Group</strong> et <strong>ATANYS</strong>, j'ai participé activement à l'ensemble du cycle de vie logiciel : analyse rigoureuse des besoins fonctionnels, modélisation relationnelle de bases de données (<strong>SQL, PostgreSQL, MySQL</strong>) et développement d'architectures applicatives robustes. Formé aux concepts avancés de la programmation orientée objet, je maîtrise le développement back-end (<strong>Java, Python</strong>) et la conception de services fiables et maintenables.
      </p>

      <p>
        Particulièrement sensible à la fiabilité et à la robustesse du code, j'ai mené avec succès des campagnes approfondies de <strong>recette fonctionnelle et de tests (plus de 100 cas de test exécutés)</strong>, tout en intégrant au quotidien les principes de revue de code, de tests unitaires et de refactorisation propre. Habitué à évoluer dans un <strong>environnement Agile (Scrum)</strong>, j'accorde une importance majeure à la rédaction d'une documentation technique claire, au suivi des versions logicielles et à l'amélioration continue des processus applicatifs.
      </p>

      <p>
        Curieux des environnements d'ingénierie avancés et des systèmes d'entreprise (outils EAM et PLM), je suis motivé à l'idée d'approfondir le paramétrage et l'intégration de telles plateformes à haute valeur ajoutée. Mon <strong>esprit d'analyse</strong>, ma <strong>rigueur méthodologique</strong>, mes qualités relationnelles ainsi que mon niveau d'anglais professionnel me permettront de m'intégrer rapidement au sein de vos équipes techniques et de collaborer efficacement avec vos experts métiers.
      </p>

      <p>
        Rejoindre votre entreprise représente pour moi une formidable opportunité de contribuer concrètement à l'évolution de vos solutions tout en renforçant mon expertise aux côtés de développeurs chevronnés.
      </p>

      <p>
        Je me tiens à votre entière disposition pour convenir d'un entretien afin de vous exposer plus en détail mes motivations et l'adéquation de mon profil avec vos attentes.
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
      <div class="signature-title">Étudiant Master SUPINFO Lyon · Développeur Logiciel</div>
    </div>
  </div>

</body>
</html>
"""

with open('Lettre_de_Motivation_Rodrigue_HESSOU.html', 'w', encoding='utf-8') as f:
    f.write(html_letter)

print("Lettre_de_Motivation_Rodrigue_HESSOU.html written successfully!")
