with open('photo_b64.txt', 'r') as f:
    photo_b64 = f.read().strip()

template = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Éditeur de CV Interactif - Rodrigue HESSOU</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Carlito:ital,wght@0,400;0,700;1,400;1,700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
  :root {
    --primary: #2e75b6;
    --primary-dark: #1e5a8f;
    --primary-light: #e8f2fa;
    --slate-900: #0f172a;
    --slate-800: #1e293b;
    --slate-700: #334155;
    --slate-600: #475569;
    --slate-500: #64748b;
    --slate-200: #e2e8f0;
    --slate-100: #f1f5f9;
    --slate-50: #f8fafc;
    --border: #cbd5e1;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    background-color: #0b1120;
    color: #f8fafc;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  /* TOP NAVBAR */
  .top-navbar {
    background: rgba(15, 23, 42, 0.95);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding: 12px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 50;
  }

  .nav-brand {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .nav-logo {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #2e75b6, #60a5fa);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 18px;
    color: white;
    box-shadow: 0 4px 12px rgba(46, 117, 182, 0.4);
  }

  .nav-title h1 {
    font-size: 15px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
  }

  .nav-title p {
    font-size: 11px;
    color: #94a3b8;
  }

  .nav-actions {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.15s ease;
    border: none;
    text-decoration: none;
  }

  .btn-primary {
    background: linear-gradient(135deg, #2e75b6, #2563eb);
    color: white;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
  }

  .btn-primary:hover {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(37, 99, 235, 0.45);
  }

  .btn-secondary {
    background: #1e293b;
    color: #e2e8f0;
    border: 1px solid #334155;
  }

  .btn-secondary:hover {
    background: #334155;
    color: white;
  }

  .btn-outline {
    background: transparent;
    color: #cbd5e1;
    border: 1px solid #475569;
  }

  .btn-outline:hover {
    background: rgba(255, 255, 255, 0.05);
    color: white;
  }

  /* WORKSPACE */
  .workspace {
    flex: 1;
    display: flex;
    overflow: hidden;
  }

  /* SIDEBAR CONTROLS */
  .editor-sidebar {
    width: 440px;
    background: #0f172a;
    border-right: 1px solid rgba(255, 255, 255, 0.08);
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    max-height: calc(100vh - 61px);
  }

  .sidebar-inner {
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 18px;
  }

  .card {
    background: #1e293b;
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 10px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .card-title {
    font-size: 13px;
    font-weight: 700;
    color: #f1f5f9;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .card-badge {
    font-size: 10px;
    padding: 2px 8px;
    background: rgba(46, 117, 182, 0.2);
    color: #60a5fa;
    border-radius: 999px;
    font-weight: 600;
  }

  /* PRESET BUTTONS */
  .preset-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
  }

  .btn-preset {
    background: #0f172a;
    border: 1px solid #334155;
    color: #cbd5e1;
    padding: 9px 10px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 600;
    text-align: left;
    cursor: pointer;
    transition: all 0.15s ease;
    line-height: 1.3;
  }

  .btn-preset:hover, .btn-preset.active {
    border-color: #2e75b6;
    background: rgba(46, 117, 182, 0.15);
    color: white;
  }

  /* FORM INPUTS */
  .form-group {
    display: flex;
    flex-direction: column;
    gap: 5px;
  }

  .form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }

  label {
    font-size: 11px;
    font-weight: 600;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }

  input, textarea {
    background: #0f172a;
    border: 1px solid #334155;
    border-radius: 6px;
    padding: 8px 10px;
    color: #f8fafc;
    font-size: 12.5px;
    font-family: inherit;
    transition: border-color 0.15s ease;
  }

  input:focus, textarea:focus {
    outline: none;
    border-color: #2e75b6;
    box-shadow: 0 0 0 3px rgba(46, 117, 182, 0.2);
  }

  textarea {
    resize: vertical;
    min-height: 80px;
    line-height: 1.4;
  }

  /* PREVIEW PANEL */
  .preview-panel {
    flex: 1;
    background: #0b1120;
    overflow-y: auto;
    padding: 30px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
  }

  .preview-notice {
    margin-bottom: 16px;
    background: rgba(30, 41, 59, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 12px;
    color: #94a3b8;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .preview-notice strong {
    color: #60a5fa;
  }

  /* A4 CV SHEET */
  .cv-sheet {
    width: 210mm;
    height: 297mm;
    min-height: 297mm;
    max-height: 297mm;
    background-color: #ffffff;
    color: #262626;
    margin: 0 auto;
    padding: 8.5mm;
    display: flex;
    flex-direction: row;
    gap: 6mm;
    overflow: hidden;
    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.1);
    border-radius: 2px;
    font-family: 'Carlito', 'Calibri', 'Segoe UI', Arial, sans-serif;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  /* EDITABLE STYLING IN PREVIEW */
  [contenteditable="true"] {
    outline: none;
    transition: background 0.15s ease, box-shadow 0.15s ease;
    border-radius: 3px;
    padding: 1px 2px;
    margin: -1px -2px;
  }

  [contenteditable="true"]:hover {
    background-color: rgba(46, 117, 182, 0.08);
    cursor: text;
  }

  [contenteditable="true"]:focus {
    background-color: rgba(46, 117, 182, 0.12);
    box-shadow: 0 0 0 2px rgba(46, 117, 182, 0.4);
  }

  /* LEFT SIDEBAR */
  .cv-sidebar {
    width: 63mm;
    background-color: #1f2937;
    border-radius: 4px;
    padding: 5.5mm 5mm;
    color: #f1f5f9;
    display: flex;
    flex-direction: column;
    gap: 4.2mm;
    flex-shrink: 0;
  }

  .photo-container {
    text-align: center;
    margin-bottom: 0.5mm;
    position: relative;
  }

  .photo {
    width: 39mm;
    height: 51mm;
    object-fit: cover;
    border-radius: 5px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    display: block;
    margin: 0 auto;
    cursor: pointer;
  }

  .sidebar-section {
    display: flex;
    flex-direction: column;
    gap: 1.4mm;
  }

  .sidebar-title {
    font-size: 10pt;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    padding-bottom: 0.8mm;
    border-bottom: 1px solid #5b7fa6;
    margin-bottom: 0.8mm;
  }

  .sidebar-item {
    font-size: 8.4pt;
    line-height: 1.28;
    color: #cbd5e1;
  }

  .sidebar-item strong {
    color: #ffffff;
    font-weight: 700;
    display: block;
    font-size: 8.6pt;
  }

  .sidebar-item.compact {
    line-height: 1.25;
  }

  .sidebar-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 1.2mm;
  }

  .sidebar-list li {
    font-size: 8.4pt;
    line-height: 1.24;
    color: #cbd5e1;
    position: relative;
    padding-left: 3.5mm;
  }

  .sidebar-list li::before {
    content: "•";
    position: absolute;
    left: 0;
    color: #60a5fa;
    font-size: 9.5pt;
    line-height: 1;
  }

  /* RIGHT MAIN CONTENT */
  .cv-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 3.2mm;
    min-width: 0;
  }

  .cv-header {
    margin-top: 0.5mm;
    margin-bottom: 0.5mm;
  }

  .cv-header h1 {
    font-size: 21pt;
    font-weight: 700;
    color: #1e293b;
    line-height: 1.1;
    letter-spacing: -0.3px;
  }

  .cv-header .subtitle {
    font-size: 11.5pt;
    font-weight: 700;
    color: #2e75b6;
    margin-top: 0.8mm;
  }

  .main-section {
    display: flex;
    flex-direction: column;
    gap: 1.8mm;
  }

  .main-section-title {
    font-size: 10.8pt;
    font-weight: 700;
    color: #2e75b6;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    padding-bottom: 0.7mm;
    border-bottom: 1.5px solid #2e75b6;
  }

  .profile-text {
    font-size: 8.5pt;
    line-height: 1.34;
    color: #262626;
    text-align: justify;
  }

  /* EXPERIENCES */
  .experience-item {
    display: flex;
    flex-direction: column;
    gap: 0.7mm;
  }

  .item-title {
    font-size: 9.2pt;
    font-weight: 700;
    color: #262626;
  }

  .item-subrow {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.3pt;
    font-style: italic;
    color: #595959;
  }

  .item-bullets {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.6mm;
    margin-top: 0.2mm;
  }

  .item-bullets li {
    font-size: 8.25pt;
    line-height: 1.25;
    color: #262626;
    position: relative;
    padding-left: 3.5mm;
    text-align: justify;
  }

  .item-bullets li::before {
    content: "•";
    position: absolute;
    left: 0;
    color: #2e75b6;
    font-size: 9pt;
    line-height: 1.1;
  }

  /* FORMATION */
  .formation-list {
    display: flex;
    flex-direction: column;
    gap: 1.5mm;
  }

  .formation-item {
    display: flex;
    flex-direction: column;
    gap: 0.3mm;
  }

  .formation-title {
    font-size: 9.1pt;
    font-weight: 700;
    color: #262626;
  }

  .formation-subrow {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.3pt;
    font-style: italic;
    color: #595959;
  }

  /* KEY COMPETENCES */
  .keywords-block {
    display: flex;
    flex-direction: column;
    gap: 0.9mm;
  }

  .keyword-line {
    font-size: 8.25pt;
    line-height: 1.25;
    color: #262626;
  }

  .keyword-line strong {
    color: #262626;
    font-weight: 700;
  }

  /* TOAST */
  .toast {
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: #1e293b;
    color: #ffffff;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 12px 18px;
    font-size: 13px;
    font-weight: 500;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    gap: 10px;
    transform: translateY(100px);
    opacity: 0;
    transition: all 0.25s ease;
    z-index: 100;
  }

  .toast.show {
    transform: translateY(0);
    opacity: 1;
  }

  /* PRINT STYLES */
  @media print {
    body {
      background: transparent !important;
      color: #000000 !important;
      padding: 0 !important;
      margin: 0 !important;
    }

    .top-navbar, .editor-sidebar, .preview-notice, .toast {
      display: none !important;
    }

    .workspace {
      display: block !important;
      overflow: visible !important;
    }

    .preview-panel {
      padding: 0 !important;
      background: transparent !important;
      overflow: visible !important;
      display: block !important;
    }

    .cv-sheet {
      width: 210mm !important;
      height: 297mm !important;
      min-height: 297mm !important;
      max-height: 297mm !important;
      margin: 0 !important;
      padding: 8.5mm !important;
      box-shadow: none !important;
      border: none !important;
      page-break-after: avoid !important;
      page-break-inside: avoid !important;
    }

    [contenteditable="true"] {
      outline: none !important;
      background: transparent !important;
      box-shadow: none !important;
    }

    @page {
      size: A4 portrait;
      margin: 0;
    }
  }
</style>
</head>
<body>

  <!-- TOP NAVBAR -->
  <header class="top-navbar">
    <div class="nav-brand">
      <div class="nav-logo">RH</div>
      <div class="nav-title">
        <h1>Éditeur de CV Interactif</h1>
        <p>Rodrigue HESSOU — Alternance, Stage ou Job Étudiant</p>
      </div>
    </div>

    <div class="nav-actions">
      <button class="btn btn-secondary" onclick="exportCVText()">
        📋 Copier le texte
      </button>
      <button class="btn btn-primary" onclick="printCV()">
        📥 Télécharger en PDF
      </button>
    </div>
  </header>

  <!-- WORKSPACE -->
  <div class="workspace">

    <!-- CONTROLS SIDEBAR -->
    <aside class="editor-sidebar">
      <div class="sidebar-inner">

        <!-- PRESETS DE PROFIL -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">⚡ Profils & Objectifs</span>
            <span class="card-badge">1 clic</span>
          </div>
          <div class="preset-grid">
            <button class="btn-preset active" onclick="loadCVPreset('alternance_logiciel')">
              💼 Alternance Dév. Logiciel (Java / Python / Web)
            </button>
            <button class="btn-preset" onclick="loadCVPreset('stage_mobile')">
              📱 Stage / Alt. Mobile (Flutter & iOS)
            </button>
            <button class="btn-preset" onclick="loadCVPreset('stage_qa')">
              🧪 Stage / Alt. QA & Recette Logicielle
            </button>
            <button class="btn-preset" onclick="loadCVPreset('job_etudiant')">
              🛒 Job Étudiant / Support & Données
            </button>
          </div>
        </div>

        <!-- TITRE & ACCROCHE PROFIL -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">🎯 Titre & Accroche</span>
          </div>
          <div class="form-group">
            <label>Titre Principal du CV</label>
            <input type="text" id="input-cv-title" value="Développeur Logiciel — Étudiant Master 1 (Cursus Bac+5)" oninput="syncCV('title', this.value)">
          </div>
          <div class="form-group">
            <label>Texte du Profil / Accroche</label>
            <textarea id="input-cv-profile" oninput="syncCV('profile', this.value)">Actuellement étudiant en Master 1 en Informatique à SUPINFO Lyon (cursus préparant au diplôme Bac+5) et titulaire d'une Licence en Génie Logiciel (IAI-TOGO), je dispose d'une solide expertise pratique en développement web et mobile (Flutter, iOS, Django, Laravel), en programmation orientée objet (Java, Python) et en gestion de bases de données (SQL). Mes expériences en ESN et en entreprise m'ont permis d'intervenir sur tout le cycle de vie applicatif : cadrage du besoin, architecture, développement hors ligne, recette fonctionnelle approfondie et publication sur les stores (App Store Connect). Rigoureux et adaptable, je recherche une opportunité (stage ou alternance) à Lyon pour mettre mes compétences au service de projets innovants.</textarea>
          </div>
        </div>

        <!-- COORDONNEES -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">📍 Coordonnées & Contact</span>
          </div>
          <div class="form-group">
            <label>Adresse</label>
            <input type="text" id="input-cv-addr" value="429 Cours Émile Zola" oninput="syncCV('addr', this.value)">
          </div>
          <div class="form-row">
            <div class="form-group">
              <label>Ville</label>
              <input type="text" id="input-cv-city" value="69100 Villeurbanne – Lyon" oninput="syncCV('city', this.value)">
            </div>
            <div class="form-group">
              <label>Téléphone</label>
              <input type="text" id="input-cv-phone" value="+33 7 44 11 75 73" oninput="syncCV('phone', this.value)">
            </div>
          </div>
          <div class="form-group">
            <label>Email</label>
            <input type="email" id="input-cv-email" value="rodriguehessou14@gmail.com" oninput="syncCV('email', this.value)">
          </div>
        </div>

        <!-- PHOTO -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">📷 Photo de profil</span>
          </div>
          <input type="file" id="photo-input" accept="image/*" style="display: none;" onchange="changePhoto(event)">
          <div style="display: flex; gap: 10px;">
            <button class="btn btn-secondary" style="flex: 1;" onclick="document.getElementById('photo-input').click()">
              Importer une nouvelle photo
            </button>
            <button class="btn btn-outline" onclick="resetPhoto()">
              Réinitialiser
            </button>
          </div>
        </div>

        <!-- ACTIONS -->
        <div style="display: flex; gap: 10px;">
          <button class="btn btn-outline" style="flex: 1;" onclick="resetCVToDefault()">
            🔄 Rétablir défaut
          </button>
          <button class="btn btn-primary" style="flex: 1;" onclick="printCV()">
            📥 Télécharger PDF
          </button>
        </div>

      </div>
    </aside>

    <!-- RIGHT CANVAS PREVIEW -->
    <main class="preview-panel">
      <div class="preview-notice">
        <span>💡 <strong>Astuce :</strong> Vous pouvez modifier chaque texte, mission et puce <em>directement</em> sur le CV en cliquant dessus.</span>
      </div>

      <!-- A4 PAPER SHEET -->
      <div class="cv-sheet" id="printable-cv">

        <!-- SIDEBAR -->
        <aside class="cv-sidebar">
          <div class="photo-container">
            <img src="data:image/jpeg;base64,__PHOTO_B64__" id="cv-profile-img" alt="Rodrigue HESSOU" class="photo" title="Cliquez pour changer la photo" onclick="document.getElementById('photo-input').click()">
          </div>

          <!-- CONTACT -->
          <div class="sidebar-section">
            <div class="sidebar-title">Contact</div>
            <div class="sidebar-item" id="cv-addr" contenteditable="true">429 Cours Émile Zola</div>
            <div class="sidebar-item" id="cv-city" contenteditable="true">69100 Villeurbanne – Lyon</div>
            <div class="sidebar-item" id="cv-phone" contenteditable="true">+33 7 44 11 75 73</div>
            <div class="sidebar-item" id="cv-email" contenteditable="true">rodriguehessou14@gmail.com</div>
            <div class="sidebar-item" id="cv-birth" contenteditable="true">Né le 14/03/2006</div>
          </div>

          <!-- LANGUES -->
          <div class="sidebar-section">
            <div class="sidebar-title">Langues</div>
            <div class="sidebar-item">
              <strong>Français</strong>
              Langue maternelle — courant
            </div>
            <div class="sidebar-item">
              <strong>Anglais</strong>
              Niveau B1/B2 — intermédiaire / professionnel
            </div>
          </div>

          <!-- COMPÉTENCES TECHNIQUES SIDEBAR -->
          <div class="sidebar-section" id="sidebar-skills">
            <div class="sidebar-title">Compétences Techniques</div>
            <div class="sidebar-item" id="sb-skill-1">
              <strong>Développement Mobile & Back-End</strong>
              Flutter, Dart, Java, Python, Firebase, iOS (App Store Connect, APNs)
            </div>
            <div class="sidebar-item" id="sb-skill-2">
              <strong>Développement Web & Frameworks</strong>
              Django, Laravel, PHP, JavaScript, HTML5/CSS3, Audit UI/UX
            </div>
            <div class="sidebar-item" id="sb-skill-3">
              <strong>BaaS, API & Systèmes</strong>
              Firebase (Auth, Firestore), FedaPay, REST APIs, Notifications APNs
            </div>
            <div class="sidebar-item" id="sb-skill-4">
              <strong>Assurance Qualité (QA)</strong>
              Tests unitaires, recette fonctionnelle, cahiers de tests (100+ cas)
            </div>
            <div class="sidebar-item" id="sb-skill-5">
              <strong>Bases de données</strong>
              MySQL, PostgreSQL, MariaDB, modélisation relationnelle SQL
            </div>
            <div class="sidebar-item" id="sb-skill-6">
              <strong>Méthodologie & Projets</strong>
              Git/GitHub, Agile/Scrum, Prospection B2B, Archivage client
            </div>
          </div>

          <!-- QUALITÉS -->
          <div class="sidebar-section" id="sidebar-qualities">
            <div class="sidebar-title">Qualités</div>
            <ul class="sidebar-list">
              <li contenteditable="true">Travail en équipe et collaboration</li>
              <li contenteditable="true">Rigueur, esprit d'analyse et organisation</li>
              <li contenteditable="true">Sens du détail et de la qualité logicielle</li>
              <li contenteditable="true">Capacité d'adaptation et curiosité technique</li>
            </ul>
          </div>

          <!-- CENTRES D'INTÉRÊT -->
          <div class="sidebar-section">
            <div class="sidebar-title">Centres d'intérêt</div>
            <div class="sidebar-item compact" contenteditable="true">Football</div>
            <div class="sidebar-item compact" contenteditable="true">Musique</div>
            <div class="sidebar-item compact" contenteditable="true">Veille technologique & UI/UX</div>
          </div>
        </aside>

        <!-- MAIN COLUMN -->
        <main class="cv-main">
          <!-- HEADER -->
          <header class="cv-header">
            <h1 contenteditable="true">Rodrigue HESSOU</h1>
            <div class="subtitle" id="cv-subtitle" contenteditable="true">Développeur Logiciel — Étudiant Master 1 (Cursus Bac+5)</div>
          </header>

          <!-- PROFIL -->
          <section class="main-section">
            <div class="main-section-title">Profil</div>
            <p class="profile-text" id="cv-profile-p" contenteditable="true">
              Actuellement étudiant en <strong>Master 1 en Informatique à SUPINFO Lyon (cursus préparant au diplôme Bac+5)</strong> et titulaire d'une <strong>Licence en Génie Logiciel</strong> (IAI-TOGO), je dispose d'une solide expertise pratique en développement web et mobile (Flutter, iOS, Django, Laravel), en programmation orientée objet (Java, Python) et en gestion de bases de données (SQL). Mes expériences en ESN et en entreprise m'ont permis d'intervenir sur tout le cycle de vie applicatif : cadrage du besoin, architecture, développement hors ligne, recette fonctionnelle approfondie et publication sur les stores (App Store Connect). Rigoureux et adaptable, je recherche une opportunité (stage ou alternance) à Lyon pour mettre mes compétences au service de projets innovants.
            </p>
          </section>

          <!-- EXPERIENCES -->
          <section class="main-section">
            <div class="main-section-title">Expériences Professionnelles</div>

            <!-- NATAN GROUP -->
            <div class="experience-item" id="exp-nataan">
              <div class="item-title" id="exp-nataan-title" contenteditable="true">Stagiaire — Développement Mobile, QA & Business Development</div>
              <div class="item-subrow">
                <span contenteditable="true">Nataan Group (ESN) — Lomé, Togo</span>
                <span contenteditable="true">Juil. 2026 – Sept. 2026</span>
              </div>
              <ul class="item-bullets" id="exp-nataan-bullets">
                <li contenteditable="true"><strong>Application BoutiK :</strong> Co-développement d'une application mobile de gestion de boutique / POS sous <strong>Flutter</strong>, connectée à <strong>Firebase</strong> et intégrant la passerelle de paiement <strong>FedaPay</strong>.</li>
                <li contenteditable="true"><strong>Portage & Release iOS :</strong> Portage iOS, mise en conformité avec les guidelines Apple, gestion de l'authentification OTP, push notifications <strong>APNs</strong> et publication en production via <strong>App Store Connect</strong>.</li>
                <li contenteditable="true"><strong>Assurance Qualité & Web :</strong> Conduite de la recette fonctionnelle complète d'un site institutionnel (exécution de <strong>103 cas de test</strong>), audit ergonomique UI/UX et refonte web.</li>
                <li contenteditable="true"><strong>Business Development & Données :</strong> Prospection commerciale B2B qualifiée (<strong>100 prospects ciblés</strong>) et réalisation de prestations d'archivage client.</li>
              </ul>
            </div>

            <!-- ATANYS -->
            <div class="experience-item" id="exp-atanys">
              <div class="item-title" id="exp-atanys-title" contenteditable="true">Stagiaire en Développement Web</div>
              <div class="item-subrow">
                <span contenteditable="true">ATANYS — Lomé, Togo</span>
                <span contenteditable="true">Sept. 2025 – Déc. 2025</span>
              </div>
              <ul class="item-bullets" id="exp-atanys-bullets">
                <li contenteditable="true">Conception et développement d'une plateforme web de gestion et de signalement des objets perdus et retrouvés.</li>
                <li contenteditable="true">Participation à l'ensemble du cycle de développement : analyse des besoins, modélisation de la base de données, développement et tests.</li>
              </ul>
            </div>

            <!-- DAROLLO -->
            <div class="experience-item" id="exp-darollo">
              <div class="item-title" id="exp-darollo-title" contenteditable="true">Stagiaire en Développement d'Applications</div>
              <div class="item-subrow">
                <span contenteditable="true">Darollo Technologies Corporation — Lomé, Togo</span>
                <span contenteditable="true">Juil. 2025 – Août 2025</span>
              </div>
              <ul class="item-bullets" id="exp-darollo-bullets">
                <li contenteditable="true">Développement d'une application mobile Flutter dédiée aux tailleurs pour la gestion de leur activité (prise de mesures, suivi des commandes, notifications de livraison).</li>
                <li contenteditable="true">Implémentation du fonctionnement hors ligne avec synchronisation automatique des données dès rétablissement de la connexion internet.</li>
              </ul>
            </div>

            <!-- ONG-CRISTO -->
            <div class="experience-item" id="exp-cristo">
              <div class="item-title" id="exp-cristo-title" contenteditable="true">Stagiaire en Gestion de Données</div>
              <div class="item-subrow">
                <span contenteditable="true">ONG-CRISTO — Lomé, Togo</span>
                <span contenteditable="true">Juil. 2024 – Sept. 2024</span>
              </div>
              <ul class="item-bullets" id="exp-cristo-bullets">
                <li contenteditable="true">Mise en place d'un système de gestion automatisée de la collecte d'informations pour un cabinet de recherche.</li>
                <li contenteditable="true">Structuration et fiabilisation des données collectées sur le terrain.</li>
              </ul>
            </div>
          </section>

          <!-- FORMATION -->
          <section class="main-section">
            <div class="main-section-title">Formation</div>
            <div class="formation-list">
              <div class="formation-item">
                <div class="formation-title" contenteditable="true">Master 1 en Informatique / Génie Logiciel (Cursus Bac+5)</div>
                <div class="formation-subrow">
                  <span contenteditable="true">SUPINFO Lyon — Lyon, France</span>
                  <span contenteditable="true">Depuis Oct. 2026</span>
                </div>
              </div>

              <div class="formation-item">
                <div class="formation-title" contenteditable="true">Licence en Génie Logiciel</div>
                <div class="formation-subrow">
                  <span contenteditable="true">IAI-TOGO (Institut Africain d'Informatique) — Lomé, Togo</span>
                  <span contenteditable="true">Nov. 2022 – Déc. 2025</span>
                </div>
              </div>

              <div class="formation-item">
                <div class="formation-title" contenteditable="true">Baccalauréat (BAC 2)</div>
                <div class="formation-subrow">
                  <span contenteditable="true">LPL Le Rossignol — Lomé, Togo</span>
                  <span contenteditable="true">Sept. 2021 – Juin 2022</span>
                </div>
              </div>
            </div>
          </section>

          <!-- MOTS CLES -->
          <section class="main-section">
            <div class="main-section-title">Compétences Clés (Mots-clés)</div>
            <div class="keywords-block" id="cv-keywords">
              <div class="keyword-line" id="kw-line-1" contenteditable="true">
                <strong>Langages & Frameworks :</strong> Java, Python, Flutter, Dart, Django, Laravel, PHP, HTML, CSS, JavaScript
              </div>
              <div class="keyword-line" id="kw-line-2" contenteditable="true">
                <strong>Développement mobile & Cloud :</strong> iOS (App Store Connect, APNs), Android, Flutter, Firebase, FedaPay, offline-first, synchronisation
              </div>
              <div class="keyword-line" id="kw-line-3" contenteditable="true">
                <strong>QA, Tests & Qualité :</strong> Tests unitaires, recette fonctionnelle (103 cas de test), revues de code, audit UI/UX, refonte web
              </div>
              <div class="keyword-line" id="kw-line-4" contenteditable="true">
                <strong>Bases de données :</strong> MySQL, PostgreSQL, MariaDB, Firebase Firestore, modélisation relationnelle SQL
              </div>
              <div class="keyword-line" id="kw-line-5" contenteditable="true">
                <strong>Méthodologie & Gestion :</strong> Méthodes agiles (Scrum), sécurité informatique, gestion de release, prospection B2B, travail en équipe
              </div>
            </div>
          </section>
        </main>

      </div>
    </main>

  </div>

  <!-- TOAST -->
  <div class="toast" id="toast">Message</div>

  <script>
    const defaultPhoto = "data:image/jpeg;base64,__PHOTO_B64__";

    // PRESETS FOR CV
    const cvPresets = {
      alternance_logiciel: {
        title: "Développeur Logiciel — Étudiant Master 1 (Cursus Bac+5)",
        profile: "Actuellement étudiant en <strong>Master 1 en Informatique à SUPINFO Lyon (cursus préparant au diplôme Bac+5)</strong> et titulaire d'une <strong>Licence en Génie Logiciel</strong> (IAI-TOGO), je dispose d'une solide expertise pratique en développement web et mobile (Flutter, iOS, Django, Laravel), en programmation orientée objet (Java, Python) et en gestion de bases de données (SQL). Mes expériences en ESN et en entreprise m'ont permis d'intervenir sur tout le cycle de vie applicatif : cadrage du besoin, architecture, développement hors ligne, recette fonctionnelle approfondie et publication sur les stores (App Store Connect). Rigoureux et adaptable, je recherche une <strong>alternance ou un stage</strong> à Lyon pour mettre mes compétences au service de projets innovants.",
        nataanTitle: "Stagiaire — Développement Mobile, QA & Business Development",
        nataanBullets: `
          <li contenteditable="true"><strong>Application BoutiK :</strong> Co-développement d'une application mobile de gestion de boutique / POS sous <strong>Flutter</strong>, connectée à <strong>Firebase</strong> et intégrant la passerelle de paiement <strong>FedaPay</strong>.</li>
          <li contenteditable="true"><strong>Portage & Release iOS :</strong> Portage iOS, mise en conformité avec les guidelines Apple, gestion de l'authentification OTP, push notifications <strong>APNs</strong> et publication en production via <strong>App Store Connect</strong>.</li>
          <li contenteditable="true"><strong>Assurance Qualité & Web :</strong> Conduite de la recette fonctionnelle complète d'un site institutionnel (exécution de <strong>103 cas de test</strong>), audit ergonomique UI/UX et refonte web.</li>
          <li contenteditable="true"><strong>Business Development & Données :</strong> Prospection commerciale B2B qualifiée (<strong>100 prospects ciblés</strong>) et réalisation de prestations d'archivage client.</li>
        `,
        kw1: "<strong>Langages & Frameworks :</strong> Java, Python, Flutter, Dart, Django, Laravel, PHP, HTML, CSS, JavaScript",
        kw2: "<strong>Développement mobile & Cloud :</strong> iOS (App Store Connect, APNs), Android, Flutter, Firebase, FedaPay, offline-first, synchronisation",
        kw3: "<strong>QA, Tests & Qualité :</strong> Tests unitaires, recette fonctionnelle (103 cas de test), revues de code, audit UI/UX, refonte web",
        kw4: "<strong>Bases de données :</strong> MySQL, PostgreSQL, MariaDB, Firebase Firestore, modélisation relationnelle SQL",
        kw5: "<strong>Méthodologie & Gestion :</strong> Méthodes agiles (Scrum), sécurité informatique, gestion de release, prospection B2B, travail en équipe"
      },
      stage_mobile: {
        title: "Développeur Mobile Flutter & iOS — Étudiant Master 1",
        profile: "Étudiant en <strong>Master 1 à SUPINFO Lyon (Bac+5)</strong> et passionné par le développement d'applications mobiles performantes et réactives, je maîtrise l'écosystème <strong>Flutter, Dart, Firebase</strong> ainsi que le portage et le cycle de release <strong>iOS (App Store Connect, APNs)</strong>. Fort d'expériences concrètes en ESN (co-développement de POS, intégration de passerelles de paiement FedaPay, mode offline-first), je recherche un <strong>stage ou une alternance</strong> en développement mobile pour concevoir des applications scalables et centrées sur l'expérience utilisateur.",
        nataanTitle: "Stagiaire — Développement Mobile (Flutter/iOS) & Déploiement Stores",
        nataanBullets: `
          <li contenteditable="true"><strong>Application BoutiK (POS) :</strong> Co-développement de l'application sous <strong>Flutter</strong> avec backend Firebase et intégration de la passerelle de paiement <strong>FedaPay</strong>.</li>
          <li contenteditable="true"><strong>Cycle iOS & Stores :</strong> Portage iOS intégral, conformité aux exigences de révision Apple, configuration OTP/APNs et publication en production via <strong>App Store Connect</strong>.</li>
          <li contenteditable="true"><strong>Expérience Utilisateur & Recette :</strong> Audit ergonomique UI/UX, validation fonctionnelle (103 cas de test) et optimisation des parcours marchands.</li>
          <li contenteditable="true"><strong>Déploiement & Clientèle :</strong> Prospection B2B (100 prospects commerçants) et onboarding utilisateur sur l'application.</li>
        `,
        kw1: "<strong>Mobile & Écosystème :</strong> Flutter, Dart, iOS (App Store Connect, APNs, TestFlight), Android, Architecture Offline-first",
        kw2: "<strong>Cloud, BaaS & Paiement :</strong> Firebase (Firestore, Auth, Push), FedaPay, API REST, Intégration OTP",
        kw3: "<strong>Langages & Web :</strong> Python, Django, PHP, JavaScript, HTML5/CSS3, Audit UI/UX",
        kw4: "<strong>Bases de données :</strong> Firebase Firestore, PostgreSQL, MySQL, modélisation relationnelle",
        kw5: "<strong>Méthodes & Outils :</strong> Git/GitHub, Agile/Scrum, CI/CD mobile, qualité logicielle, travail en équipe"
      },
      stage_qa: {
        title: "Ingénieur QA & Qualité Logicielle — Étudiant Master 1",
        profile: "Étudiant en <strong>Master 1 en Informatique à SUPINFO Lyon (Bac+5)</strong> avec une solide formation en génie logiciel, je combine compétences de développement (Java, Python, SQL) et expertise opérationnelle en <strong>Assurance Qualité (QA) et recette fonctionnelle</strong>. Ayant rédigé et exécuté plus d'une centaine de cas de test sur des plateformes web et mobiles, et maîtrisé les critères d'acceptation stricts d'Apple, je recherche une <strong>opportunité en alternance ou stage QA</strong> pour fiabiliser et automatiser vos processus de tests.",
        nataanTitle: "Stagiaire — Assurance Qualité (QA), Recette & Conformité Logicielle",
        nataanBullets: `
          <li contenteditable="true"><strong>Recette Fonctionnelle :</strong> Élaboration du cahier de recette et exécution complète de <strong>103 cas de test</strong> pour un site institutionnel (non-régression, cas limites).</li>
          <li contenteditable="true"><strong>Audit UI/UX & Refonte :</strong> Analyse de conformité ergonomique, identification des anomalies graphiques et participation à la refonte web.</li>
          <li contenteditable="true"><strong>Conformité Apple & Release :</strong> Audit et mise en conformité rigoureuse de l'application BoutiK avec les guidelines App Store (validation du store du premier coup).</li>
          <li contenteditable="true"><strong>Suivi Qualité & Données :</strong> Reporting d'anomalies, revues de code avec l'équipe de dev et fiabilisation de données d'archivage client.</li>
        `,
        kw1: "<strong>Assurance Qualité (QA) :</strong> Cahiers & plans de test, recette fonctionnelle, non-régression, reporting d'anomalies",
        kw2: "<strong>Conformité & Stores :</strong> Validation App Store Apple, audit UI/UX, respect des cahiers des charges",
        kw3: "<strong>Langages & Automatisation :</strong> Java, Python, SQL, Dart/Flutter, notions de tests unitaires et d'intégration",
        kw4: "<strong>Bases de données :</strong> PostgreSQL, MySQL, requêtage SQL avancé pour vérification de cohérence des données",
        kw5: "<strong>Méthodologie :</strong> Méthodes agiles (Scrum), Git/GitHub, documentation technique, rigueur d'analyse"
      },
      job_etudiant: {
        title: "Assistant Polyvalent / Support & Gestion de Données — Étudiant Master",
        profile: "Étudiant sérieux et dynamique en <strong>Master 1 à SUPINFO Lyon</strong>, je recherche un <strong>job étudiant à temps partiel</strong> (soirées, week-ends ou jours libérés) en support technique, gestion de données, relation client ou assistance polyvalente. Rigoureux, ponctuel et doté d'un excellent relationnel, je m'appuie sur une expérience solide en prospection B2B (100 prospects qualifiés), en fiabilisation de données terrain et en assistance informatique pour apporter une valeur immédiate à votre structure.",
        nataanTitle: "Assistant Polyvalent — Business Development & Gestion de Données",
        nataanBullets: `
          <li contenteditable="true"><strong>Prospection & Relation Client :</strong> Qualification ciblée de <strong>100 prospects professionnels (B2B)</strong>, prise de contact et suivi de portefeuille client.</li>
          <li contenteditable="true"><strong>Archivage & Données :</strong> Réalisation de prestations d'archivage numérique, structuration et contrôle qualité des fichiers clients.</li>
          <li contenteditable="true"><strong>Assistance Numérique :</strong> Support utilisateur, tests fonctionnels et vérification de la conformité d'outils digitaux.</li>
          <li contenteditable="true"><strong>Organisation & Rigueur :</strong> Gestion multitâche en équipe, respect rigoureux des délais et sens aigu du service.</li>
        `,
        kw1: "<strong>Relation Client & Vente :</strong> Prospection commerciale B2B, accueil, écoute active, sens du service",
        kw2: "<strong>Bureautique & Données :</strong> Excel/Sheets avancé, traitement et archivage de données, structuration SQL",
        kw3: "<strong>Compétences Numériques :</strong> Support informatique premier niveau, maintenance web, outils collaboratifs",
        kw4: "<strong>Langues :</strong> Français (courant/maternel), Anglais (professionnel B1/B2)",
        kw5: "<strong>Soft Skills :</strong> Ponctualité, rigueur, esprit d'équipe, autonomie, excellente présentation"
      }
    };

    // SYNC CONTROLS TO SHEET
    function syncCV(field, val) {
      if (field === 'title') {
        document.getElementById('cv-subtitle').innerText = val;
      } else if (field === 'profile') {
        document.getElementById('cv-profile-p').innerHTML = val;
      } else if (field === 'addr') {
        document.getElementById('cv-addr').innerText = val;
      } else if (field === 'city') {
        document.getElementById('cv-city').innerText = val;
      } else if (field === 'phone') {
        document.getElementById('cv-phone').innerText = val;
      } else if (field === 'email') {
        document.getElementById('cv-email').innerText = val;
      }
      autoSaveCV();
    }

    // LOAD PRESET
    function loadCVPreset(key) {
      document.querySelectorAll('.btn-preset').forEach(b => b.classList.remove('active'));
      if (event && event.target) {
        event.target.classList.add('active');
      }

      const data = cvPresets[key];
      if (!data) return;

      document.getElementById('input-cv-title').value = data.title;
      document.getElementById('cv-subtitle').innerText = data.title;

      document.getElementById('input-cv-profile').value = data.profile.replace(/<[^>]*>/g, '');
      document.getElementById('cv-profile-p').innerHTML = data.profile;

      document.getElementById('exp-nataan-title').innerText = data.nataanTitle;
      document.getElementById('exp-nataan-bullets').innerHTML = data.nataanBullets;

      document.getElementById('kw-line-1').innerHTML = data.kw1;
      document.getElementById('kw-line-2').innerHTML = data.kw2;
      document.getElementById('kw-line-3').innerHTML = data.kw3;
      document.getElementById('kw-line-4').innerHTML = data.kw4;
      document.getElementById('kw-line-5').innerHTML = data.kw5;

      const label = key.toUpperCase().replace('_', ' ');
      showToast("Profil " + label + " activé !");
      autoSaveCV();
    }

    // PHOTO HANDLER
    function changePhoto(e) {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function(evt) {
          document.getElementById('cv-profile-img').src = evt.target.result;
          showToast("Photo mise à jour avec succès !");
          autoSaveCV();
        };
        reader.readAsDataURL(file);
      }
    }

    function resetPhoto() {
      document.getElementById('cv-profile-img').src = defaultPhoto;
      showToast("Photo d'origine rétablie.");
      autoSaveCV();
    }

    // PRINT / EXPORT
    function printCV() {
      showToast("Génération du PDF... Sélectionnez 'Enregistrer au format PDF'");
      window.print();
    }

    function exportCVText() {
      const text = document.getElementById('printable-cv').innerText;
      navigator.clipboard.writeText(text).then(() => {
        showToast("Texte du CV copié dans le presse-papier !");
      }).catch(() => {
        showToast("Erreur lors de la copie.");
      });
    }

    // TOAST
    function showToast(msg) {
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 3000);
    }

    // AUTOSAVE
    function autoSaveCV() {
      try {
        localStorage.setItem('rodrigue_cv_saved', document.getElementById('printable-cv').innerHTML);
      } catch(e) {}
    }

    // LISTENERS
    window.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('[contenteditable="true"]').forEach(el => {
        el.addEventListener('input', autoSaveCV);
      });
    });

    function resetCVToDefault() {
      localStorage.removeItem('rodrigue_cv_saved');
      loadCVPreset('alternance_logiciel');
      resetPhoto();
      showToast("CV réinitialisé aux paramètres d'origine !");
    }
  </script>

</body>
</html>
"""

final_html = template.replace('__PHOTO_B64__', photo_b64)

with open('editeur_cv.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("editeur_cv.html written cleanly!")
