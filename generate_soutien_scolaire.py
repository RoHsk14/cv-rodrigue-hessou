import base64
import subprocess
import fitz

with open('photo.jpg', 'rb') as f:
    photo_b64 = base64.b64encode(f.read()).decode('utf-8')

# 1. CV SOUTIEN SCOLAIRE
cv_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>CV - Rodrigue HESSOU - Tuteur & Soutien Scolaire</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Carlito:ital,wght@0,400;0,700;1,400;1,700&display=swap');

  @page {{
    size: A4 portrait;
    margin: 0;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Carlito', 'Calibri', 'Segoe UI', Arial, sans-serif;
    background-color: #ffffff;
    color: #262626;
    width: 210mm;
    height: 297mm;
    margin: 0 auto;
    padding: 7.5mm 8mm 7.5mm 8mm;
    display: flex;
    flex-direction: row;
    gap: 5.5mm;
    overflow: hidden;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .sidebar {{
    width: 63mm;
    background-color: #1e293b;
    border-radius: 4px;
    padding: 4.8mm 4.5mm;
    color: #f1f5f9;
    display: flex;
    flex-direction: column;
    gap: 3.6mm;
    flex-shrink: 0;
  }}

  .photo-container {{
    text-align: center;
    margin-bottom: 0.2mm;
  }}

  .photo {{
    width: 38mm;
    height: 49mm;
    object-fit: cover;
    border-radius: 5px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    display: block;
    margin: 0 auto;
  }}

  .sidebar-section {{
    display: flex;
    flex-direction: column;
    gap: 1.2mm;
  }}

  .sidebar-title {{
    font-size: 9.8pt;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    padding-bottom: 0.6mm;
    border-bottom: 1px solid #5b7fa6;
    margin-bottom: 0.6mm;
  }}

  .sidebar-item {{
    font-size: 8.3pt;
    line-height: 1.25;
    color: #cbd5e1;
  }}

  .sidebar-item strong {{
    color: #ffffff;
    font-weight: 700;
    display: block;
    font-size: 8.5pt;
  }}

  .sidebar-item.compact {{
    line-height: 1.22;
  }}

  .sidebar-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 1.1mm;
  }}

  .sidebar-list li {{
    font-size: 8.3pt;
    line-height: 1.22;
    color: #cbd5e1;
    position: relative;
    padding-left: 3.5mm;
  }}

  .sidebar-list li::before {{
    content: "•";
    position: absolute;
    left: 0;
    color: #60a5fa;
    font-size: 9pt;
    line-height: 1;
  }}

  .main-content {{
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 2.8mm;
    min-width: 0;
  }}

  .header {{
    margin-top: 0.2mm;
    margin-bottom: 0.2mm;
  }}

  .header h1 {{
    font-size: 20.5pt;
    font-weight: 700;
    color: #1e293b;
    line-height: 1.1;
    letter-spacing: -0.3px;
  }}

  .header .subtitle {{
    font-size: 11pt;
    font-weight: 700;
    color: #2e75b6;
    margin-top: 0.6mm;
  }}

  .main-section {{
    display: flex;
    flex-direction: column;
    gap: 1.5mm;
  }}

  .main-section-title {{
    font-size: 10.5pt;
    font-weight: 700;
    color: #2e75b6;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    padding-bottom: 0.6mm;
    border-bottom: 1.5px solid #2e75b6;
  }}

  .profile-text {{
    font-size: 8.35pt;
    line-height: 1.3;
    color: #262626;
    text-align: justify;
  }}

  .experience-item {{
    display: flex;
    flex-direction: column;
    gap: 0.5mm;
  }}

  .item-title {{
    font-size: 9pt;
    font-weight: 700;
    color: #262626;
  }}

  .item-subrow {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.2pt;
    font-style: italic;
    color: #595959;
  }}

  .item-bullets {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.5mm;
    margin-top: 0.2mm;
  }}

  .item-bullets li {{
    font-size: 8.15pt;
    line-height: 1.22;
    color: #262626;
    position: relative;
    padding-left: 3.5mm;
    text-align: justify;
  }}

  .item-bullets li::before {{
    content: "•";
    position: absolute;
    left: 0;
    color: #2e75b6;
    font-size: 8.8pt;
    line-height: 1.1;
  }}

  .formation-list {{
    display: flex;
    flex-direction: column;
    gap: 1.2mm;
  }}

  .formation-item {{
    display: flex;
    flex-direction: column;
    gap: 0.2mm;
  }}

  .formation-title {{
    font-size: 8.9pt;
    font-weight: 700;
    color: #262626;
  }}

  .formation-subrow {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.1pt;
    font-style: italic;
    color: #595959;
  }}

  .keywords-block {{
    display: flex;
    flex-direction: column;
    gap: 0.7mm;
  }}

  .keyword-line {{
    font-size: 8.15pt;
    line-height: 1.22;
    color: #262626;
  }}

  .keyword-line strong {{
    color: #262626;
    font-weight: 700;
  }}
</style>
</head>
<body>

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div class="photo-container">
      <img src="data:image/jpeg;base64,{photo_b64}" alt="Rodrigue HESSOU" class="photo">
    </div>

    <!-- CONTACT -->
    <div class="sidebar-section">
      <div class="sidebar-title">Contact</div>
      <div class="sidebar-item">429 Cours Émile Zola</div>
      <div class="sidebar-item">69100 Villeurbanne – Lyon</div>
      <div class="sidebar-item">+33 7 44 11 75 73</div>
      <div class="sidebar-item">rodriguehessou14@gmail.com</div>
      <div class="sidebar-item">Né le 14/03/2006</div>
    </div>

    <!-- DISPONIBILITÉ -->
    <div class="sidebar-section">
      <div class="sidebar-title">Disponibilités</div>
      <div class="sidebar-item">
        <strong>Tutorat & Cours Particuliers</strong>
        Soirées en semaine, mercredis après-midi, week-ends et vacances scolaires
      </div>
    </div>

    <!-- MATIÈRES ENSEIGNÉES -->
    <div class="sidebar-section">
      <div class="sidebar-title">Matières Enseignées</div>
      <div class="sidebar-item">
        <strong>Mathématiques</strong>
        Collège & Lycée (Algèbre, Géométrie, Fonctions, Probabilités)
      </div>
      <div class="sidebar-item">
        <strong>Informatique & NSI / SNT</strong>
        Python, Algorithmique, Web (HTML/CSS), Bases de données
      </div>
      <div class="sidebar-item">
        <strong>Sciences & Méthodologie</strong>
        Physique-Chimie (Collège), Organisation du travail et préparation aux examens
      </div>
    </div>

    <!-- SAVOIR-ÊTRE PÉDAGOGIQUE -->
    <div class="sidebar-section">
      <div class="sidebar-title">Atouts Pédagogiques</div>
      <div class="sidebar-item">
        <strong>Patience & Écoute Active</strong>
        Capacité à débloquer les difficultés sans jugement et redonner confiance
      </div>
      <div class="sidebar-item">
        <strong>Pédagogie Adaptative</strong>
        Explications imagées et vulgarisation des concepts abstraits
      </div>
      <div class="sidebar-item">
        <strong>Suivi & Communication</strong>
        Bilans réguliers avec les parents et fixation d'objectifs hebdomadaires
      </div>
    </div>

    <!-- QUALITÉS -->
    <div class="sidebar-section">
      <div class="sidebar-title">Qualités</div>
      <ul class="sidebar-list">
        <li>Bienveillance, calme et clarté d'élocution</li>
        <li>Rigueur scientifique et esprit d'analyse</li>
        <li>Ponctualité exemplaire et assiduité</li>
        <li>Transmission du goût de l'effort</li>
      </ul>
    </div>

    <!-- CENTRES D'INTÉRÊT -->
    <div class="sidebar-section">
      <div class="sidebar-title">Centres d'intérêt</div>
      <div class="sidebar-item compact">Jeux de logique & Algorithmes</div>
      <div class="sidebar-item compact">Football & Esprit d'équipe</div>
      <div class="sidebar-item compact">Lecture & Vulgarisation scientifique</div>
    </div>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="main-content">
    <!-- HEADER -->
    <header class="header">
      <h1>Rodrigue HESSOU</h1>
      <div class="subtitle">Professeur Particulier & Tuteur de Soutien Scolaire — Maths & Sciences</div>
    </header>

    <!-- PROFIL -->
    <section class="main-section">
      <div class="main-section-title">Profil Pédagogique</div>
      <p class="profile-text">
        Étudiant en <strong>Master 1 à SUPINFO Lyon (Bac+5 en Informatique)</strong> et titulaire d'une <strong>Licence en Génie Logiciel</strong> avec un Baccalauréat Scientifique, je propose des cours de soutien scolaire et d'aide aux devoirs personnalisés pour élèves de collège et de lycée. Passionné par la transmission des savoirs, je m'appuie sur une démarche méthodique : diagnostic des lacunes, explication pas à pas des cours, exercices progressifs et techniques d'apprentissage concrètes pour redonner confiance et autonomie à l'élève. Patient, rigoureux et attentif, je veille à instaurer un climat d'échange bienveillant propice à la réussite et à l'obtention de résultats mesurables (remontée des moyennes, préparation du Brevet et du Bac).
      </p>
    </section>

    <!-- EXPÉRIENCES PROFESSIONNELLES ET TRANSMISSION -->
    <section class="main-section">
      <div class="main-section-title">Expériences de Transmission & Encadrement</div>

      <!-- SOUTIEN SCOLAIRE & TUTORAT -->
      <div class="experience-item">
        <div class="item-title">Tuteur Pédagogique & Accompagnement Individuel</div>
        <div class="item-subrow">
          <span>Cours Particuliers & Tutorat Académique</span>
          <span>2024 – 2026</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Accompagnement en Mathématiques & Sciences :</strong> Suivi individuel d'élèves de la 6e à la Terminale ; consolidation des bases, révision des théorèmes et résolution méthodique d'exercices types.</li>
          <li><strong>Méthodologie & Organisation :</strong> Apprentissage de la prise de notes efficace, gestion du temps lors des devoirs sur table, fiches de synthèse et techniques de mémorisation.</li>
          <li><strong>Motivation & Confiance :</strong> Désamorçage des blocages psychologiques face aux matières scientifiques par une pédagogie de l'encouragement et des exemples tirés du quotidien.</li>
          <li><strong>Relation Parents :</strong> Restitution transparente des progrès de l'élève après chaque séance et ajustement du plan de travail.</li>
        </ul>
      </div>

      <!-- NATAAN GROUP - PEDAGOGIE & VULGARISATION -->
      <div class="experience-item">
        <div class="item-title">Formateur & Chargé d'Onboarding Numérique</div>
        <div class="item-subrow">
          <span>Nataan Group (ESN)</span>
          <span>Juil. 2026 – Sept. 2026</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Pédagogie & Formation Utilisateurs :</strong> Formation et accompagnement personnalisé de <strong>100 professionnels</strong> à la prise en main d'outils numériques ; explication pas à pas adaptée au niveau de chaque apprenant.</li>
          <li><strong>Vulgarisation Technique :</strong> Traduction de fonctionnalités complexes en concepts simples, accessibles et intuitifs pour des publics non spécialistes.</li>
        </ul>
      </div>

      <!-- DAROLLO & ATANYS -->
      <div class="experience-item">
        <div class="item-title">Animateur d'Ateliers & Démonstrations Applicatives</div>
        <div class="item-subrow">
          <span>Darollo Technologies & ATANYS</span>
          <span>2025</span>
        </div>
        <ul class="item-bullets">
          <li>Animation de sessions de démonstration auprès d'utilisateurs finaux ; écoute active, identification immédiate des incompréhensions et reformulation claire.</li>
          <li>Développement d'une grande patience et d'une posture d'écoute bienveillante et constructive.</li>
        </ul>
      </div>

      <!-- SUPERMARCHE CHAMPION -->
      <div class="experience-item">
        <div class="item-title">Employé Polyvalent — Sens du Contact & Rigueur</div>
        <div class="item-subrow">
          <span>Supermarché Champion</span>
          <span>2024</span>
        </div>
        <ul class="item-bullets">
          <li>Écoute, sens de l'accueil, ponctualité exemplaire et rigueur dans l'organisation quotidienne.</li>
        </ul>
      </div>
    </section>

    <!-- FORMATION -->
    <section class="main-section">
      <div class="main-section-title">Formation & Parcours Académique</div>
      <div class="formation-list">
        <div class="formation-item">
          <div class="formation-title">Master 1 en Informatique (Cursus Bac+5)</div>
          <div class="formation-subrow">
            <span>SUPINFO Lyon — Lyon, France</span>
            <span>Depuis Oct. 2026</span>
          </div>
        </div>

        <div class="formation-item">
          <div class="formation-title">Licence en Génie Logiciel (Mention Bien)</div>
          <div class="formation-subrow">
            <span>IAI-TOGO (Institut Africain d'Informatique)</span>
            <span>2022 – 2025</span>
          </div>
        </div>

        <div class="formation-item">
          <div class="formation-title">Baccalauréat Scientifique (BAC 2)</div>
          <div class="formation-subrow">
            <span>LPL Le Rossignol</span>
            <span>2021 – 2022</span>
          </div>
        </div>
      </div>
    </section>

    <!-- METHODOLOGIE & ATOUTS CLES -->
    <section class="main-section">
      <div class="main-section-title">Approche Pédagogique & Compétences</div>
      <div class="keywords-block">
        <div class="keyword-line">
          <strong>Mathématiques & Logique :</strong> Algèbre, calcul littéral, géométrie, trigonométrie, analyse, probabilités, raisonnement déductif
        </div>
        <div class="keyword-line">
          <strong>Numérique & Sciences :</strong> Initiation à la programmation (Python, Scratch, Web), NSI, sciences physiques collège, pensée algorithmique
        </div>
        <div class="keyword-line">
          <strong>Méthode de Travail :</strong> Organisation des devoirs, fiches de révision, gestion du stress aux examens, autonomie de l'élève
        </div>
        <div class="keyword-line">
          <strong>Savoir-Être Pédagogique :</strong> Patience infinie, empathie, communication positive, pédagogie différenciée, écoute attentive des besoins
        </div>
        <div class="keyword-line">
          <strong>Organisation & Flexibilité :</strong> Déplacements sur Lyon et agglomération (Villeurbanne, Part-Dieu, etc.) ou cours en visioconférence
        </div>
      </div>
    </section>
  </main>

</body>
</html>
"""

with open('CV_Rodrigue_HESSOU_Soutien_Scolaire.html', 'w', encoding='utf-8') as f:
    f.write(cv_html)

# 2. LETTRE DE MOTIVATION SOUTIEN SCOLAIRE
letter_html = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Lettre de Motivation - Rodrigue HESSOU - Soutien Scolaire</title>
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
        <div class="sender-subtitle">Professeur Particulier & Tuteur de Soutien Scolaire (Bac+5)</div>
        <div class="sender-detail">429 Cours Émile Zola</div>
        <div class="sender-detail">69100 Villeurbanne – Lyon</div>
        <div class="sender-detail">+33 7 44 11 75 73</div>
        <div class="sender-detail">rodriguehessou14@gmail.com</div>
      </div>

      <div class="recipient-card">
        <div class="recipient-name">Organisme de Soutien Scolaire / Familles</div>
        <div class="recipient-detail">À l'attention de l'équipe Recrutement Pédagogique</div>
        <div class="recipient-detail">Agence Acadomia / Complétude / Anacours Lyon</div>
        <div class="recipient-detail">Lyon, France</div>
      </div>
    </div>

    <!-- META: DATE & OBJET -->
    <div class="meta-block">
      <div class="date-line">À Lyon, le 22 octobre 2026</div>
      <div class="object-line">
        <strong>Objet :</strong> Candidature comme Enseignant / Tuteur en Soutien Scolaire (Mathématiques & Sciences)
      </div>
    </div>

    <!-- CORPS DE LA LETTRE -->
    <div class="letter-content">
      <div class="salutation">Madame, Monsieur,</div>

      <p>
        Passionné par la transmission des connaissances, la pédagogie positive et l'accompagnement des jeunes vers la réussite, je vous présente avec enthousiasme ma candidature en tant qu'<strong>Enseignant en Soutien Scolaire et Aide aux Devoirs</strong>. Actuellement étudiant en <strong>Master 1 à SUPINFO Lyon (Bac+5 en Informatique)</strong> et titulaire d'une <strong>Licence en Génie Logiciel</strong> précédée d'un Baccalauréat Scientifique, je souhaite mettre ma rigueur méthodologique et ma bienveillance au service de vos élèves.
      </p>

      <p>
        Mon parcours académique m'a conféré une solide maîtrise des matières scientifiques (<strong>Mathématiques, Algorithmique, Physique et Numérique</strong>), ainsi qu'une démarche de travail structurée. Au-delà des connaissances théoriques, je suis convaincu que la clé de la réussite scolaire réside dans la relation de confiance établie avec l'élève : savoir écouter sans juger, identifier la source précise des blocages (manque de confiance, lacunes de cours ou mauvaise organisation) et réexpliquer les notions sous des angles concrets et imagés.
      </p>

      <p>
        Mes expériences m'ont permis de développer de réelles compétences pédagogiques. J'ai notamment formé plus de <strong>100 utilisateurs</strong> aux fonctionnalités d'outils numériques en adaptant mon discours au rythme de chacun, et animé des ateliers individuels de renforcement. Habitué à structurer des séances de travail complètes (rappel des points clés du cours, exercices d'application guidés, puis mise en autonomie progressive), j'accorde une importance essentielle à l'acquisition d'une méthode de travail pérenne.
      </p>

      <p>
        Mon approche s'adresse aussi bien aux élèves de <strong>collège</strong> nécessitant un cadre rassurant pour consolider leurs bases et préparer le Brevet, qu'aux lycéens préparant les épreuves du <strong>Baccalauréat</strong> ou souhaitant se perfectionner en spécialité Mathématiques et NSI. Je m'assure toujours d'un dialogue fluide et régulier avec les parents pour faire part des progrès réalisés.
      </p>

      <p>
        Ponctuel, patient, motivant et à l'écoute, je suis disponible sur toute l'agglomération lyonnaise (Villeurbanne, Lyon) ainsi qu'en distanciel, sur les créneaux de fin d'après-midi, mercredis, week-ends et vacances scolaires.
      </p>

      <p>
        Je serais ravi d'échanger avec vous lors d'un entretien afin de vous détailler mon approche pédagogique. En vous remerciant pour votre bienveillante attention, je vous prie d'agréer, Madame, Monsieur, mes salutations respectueuses.
      </p>
    </div>
  </div>

  <!-- CLOSING & SIGNATURE -->
  <div class="closing-block">
    <div class="signature-box">
      <div class="signature-name">Rodrigue HESSOU</div>
      <div class="signature-title">Étudiant Master 1 SUPINFO Lyon · Tuteur Pédagogique</div>
    </div>
  </div>

</body>
</html>
"""

with open('Lettre_de_Motivation_Soutien_Scolaire_Rodrigue_HESSOU.html', 'w', encoding='utf-8') as f:
    f.write(letter_html)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Build CV PDF
subprocess.run([
    chrome_path, "--headless", "--disable-gpu", "--no-pdf-header-footer",
    "--print-to-pdf=CV_Rodrigue_HESSOU_Soutien_Scolaire.pdf",
    "CV_Rodrigue_HESSOU_Soutien_Scolaire.html"
], check=True)

# Build Letter PDF
subprocess.run([
    chrome_path, "--headless", "--disable-gpu", "--no-pdf-header-footer",
    "--print-to-pdf=Lettre_de_Motivation_Soutien_Scolaire_Rodrigue_HESSOU.pdf",
    "Lettre_de_Motivation_Soutien_Scolaire_Rodrigue_HESSOU.html"
], check=True)

# Verify 1 page
doc1 = fitz.open("CV_Rodrigue_HESSOU_Soutien_Scolaire.pdf")
doc2 = fitz.open("Lettre_de_Motivation_Soutien_Scolaire_Rodrigue_HESSOU.pdf")
print("CV Soutien Scolaire page count:", len(doc1))
print("Letter Soutien Scolaire page count:", len(doc2))
assert len(doc1) == 1
assert len(doc2) == 1
print("SOUTIEN SCOLAIRE PERFECT 1-PAGE A4!")
