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
<link href="https://fonts.googleapis.com/css2?family=Carlito:ital,wght@0,400;0,700;1,400;1,700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

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
    --accent-orange: #f97316;
    --accent-green: #10b981;
  }

  *, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
    color-adjust: exact !important;
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
    width: 450px;
    background: #0f172a;
    border-right: 1px solid rgba(255, 255, 255, 0.08);
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    max-height: calc(100vh - 61px);
  }

  .sidebar-inner {
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  .card {
    background: #1e293b;
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 10px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .card-title {
    font-size: 12px;
    font-weight: 700;
    color: #f1f5f9;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .card-badge {
    font-size: 10px;
    padding: 2px 7px;
    background: rgba(46, 117, 182, 0.2);
    color: #60a5fa;
    border-radius: 999px;
    font-weight: 600;
  }

  .category-title {
    font-size: 11px;
    font-weight: 700;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 4px;
    margin-bottom: 2px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .preset-grid {
    display: flex;
    flex-direction: column;
    gap: 5px;
  }

  .btn-preset {
    background: #0f172a;
    border: 1px solid #334155;
    color: #cbd5e1;
    padding: 7px 10px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 600;
    text-align: left;
    cursor: pointer;
    transition: all 0.15s ease;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .btn-preset:hover, .btn-preset.active {
    border-color: #2e75b6;
    background: rgba(46, 117, 182, 0.18);
    color: white;
  }

  .btn-preset.active::after {
    content: "✓";
    color: #60a5fa;
    font-weight: 700;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
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
    padding: 7px 9px;
    color: #f8fafc;
    font-size: 12px;
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
    min-height: 65px;
    line-height: 1.4;
  }

  .quick-helper-box {
    background: rgba(46, 117, 182, 0.1);
    border: 1px dashed rgba(96, 165, 250, 0.4);
    border-radius: 6px;
    padding: 8px 10px;
    font-size: 11px;
    color: #cbd5e1;
    line-height: 1.4;
  }

  /* PREVIEW PANEL */
  .preview-panel {
    flex: 1;
    background: #0b1120;
    overflow-y: auto;
    padding: 24px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
  }

  .preview-notice {
    margin-bottom: 14px;
    background: rgba(30, 41, 59, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 7px 14px;
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

  /* A4 SHEET STYLING */
  .cv-sheet {
    width: 210mm;
    height: 297mm;
    min-height: 297mm;
    max-height: 297mm;
    background: #ffffff;
    color: #262626;
    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.1);
    border-radius: 2px;
    font-family: 'Carlito', 'Calibri', 'Segoe UI', Arial, sans-serif;
    padding: 7.5mm 8mm 7.5mm 8mm;
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    gap: 5.5mm;
    overflow: hidden;
    position: relative;
  }

  /* EDITABLE STYLING IN PREVIEW */
  [contenteditable="true"] {
    outline: none;
    transition: background 0.15s ease, box-shadow 0.15s ease;
    border-radius: 2px;
  }

  [contenteditable="true"]:hover {
    background-color: rgba(46, 117, 182, 0.08);
    cursor: text;
  }

  [contenteditable="true"]:focus {
    background-color: rgba(46, 117, 182, 0.12);
    box-shadow: 0 0 0 1.5px rgba(46, 117, 182, 0.4);
  }

  /* SIDEBAR IN CV */
  .cv-sidebar {
    width: 63mm;
    background-color: #1e293b !important;
    background: #1e293b !important;
    box-shadow: inset 0 0 0 1000px #1e293b !important;
    border-radius: 4px;
    padding: 4.8mm 4.5mm;
    color: #f1f5f9 !important;
    display: flex;
    flex-direction: column;
    gap: 3.6mm;
    flex-shrink: 0;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
    color-adjust: exact !important;
  }

  .photo-container {
    text-align: center;
    margin-bottom: 0.2mm;
    position: relative;
  }

  .photo {
    width: 38mm;
    height: 49mm;
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
    gap: 1.2mm;
  }

  .sidebar-title {
    font-size: 9.8pt;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    padding-bottom: 0.6mm;
    border-bottom: 1px solid #5b7fa6;
    margin-bottom: 0.6mm;
  }

  .sidebar-item {
    font-size: 8.3pt;
    line-height: 1.25;
    color: #cbd5e1;
  }

  .sidebar-item strong {
    color: #ffffff;
    font-weight: 700;
    display: block;
    font-size: 8.5pt;
  }

  .sidebar-item.compact {
    line-height: 1.22;
  }

  .sidebar-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 1.1mm;
  }

  .sidebar-list li {
    font-size: 8.3pt;
    line-height: 1.22;
    color: #cbd5e1;
    position: relative;
    padding-left: 3.5mm;
  }

  .sidebar-list li::before {{
    content: "•";
    position: absolute;
    left: 0;
    color: #60a5fa;
    font-size: 9pt;
    line-height: 1;
  }}

  /* MAIN COLUMN IN CV */
  .cv-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 2.8mm;
    min-width: 0;
  }

  .cv-header {
    margin-top: 0.2mm;
    margin-bottom: 0.2mm;
  }

  .cv-header h1 {
    font-size: 20.5pt;
    font-weight: 700;
    color: #1e293b;
    line-height: 1.1;
    letter-spacing: -0.3px;
  }

  .cv-header .subtitle {
    font-size: 11pt;
    font-weight: 700;
    color: #2e75b6;
    margin-top: 0.6mm;
  }

  .main-section {
    display: flex;
    flex-direction: column;
    gap: 1.5mm;
  }

  .main-section-title {
    font-size: 10.5pt;
    font-weight: 700;
    color: #2e75b6;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    padding-bottom: 0.6mm;
    border-bottom: 1.5px solid #2e75b6;
  }

  .profile-text {
    font-size: 8.35pt;
    line-height: 1.3;
    color: #262626;
    text-align: justify;
  }

  /* EXPERIENCES */
  .experience-item {
    display: flex;
    flex-direction: column;
    gap: 0.5mm;
  }

  .item-title {
    font-size: 9pt;
    font-weight: 700;
    color: #262626;
  }

  .item-subrow {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.2pt;
    font-style: italic;
    color: #595959;
  }

  .item-bullets {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.5mm;
    margin-top: 0.2mm;
  }

  .item-bullets li {
    font-size: 8.15pt;
    line-height: 1.22;
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
    font-size: 8.8pt;
    line-height: 1.1;
  }

  /* FORMATION */
  .formation-list {
    display: flex;
    flex-direction: column;
    gap: 1.2mm;
  }

  .formation-item {
    display: flex;
    flex-direction: column;
    gap: 0.2mm;
  }

  .formation-title {
    font-size: 8.9pt;
    font-weight: 700;
    color: #262626;
  }

  .formation-subrow {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.1pt;
    font-style: italic;
    color: #595959;
  }

  /* KEY COMPETENCES */
  .keywords-block {
    display: flex;
    flex-direction: column;
    gap: 0.7mm;
  }

  .keyword-line {
    font-size: 8.15pt;
    line-height: 1.22;
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

  /* PRINT STYLES - 1 PAGE A4 STRICT */
  @media print {
    *, *::before, *::after {
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      color-adjust: exact !important;
    }

    html, body {
      background: transparent !important;
      color: #000000 !important;
      padding: 0 !important;
      margin: 0 !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      color-adjust: exact !important;
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
      margin: 0 auto !important;
      padding: 7.5mm 8mm 7.5mm 8mm !important;
      box-shadow: none !important;
      border: none !important;
      page-break-after: avoid !important;
      page-break-inside: avoid !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      color-adjust: exact !important;
    }

    .cv-sidebar {
      background-color: #1e293b !important;
      background: #1e293b !important;
      box-shadow: inset 0 0 0 1000px #1e293b !important;
      color: #f1f5f9 !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      color-adjust: exact !important;
    }

    .sidebar-title {
      color: #ffffff !important;
      border-bottom: 1px solid #5b7fa6 !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }

    .sidebar-item {
      color: #cbd5e1 !important;
    }

    .sidebar-item strong {
      color: #ffffff !important;
    }

    .sidebar-list li {
      color: #cbd5e1 !important;
    }

    .sidebar-list li::before {
      background-color: #60a5fa !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }

    .lang-level {
      color: #93c5fd !important;
    }

    .cv-main-title {
      color: #1e5a8f !important;
      border-bottom: 1.5px solid #2e75b6 !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }

    .main-section-title {
      color: #2e75b6 !important;
      border-bottom: 1.5px solid #2e75b6 !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }

    .cv-header .subtitle {
      color: #2e75b6 !important;
    }

    .item-bullets li::before {
      color: #2e75b6 !important;
    }

    .role-badge {
      background-color: #eff6ff !important;
      color: #1d4ed8 !important;
      border: 1px solid #bfdbfe !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
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
        <p>Rodrigue HESSOU — Jobs Étudiants, Retail & Ingénierie Bac+5</p>
      </div>
    </div>

    <div class="nav-actions">
      <a id="btn-download-preset-pdf" href="CV_Rodrigue_HESSOU_Soutien_Scolaire.pdf" download class="btn btn-secondary" title="Télécharger directement le PDF officiel pré-généré avec le bandeau bleu">
        ⚡ PDF Officiel Direct
      </a>
      <button class="btn btn-secondary" onclick="exportCVText()">
        📋 Copier le texte
      </button>
      <button class="btn btn-primary" onclick="printCV()">
        🖨️ Télécharger en PDF
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
            <span class="card-title">⚡ Modèles Prédéfinis</span>
            <span class="card-badge">1 clic</span>
          </div>

          <div class="category-title">🎓 Jobs Étudiants Polyvalents</div>
          <div class="preset-grid">
            <button class="btn-preset active" onclick="loadCVPreset('soutien_scolaire')">
              <span>🎓 Soutien Scolaire & Tutorat (Maths / Sciences)</span>
            </button>
            <button class="btn-preset" onclick="loadCVPreset('macdo')">
              <span>🍔 McDonald's & Fast-Food (Équipier Polyvalent)</span>
            </button>
            <button class="btn-preset" onclick="loadCVPreset('hote_caisse_rayon')">
              <span>🛒 Hôte de Caisse / Rayon (Grande Distribution)</span>
            </button>
            <button class="btn-preset" onclick="loadCVPreset('agent_accueil')">
              <span>🎟️ Agent d'Accueil & Cinéma (UGC / Événements)</span>
            </button>
          </div>

          <div class="category-title" style="margin-top: 6px;">👟 Vente, Commerce & Marques</div>
          <div class="preset-grid">
            <button class="btn-preset" onclick="loadCVPreset('adidas')">
              <span>👟 adidas Part-Dieu (Vendeur Polyvalent)</span>
            </button>
            <button class="btn-preset" onclick="loadCVPreset('apple')">
              <span>🍏 Apple Retail (Spécialiste #114438069)</span>
            </button>
            <button class="btn-preset" onclick="loadCVPreset('retail_polyvalent')">
              <span>🛍️ Conseiller de Vente (Commerce Généraliste)</span>
            </button>
            <button class="btn-preset" onclick="loadCVPreset('sephora')">
              <span>💄 Sephora / Beauté & Cosmétiques</span>
            </button>
            <button class="btn-preset" onclick="loadCVPreset('hermes')">
              <span>👜 Hermès / Luxe & Expérience Client</span>
            </button>
          </div>

          <div class="category-title" style="margin-top: 6px;">💼 Tech & Ingénierie Bac+5</div>
          <div class="preset-grid">
            <button class="btn-preset" onclick="loadCVPreset('alternance_logiciel')">
              <span>💻 Alternance Dév. Logiciel (Java/Python)</span>
            </button>
            <button class="btn-preset" onclick="loadCVPreset('stage_mobile')">
              <span>📱 Stage / Alt. Mobile (Flutter & iOS)</span>
            </button>
            <button class="btn-preset" onclick="loadCVPreset('stage_qa')">
              <span>🧪 Stage / Alt. QA & Recette Logicielle</span>
            </button>
          </div>
        </div>

        <!-- ASSOCIER UNE OFFRE / NUMERO DE ROLE -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">🏷️ Offre, Marque & Rôle</span>
          </div>
          <div class="quick-helper-box">
            Associez le <strong>numéro de rôle</strong> ou la référence de l'offre et l'enseigne ciblée pour adapter le titre en direct.
          </div>
          <div class="form-row">
            <div class="form-group">
              <label>Enseigne / Établissement</label>
              <input type="text" id="input-brand" value="Acadomia / Complétude" placeholder="ex: McDonald's, Acadomia..." oninput="updateCVTitleFromInputs()">
            </div>
            <div class="form-group">
              <label>N° Rôle / Référence</label>
              <input type="text" id="input-role-ref" value="Tutorat Lyon" placeholder="ex: 114438069, Réf. Soirs..." oninput="updateCVTitleFromInputs()">
            </div>
          </div>
          <div class="form-group">
            <label>Intitulé du poste ciblé</label>
            <input type="text" id="input-job-role" value="Professeur Particulier & Tuteur Soutien Scolaire" placeholder="ex: Équipier Polyvalent, Tuteur..." oninput="updateCVTitleFromInputs()">
          </div>
        </div>

        <!-- TITRE & ACCROCHE PROFIL -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">🎯 Titre & Accroche</span>
          </div>
          <div class="form-group">
            <label>Titre Affiché sur le CV</label>
            <input type="text" id="input-cv-title" value="Professeur Particulier & Tuteur de Soutien Scolaire — Maths & Sciences" oninput="syncCV('title', this.value)">
          </div>
          <div class="form-group">
            <label>Texte du Profil / Accroche</label>
            <textarea id="input-cv-profile" oninput="syncCV('profile', this.value)">Étudiant en Master 1 à SUPINFO Lyon (Bac+5 en Informatique) et titulaire d'une Licence en Génie Logiciel avec un Baccalauréat Scientifique, je propose des cours de soutien scolaire et d'aide aux devoirs personnalisés pour élèves de collège et de lycée. Passionné par la transmission des savoirs, je m'appuie sur une démarche méthodique : diagnostic des lacunes, explication pas à pas des cours, exercices progressifs et techniques d'apprentissage concrètes pour redonner confiance et autonomie à l'élève. Patient, rigoureux et attentif, je veille à instaurer un climat d'échange bienveillant propice à la réussite et à l'obtention de résultats mesurables.</textarea>
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
          <div style="display: flex; gap: 8px;">
            <button class="btn btn-secondary" style="flex: 1;" onclick="document.getElementById('photo-input').click()">
              Importer photo
            </button>
            <button class="btn btn-outline" onclick="resetPhoto()">
              Réinitialiser
            </button>
          </div>
        </div>

        <!-- ACTIONS -->
        <div style="display: flex; gap: 8px;">
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
        <span>💡 <strong>Astuce Impression :</strong> En téléchargeant en PDF, vérifiez que l'option <strong>« Graphiques d'arrière-plan »</strong> (Background graphics) est cochée dans votre fenêtre d'impression pour conserver la colonne bleue nuit à gauche, ou utilisez le bouton direct <strong>« ⚡ PDF Officiel Direct »</strong> !</span>
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

          <!-- DISPONIBILITÉ -->
          <div class="sidebar-section" id="sb-dispo-sec">
            <div class="sidebar-title">Disponibilités</div>
            <div class="sidebar-item" id="sb-dispo-item" contenteditable="true">
              <strong>Tutorat & Cours Particuliers</strong>
              Soirées en semaine, mercredis après-midi, week-ends et vacances scolaires
            </div>
          </div>

          <!-- LANGUES -->
          <div class="sidebar-section">
            <div class="sidebar-title">Langues</div>
            <div class="sidebar-item">
              <strong>Français</strong>
              Langue maternelle — élocution soignée
            </div>
            <div class="sidebar-item">
              <strong>Anglais</strong>
              Niveau B1/B2 — pratique courante
            </div>
          </div>

          <!-- COMPÉTENCES / ATOUTS SIDEBAR -->
          <div class="sidebar-section" id="sidebar-skills">
            <div class="sidebar-title" id="sb-skills-title">Atouts Pédagogiques</div>
            <div class="sidebar-item" id="sb-skill-1" contenteditable="true">
              <strong>Patience & Écoute Active</strong>
              Capacité à débloquer les difficultés sans jugement et redonner confiance
            </div>
            <div class="sidebar-item" id="sb-skill-2" contenteditable="true">
              <strong>Pédagogie Adaptative</strong>
              Explications imagées et vulgarisation des concepts abstraits
            </div>
            <div class="sidebar-item" id="sb-skill-3" contenteditable="true">
              <strong>Suivi & Communication</strong>
              Bilans réguliers avec les parents et fixation d'objectifs hebdomadaires
            </div>
            <div class="sidebar-item" id="sb-skill-4" contenteditable="true">
              <strong>Rigueur Scientifique</strong>
              Culture des mathématiques, logique algorithmique et sciences physiques
            </div>
            <div class="sidebar-item" id="sb-skill-5" contenteditable="true">
              <strong>Méthodologie d'Examen</strong>
              Préparation au Brevet des collèges et épreuves du Baccalauréat
            </div>
          </div>

          <!-- QUALITÉS -->
          <div class="sidebar-section" id="sidebar-qualities">
            <div class="sidebar-title">Qualités</div>
            <ul class="sidebar-list" id="sb-qualities-list">
              <li contenteditable="true">Bienveillance, calme et clarté d'élocution</li>
              <li contenteditable="true">Rigueur scientifique et esprit d'analyse</li>
              <li contenteditable="true">Ponctualité exemplaire et assiduité</li>
              <li contenteditable="true">Transmission du goût de l'effort</li>
            </ul>
          </div>

          <!-- CENTRES D'INTÉRÊT -->
          <div class="sidebar-section" id="sidebar-interests">
            <div class="sidebar-title">Centres d'intérêt</div>
            <div class="sidebar-item compact" id="sb-int-1" contenteditable="true">Jeux de logique & Algorithmes</div>
            <div class="sidebar-item compact" id="sb-int-2" contenteditable="true">Football & Esprit d'équipe</div>
            <div class="sidebar-item compact" id="sb-int-3" contenteditable="true">Lecture & Vulgarisation scientifique</div>
          </div>
        </aside>

        <!-- MAIN COLUMN -->
        <main class="cv-main">
          <!-- HEADER -->
          <header class="cv-header">
            <h1 contenteditable="true">Rodrigue HESSOU</h1>
            <div class="subtitle" id="cv-subtitle" contenteditable="true">Professeur Particulier & Tuteur de Soutien Scolaire — Maths & Sciences</div>
          </header>

          <!-- PROFIL -->
          <section class="main-section">
            <div class="main-section-title" id="sec-profile-title">Profil Pédagogique</div>
            <p class="profile-text" id="cv-profile-p" contenteditable="true">
              Étudiant en <strong>Master 1 à SUPINFO Lyon (Bac+5 en Informatique)</strong> et titulaire d'une <strong>Licence en Génie Logiciel</strong> avec un Baccalauréat Scientifique, je propose des cours de soutien scolaire et d'aide aux devoirs personnalisés pour élèves de collège et de lycée. Passionné par la transmission des savoirs, je m'appuie sur une démarche méthodique : diagnostic des lacunes, explication pas à pas des cours, exercices progressifs et techniques d'apprentissage concrètes pour redonner confiance et autonomie à l'élève. Patient, rigoureux et attentif, je veille à instaurer un climat d'échange bienveillant propice à la réussite et à l'obtention de résultats mesurables.
            </p>
          </section>

          <!-- EXPERIENCES -->
          <section class="main-section">
            <div class="main-section-title">Expériences de Transmission & Encadrement</div>

            <div id="experiences-container">
              <!-- CONTENU DYNAMIQUE DES EXPERIENCES -->
            </div>
          </section>

          <!-- FORMATION -->
          <section class="main-section">
            <div class="main-section-title">Formation & Parcours Académique</div>
            <div class="formation-list">
              <div class="formation-item">
                <div class="formation-title" contenteditable="true">Master 1 en Informatique (Cursus Bac+5)</div>
                <div class="formation-subrow">
                  <span contenteditable="true">SUPINFO Lyon — Lyon, France</span>
                  <span contenteditable="true">Depuis Oct. 2026</span>
                </div>
              </div>

              <div class="formation-item">
                <div class="formation-title" contenteditable="true">Licence en Génie Logiciel (Mention Bien)</div>
                <div class="formation-subrow">
                  <span contenteditable="true">IAI-TOGO (Institut Africain d'Informatique)</span>
                  <span contenteditable="true">2022 – 2025</span>
                </div>
              </div>

              <div class="formation-item">
                <div class="formation-title" contenteditable="true">Baccalauréat Scientifique (BAC 2)</div>
                <div class="formation-subrow">
                  <span contenteditable="true">LPL Le Rossignol</span>
                  <span contenteditable="true">2021 – 2022</span>
                </div>
              </div>
            </div>
          </section>

          <!-- MOTS CLES -->
          <section class="main-section">
            <div class="main-section-title" id="sec-keywords-title">Approche Pédagogique & Compétences</div>
            <div class="keywords-block" id="cv-keywords">
              <div class="keyword-line" id="kw-line-1" contenteditable="true">
                <strong>Mathématiques & Logique :</strong> Algèbre, calcul littéral, géométrie, trigonométrie, analyse, probabilités, raisonnement déductif
              </div>
              <div class="keyword-line" id="kw-line-2" contenteditable="true">
                <strong>Numérique & Sciences :</strong> Initiation à la programmation (Python, Scratch, Web), NSI, sciences physiques collège, pensée algorithmique
              </div>
              <div class="keyword-line" id="kw-line-3" contenteditable="true">
                <strong>Méthode de Travail :</strong> Organisation des devoirs, fiches de révision, gestion du stress aux examens, autonomie de l'élève
              </div>
              <div class="keyword-line" id="kw-line-4" contenteditable="true">
                <strong>Savoir-Être Pédagogique :</strong> Patience infinie, empathie, communication positive, pédagogie différenciée, écoute attentive des besoins
              </div>
              <div class="keyword-line" id="kw-line-5" contenteditable="true">
                <strong>Organisation & Flexibilité :</strong> Déplacements sur Lyon et agglomération (Villeurbanne, Part-Dieu, etc.) ou cours en visioconférence
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

    // EXP TEMPLATES
    const tutoratExpHTML = `
      <div class="experience-item" id="exp-1">
        <div class="item-title" id="exp-1-title" contenteditable="true">Tuteur Pédagogique & Accompagnement Individuel</div>
        <div class="item-subrow">
          <span id="exp-1-comp" contenteditable="true">Cours Particuliers & Tutorat Académique</span>
          <span id="exp-1-date" contenteditable="true">2024 – 2026</span>
        </div>
        <ul class="item-bullets" id="exp-1-bullets">
          <li contenteditable="true"><strong>Accompagnement en Mathématiques & Sciences :</strong> Suivi individuel d'élèves de la 6e à la Terminale ; consolidation des bases, révision des théorèmes et résolution méthodique d'exercices types.</li>
          <li contenteditable="true"><strong>Méthodologie & Organisation :</strong> Apprentissage de la prise de notes efficace, gestion du temps lors des devoirs sur table, fiches de synthèse et techniques de mémorisation.</li>
          <li contenteditable="true"><strong>Motivation & Confiance :</strong> Désamorçage des blocages psychologiques face aux matières scientifiques par une pédagogie de l'encouragement et des exemples concrets.</li>
          <li contenteditable="true"><strong>Relation Parents :</strong> Restitution transparente des progrès de l'élève après chaque séance et ajustement du plan de travail.</li>
        </ul>
      </div>

      <div class="experience-item" id="exp-2">
        <div class="item-title" id="exp-2-title" contenteditable="true">Formateur & Chargé d'Onboarding Numérique</div>
        <div class="item-subrow">
          <span id="exp-2-comp" contenteditable="true">Nataan Group (ESN)</span>
          <span id="exp-2-date" contenteditable="true">Juil. 2026 – Sept. 2026</span>
        </div>
        <ul class="item-bullets" id="exp-2-bullets">
          <li contenteditable="true"><strong>Pédagogie & Formation Utilisateurs :</strong> Formation et accompagnement personnalisé de <strong>100 professionnels</strong> à la prise en main d'outils numériques ; explication pas à pas adaptée au niveau de chaque apprenant.</li>
          <li contenteditable="true"><strong>Vulgarisation Technique :</strong> Traduction de fonctionnalités complexes en concepts simples, accessibles et intuitifs pour des publics non spécialistes.</li>
        </ul>
      </div>

      <div class="experience-item" id="exp-3">
        <div class="item-title" id="exp-3-title" contenteditable="true">Animateur d'Ateliers & Démonstrations Applicatives</div>
        <div class="item-subrow">
          <span id="exp-3-comp" contenteditable="true">Darollo Technologies & ATANYS</span>
          <span id="exp-3-date" contenteditable="true">2025</span>
        </div>
        <ul class="item-bullets" id="exp-3-bullets">
          <li contenteditable="true">Animation de sessions de démonstration auprès d'utilisateurs finaux ; écoute active, identification immédiate des incompréhensions et reformulation claire.</li>
          <li contenteditable="true">Développement d'une grande patience et d'une posture d'écoute bienveillante et constructive.</li>
        </ul>
      </div>

      <div class="experience-item" id="exp-4">
        <div class="item-title" id="exp-4-title" contenteditable="true">Employé Polyvalent — Sens du Contact & Rigueur</div>
        <div class="item-subrow">
          <span id="exp-4-comp" contenteditable="true">Supermarché Champion</span>
          <span id="exp-4-date" contenteditable="true">2024</span>
        </div>
        <ul class="item-bullets" id="exp-4-bullets">
          <li contenteditable="true">Écoute, sens de l'accueil, ponctualité exemplaire et rigueur dans l'organisation quotidienne.</li>
        </ul>
      </div>
    `;

    const macdoExpHTML = `
      <div class="experience-item" id="exp-1">
        <div class="item-title" id="exp-1-title" contenteditable="true">Employé Commercial & Polyvalent — Caisse & Gestion des Flux</div>
        <div class="item-subrow">
          <span id="exp-1-comp" contenteditable="true">Supermarché Champion</span>
          <span id="exp-1-date" contenteditable="true">2024</span>
        </div>
        <ul class="item-bullets" id="exp-1-bullets">
          <li contenteditable="true"><strong>Encaissement en Pic de Rush :</strong> Enregistrement rapide et sans erreur des commandes en période de forte affluence ; tenue de caisse exacte et sens du sourire.</li>
          <li contenteditable="true"><strong>Accueil & Orientation Client :</strong> Prise en charge bienveillante, écoute active des demandes et gestion fluide des réclamations avec calme et courtoisie.</li>
          <li contenteditable="true"><strong>Entretien & Propreté :</strong> Maintien constant de la propreté des postes de travail et de l'espace de vente dans le respect des règles d'hygiène.</li>
          <li contenteditable="true"><strong>Travail d'Équipe & Entraide :</strong> Coordination avec les équipiers pour fluidifier le passage des clients et limiter le temps d'attente.</li>
        </ul>
      </div>

      <div class="experience-item" id="exp-2">
        <div class="item-title" id="exp-2-title" contenteditable="true">Préparateur de Commandes — Cadence & Rigueur</div>
        <div class="item-subrow">
          <span id="exp-2-comp" contenteditable="true">Plateforme Logistique & Distribution</span>
          <span id="exp-2-date" contenteditable="true">2025</span>
        </div>
        <ul class="item-bullets" id="exp-2-bullets">
          <li contenteditable="true"><strong>Respect des Cadences :</strong> Préparation et conditionnement minutieux de commandes à rythme soutenu tout en maintenant un niveau de qualité constant.</li>
          <li contenteditable="true"><strong>Hygiène & Sécurité :</strong> Application stricte des consignes de sécurité, de rangement et de manipulation des produits.</li>
          <li contenteditable="true"><strong>Endurance & Réactivité :</strong> Aptitude physique au travail dynamique debout et esprit de cohésion collective.</li>
        </ul>
      </div>

      <div class="experience-item" id="exp-3">
        <div class="item-title" id="exp-3-title" contenteditable="true">Chargé de Prospection Commerciale & Déploiement POS</div>
        <div class="item-subrow">
          <span id="exp-3-comp" contenteditable="true">Nataan Group (ESN)</span>
          <span id="exp-3-date" contenteditable="true">Juil. 2026 – Sept. 2026</span>
        </div>
        <ul class="item-bullets" id="exp-3-bullets">
          <li contenteditable="true"><strong>Relationnel Client Terrain :</strong> Contact direct avec <strong>100 commerçants et restaurateurs</strong> ; écoute de leurs besoins et présentation de solutions de caisse.</li>
          <li contenteditable="true"><strong>Rigueur Opérationnelle :</strong> Sens du détail, organisation des priorités et fiabilité dans l'exécution des missions.</li>
        </ul>
      </div>

      <div class="experience-item" id="exp-4">
        <div class="item-title" id="exp-4-title" contenteditable="true">Conseiller Utilisateurs & Sens du Service</div>
        <div class="item-subrow">
          <span id="exp-4-comp" contenteditable="true">Darollo Technologies & ATANYS</span>
          <span id="exp-4-date" contenteditable="true">2025</span>
        </div>
        <ul class="item-bullets" id="exp-4-bullets">
          <li contenteditable="true">Écoute attentive, sens du service et volonté constante de satisfaire l'utilisateur final.</li>
        </ul>
      </div>
    `;

    const retailExpHTML = `
      <div class="experience-item" id="exp-1">
        <div class="item-title" id="exp-1-title" contenteditable="true">Employé Commercial & Polyvalent — Vente & Relation Client</div>
        <div class="item-subrow">
          <span id="exp-1-comp" contenteditable="true">Supermarché Champion</span>
          <span id="exp-1-date" contenteditable="true">2024</span>
        </div>
        <ul class="item-bullets" id="exp-1-bullets">
          <li contenteditable="true"><strong>Accueil & Conseil Client :</strong> Accueil personnalisé des visiteurs, écoute attentive des besoins, orientation immédiate et valorisation des offres du magasin.</li>
          <li contenteditable="true"><strong>Encaissement & Gestion d'Affluence :</strong> Gestion rapide et rigoureuse des encaissements lors des pics de forte affluence ; fidélisation et gestion bienveillante des réclamations.</li>
          <li contenteditable="true"><strong>Tenue de Rayon & Merchandising :</strong> Réassort quotidien, respect des standards de facing et de propreté, contrôle minutieux des stocks et des dates de péremption.</li>
          <li contenteditable="true"><strong>Travail d'Équipe & Polyvalence :</strong> Entraide active avec l'équipe pour garantir la fluidité opérationnelle et la satisfaction totale de chaque client.</li>
        </ul>
      </div>

      <div class="experience-item" id="exp-2">
        <div class="item-title" id="exp-2-title" contenteditable="true">Préparateur de Commandes & Relation Client</div>
        <div class="item-subrow">
          <span id="exp-2-comp" contenteditable="true">Plateforme Logistique & Distribution</span>
          <span id="exp-2-date" contenteditable="true">2025</span>
        </div>
        <ul class="item-bullets" id="exp-2-bullets">
          <li contenteditable="true"><strong>Rigueur Opérationnelle :</strong> Réception, contrôle conformité, préparation minutieuse et emballage des commandes selon les normes d'exigence et de sécurité.</li>
          <li contenteditable="true"><strong>Gestion des Flux & Cadence :</strong> Coordination des flux de marchandises et respect strict des délais de livraison dans un environnement à haut rythme.</li>
          <li contenteditable="true"><strong>Remise Client & Closing :</strong> Remise soignée des commandes aux clients, écoute des retours, résolution proactive des imprévus et fidélisation.</li>
        </ul>
      </div>

      <div class="experience-item" id="exp-3">
        <div class="item-title" id="exp-3-title" contenteditable="true">Chargé de Prospection Commerciale & Déploiement POS</div>
        <div class="item-subrow">
          <span id="exp-3-comp" contenteditable="true">Nataan Group (ESN) — Lomé, Togo</span>
          <span id="exp-3-date" contenteditable="true">Juil. 2026 – Sept. 2026</span>
        </div>
        <ul class="item-bullets" id="exp-3-bullets">
          <li contenteditable="true"><strong>Développement Commercial B2B :</strong> Prospection directe et qualification approfondie de <strong>100 commerçants et professionnels</strong> de proximité ; démonstration de valeur et closing d'offres.</li>
          <li contenteditable="true"><strong>Solution d'Encaissement & Retail :</strong> Déploiement de l'application de caisse/point de vente <em>BoutiK</em> ; accompagnement des commerçants sur la gestion des encaissements et le suivi des stocks.</li>
          <li contenteditable="true"><strong>Sensibilisation aux KPIs Retail :</strong> Analyse des leviers de vente (panier moyen, fréquence d'achat, rapidité d'encaissement) et optimisation des parcours clients.</li>
          <li contenteditable="true"><strong>Service & Qualité :</strong> Écoute active des retours utilisateurs (103 tests fonctionnels exécutés) pour assurer une satisfaction et une adoption optimales.</li>
        </ul>
      </div>

      <div class="experience-item" id="exp-4">
        <div class="item-title" id="exp-4-title" contenteditable="true">Conseiller Utilisateurs & Analyse des Besoins</div>
        <div class="item-subrow">
          <span id="exp-4-comp" contenteditable="true">Darollo Technologies & ATANYS</span>
          <span id="exp-4-date" contenteditable="true">2025</span>
        </div>
        <ul class="item-bullets" id="exp-4-bullets">
          <li contenteditable="true">Écoute empathique, diagnostic précis des attentes utilisateurs et formulation de recommandations adaptées.</li>
          <li contenteditable="true">Sens de la pédagogie et démonstration claire pour valoriser les bénéfices concrets des produits et services.</li>
        </ul>
      </div>
    `;

    const techExpHTML = `
      <div class="experience-item" id="exp-1">
        <div class="item-title" id="exp-1-title" contenteditable="true">Stagiaire — Développement Mobile, QA & Business Development</div>
        <div class="item-subrow">
          <span id="exp-1-comp" contenteditable="true">Nataan Group (ESN) — Lomé, Togo</span>
          <span id="exp-1-date" contenteditable="true">Juil. 2026 – Sept. 2026</span>
        </div>
        <ul class="item-bullets" id="exp-1-bullets">
          <li contenteditable="true"><strong>Application BoutiK :</strong> Co-développement d'une application mobile de gestion de boutique / POS sous <strong>Flutter</strong>, connectée à <strong>Firebase</strong> et intégrant la passerelle de paiement <strong>FedaPay</strong>.</li>
          <li contenteditable="true"><strong>Portage & Release iOS :</strong> Portage iOS, mise en conformité avec les guidelines Apple, gestion de l'authentification OTP, push notifications <strong>APNs</strong> et publication en production via <strong>App Store Connect</strong>.</li>
          <li contenteditable="true"><strong>Assurance Qualité & Web :</strong> Conduite de la recette fonctionnelle complète d'un site institutionnel (exécution de <strong>103 cas de test</strong>), audit ergonomique UI/UX et refonte web.</li>
          <li contenteditable="true"><strong>Business Development & Données :</strong> Prospection commerciale B2B qualifiée (<strong>100 prospects ciblés</strong>) et réalisation de prestations d'archivage client.</li>
        </ul>
      </div>

      <div class="experience-item" id="exp-2">
        <div class="item-title" id="exp-2-title" contenteditable="true">Stagiaire en Développement Web</div>
        <div class="item-subrow">
          <span id="exp-2-comp" contenteditable="true">ATANYS — Lomé, Togo</span>
          <span id="exp-2-date" contenteditable="true">Sept. 2025 – Déc. 2025</span>
        </div>
        <ul class="item-bullets" id="exp-2-bullets">
          <li contenteditable="true">Conception et développement d'une plateforme web de gestion et de signalement des objets perdus et retrouvés.</li>
          <li contenteditable="true">Participation à l'ensemble du cycle de développement : analyse des besoins, modélisation de la base de données relationnelle (MySQL), développement back/front et tests.</li>
        </ul>
      </div>

      <div class="experience-item" id="exp-3">
        <div class="item-title" id="exp-3-title" contenteditable="true">Stagiaire en Développement d'Applications</div>
        <div class="item-subrow">
          <span id="exp-3-comp" contenteditable="true">Darollo Technologies Corporation — Lomé, Togo</span>
          <span id="exp-3-date" contenteditable="true">Juil. 2025 – Août 2025</span>
        </div>
        <ul class="item-bullets" id="exp-3-bullets">
          <li contenteditable="true">Développement d'une application mobile Flutter dédiée aux tailleurs pour la gestion de leur activité (prise de mesures, suivi des commandes, notifications).</li>
          <li contenteditable="true">Implémentation du fonctionnement hors ligne avec synchronisation automatique des données dès rétablissement de la connexion.</li>
        </ul>
      </div>

      <div class="experience-item" id="exp-4">
        <div class="item-title" id="exp-4-title" contenteditable="true">Stagiaire en Gestion de Données</div>
        <div class="item-subrow">
          <span id="exp-4-comp" contenteditable="true">ONG-CRISTO — Lomé, Togo</span>
          <span id="exp-4-date" contenteditable="true">Juil. 2024 – Sept. 2024</span>
        </div>
        <ul class="item-bullets" id="exp-4-bullets">
          <li contenteditable="true">Mise en place d'un système de gestion automatisée de la collecte d'informations pour un cabinet de recherche.</li>
          <li contenteditable="true">Structuration et fiabilisation des données collectées sur le terrain.</li>
        </ul>
      </div>
    `;

    // PRESETS FOR CV
    const cvPresets = {
      soutien_scolaire: {
        brand: "Acadomia / Complétude / Particuliers",
        roleRef: "Tutorat Lyon",
        jobRole: "Professeur Particulier & Tuteur Soutien Scolaire",
        title: "Professeur Particulier & Tuteur de Soutien Scolaire — Maths & Sciences",
        profile: "Étudiant en <strong>Master 1 à SUPINFO Lyon (Bac+5 en Informatique)</strong> et titulaire d'une <strong>Licence en Génie Logiciel</strong> avec un Baccalauréat Scientifique, je propose des cours de soutien scolaire et d'aide aux devoirs personnalisés pour élèves de collège et de lycée. Passionné par la transmission des savoirs, je m'appuie sur une démarche méthodique : diagnostic des lacunes, explication pas à pas des cours, exercices progressifs et techniques d'apprentissage concrètes pour redonner confiance et autonomie à l'élève. Patient, rigoureux et attentif, je veille à instaurer un climat d'échange bienveillant propice à la réussite et à l'obtention de résultats mesurables.",
        expType: "tutorat",
        dispo: "<strong>Tutorat & Soutien Scolaire</strong><br>Soirées semaine, mercredis après-midi, week-ends et vacances scolaires",
        skillsTitle: "Atouts Pédagogiques",
        skills: [
          { strong: "Patience & Écoute Active", text: "Capacité à débloquer les difficultés sans jugement et redonner confiance" },
          { strong: "Pédagogie Adaptative", text: "Explications imagées et vulgarisation des concepts abstraits" },
          { strong: "Suivi & Communication", text: "Bilans réguliers avec les parents et fixation d'objectifs hebdomadaires" },
          { strong: "Rigueur Scientifique", text: "Culture des mathématiques, logique algorithmique et sciences physiques" },
          { strong: "Méthodologie d'Examen", text: "Préparation au Brevet des collèges et épreuves du Baccalauréat" }
        ],
        interests: ["Jeux de logique & Algorithmes", "Football & Esprit d'équipe", "Lecture & Vulgarisation scientifique"],
        keywordsTitle: "Approche Pédagogique & Compétences",
        kw1: "<strong>Mathématiques & Logique :</strong> Algèbre, calcul littéral, géométrie, trigonométrie, analyse, probabilités, raisonnement déductif",
        kw2: "<strong>Numérique & Sciences :</strong> Initiation à la programmation (Python, Scratch, Web), NSI, sciences physiques collège, pensée algorithmique",
        kw3: "<strong>Méthode de Travail :</strong> Organisation des devoirs, fiches de révision, gestion du stress aux examens, autonomie de l'élève",
        kw4: "<strong>Savoir-Être Pédagogique :</strong> Patience infinie, empathie, communication positive, pédagogie différenciée, écoute attentive des besoins",
        kw5: "<strong>Organisation & Flexibilité :</strong> Déplacements sur Lyon et agglomération (Villeurbanne, Part-Dieu, etc.) ou cours en visioconférence"
      },

      macdo: {
        brand: "McDonald's",
        roleRef: "Job Étudiant / Temps Partiel",
        jobRole: "Équipier Polyvalent de Restauration Rapide",
        title: "Équipier Polyvalent de Restauration Rapide — Job Étudiant (McDonald's Lyon)",
        profile: "Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, dynamique, rigoureux et résistant au stress, je recherche un poste d'<strong>Équipier Polyvalent de Restauration Rapide</strong>. Fort d'une expérience concrète du contact client et de la gestion de caisse en période de forte affluence (Supermarché Champion en 2024) ainsi que de la logistique à cadence soutenue (préparation de commandes en 2025), j'ai développé une grande réactivité et le goût du travail en équipe rythmée. Rigoureux sur les normes d'hygiène (HACCP) et doté d'un relationnel chaleureux, je souhaite m'investir pleinement au sein de votre restaurant afin d'offrir un service rapide, impeccable et convivial à chaque client.",
        expType: "macdo",
        dispo: "<strong>Temps Partiel Restauration</strong><br>Soirées (rushs & fermetures), week-ends complets, jours fériés et vacances",
        skillsTitle: "Atouts Opérationnels",
        skills: [
          { strong: "Gestion du Rythme & Rushs", text: "Sang-froid en pic d'affluence, rapidité d'exécution et dynamisme continu" },
          { strong: "Hygiène & Sécurité (HACCP)", text: "Respect scrupuleux des normes sanitaires, propreté irréprochable et traçabilité" },
          { strong: "Polyvalence Salle / Cuisine / Drive", text: "Assemblage sandwichs, friture, caisse, accueil bornes et propreté salle" },
          { strong: "Esprit d'Équipe & Communication", text: "Coordination rapide, solidarité entre équipiers et sourire communicatif" },
          { strong: "Rigueur & Exactitude", text: "Tenue de caisse sans écart et respect scrupuleux des fiches recettes" }
        ],
        interests: ["Football & Esprit d'équipe", "Course à pied & Endurance", "Cuisine & Gastronomie"],
        keywordsTitle: "Compétences Clés Restauration Rapide",
        kw1: "<strong>Service Client & Comptoir :</strong> Accueil chaleureux, prise de commande aux bornes/comptoir, encaissement rapide, service à table et Drive",
        kw2: "<strong>Cuisine & Préparation :</strong> Assemblage sandwichs, cuisson/friture, garniture selon fiches techniques, respect des temps de conservation",
        kw3: "<strong>Hygiène & Sécurité (HACCP) :</strong> Respect de la chaîne du chaud/froid, nettoyage méthodique des postes et de la salle, tri sélectif",
        kw4: "<strong>Gestion du Rush & Collectif :</strong> Esprit d'équipe solidaire, rapidité d'exécution, gestion positive du stress, communication fluide",
        kw5: "<strong>Disponibilité & Flexibilité :</strong> Adaptabilité immédiate aux plannings modulables (soirées, week-ends complets, fermetures)"
      },

      hote_caisse_rayon: {
        brand: "Carrefour / Monoprix / Auchan",
        roleRef: "Temps Partiel Étudiant",
        jobRole: "Hôte de Caisse & Employé Commercial",
        title: "Hôte de Caisse & Employé Commercial Polyvalent — Job Étudiant",
        profile: "Étudiant sérieux et dynamique en <strong>Master 1 à SUPINFO Lyon</strong>, je recherche un poste d'<strong>Hôte de Caisse et Employé Commercial Polyvalent</strong>. Fort d'une expérience directe réussie au Supermarché Champion en 2024 (encaissement en pic d'affluence, réassort, facing et accueil client) et en préparation logistique en 2025, je suis immédiatement opérationnel. Ponctuel, rigoureux dans la tenue de caisse et doté d'un excellent sens du relationnel, je m'adapte avec aisance à vos flux clients et à vos contraintes de plannings (soirées et week-ends).",
        expType: "retail",
        dispo: "<strong>Grande Distribution & Caisse</strong><br>Soirées, samedis, dimanches matin et vacances scolaires",
        skillsTitle: "Atouts Caisse & Magasin",
        skills: [
          { strong: "Rapidité & Exactitude de Caisse", text: "Saisie sans erreur, encaissements CB/espèces/chèques et fidélité" },
          { strong: "Accueil & Sourire Client", text: "Politesse, écoute active, gestion courtoise des réclamations" },
          { strong: "Mise en Rayon & Merchandising", text: "Réassort rapide, respect du facing, contrôle DLC et rotation stocks" },
          { strong: "Polyvalence & Réactivité", text: "Passage fluide entre la caisse, les rayons et l'accueil magasin" },
          { strong: "Ponctualité & Rigueur", text: "Assiduité exemplaire et respect des procédures de sécurité" }
        ],
        interests: ["Commerce & Relation Client", "Football & Esprit d'équipe", "Nouvelles technologies"],
        keywordsTitle: "Compétences Clés Grande Distribution",
        kw1: "<strong>Encaissement & Gestion de Caisse :</strong> Fluidité en forte affluence, ouverture/clôture de caisse, respect des procédures financières",
        kw2: "<strong>Tenue de Magasin & Rayon :</strong> Réassort quotidien, facing soigné, contrôle des dates limites (DLC), étiquetage prix",
        kw3: "<strong>Relation Clientèle :</strong> Accueil personnalisé, orientation des clients, information promotions, fidélisation",
        kw4: "<strong>Organisation & Logistique :</strong> Déchargement des palettes, tri des marchandises, rangement en réserve",
        kw5: "<strong>Flexibilité :</strong> Disponibilité immédiate pour contrats étudiants (soirées, fins de semaine, périodes de fêtes)"
      },

      agent_accueil: {
        brand: "Cinéma UGC / Pathé / Événementiel",
        roleRef: "Job Étudiant Soirs & WE",
        jobRole: "Agent d'Accueil & de Service",
        title: "Agent d'Accueil, de Billetterie & de Service — Job Étudiant",
        profile: "Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, doté d'une excellente présentation et d'un sens naturel du service, je recherche un poste d'<strong>Agent d'Accueil, de Billetterie et de Service</strong> (cinémas, salons, structures culturelles ou événementielles). Fort de mes expériences au contact direct du public et de la gestion de caisse, j'accueille chaque visiteur avec courtoisie, sourire et efficacité. Dynamique, ponctuel et bilingue français/anglais, je veille au confort du public et à la bonne tenue des espaces.",
        expType: "retail",
        dispo: "<strong>Accueil & Événementiel</strong><br>Soirées, week-ends complets, jours fériés et vacances",
        skillsTitle: "Atouts Accueil & Service",
        skills: [
          { strong: "Accueil d'Excellence & Sourire", text: "Prise en charge chaleureuse, orientation du public et renseignement" },
          { strong: "Billetterie & Caisse Rapide", text: "Émission des tickets, vente de confiserie/snacks et encaissement" },
          { strong: "Contrôle d'Accès & Sécurité", text: "Vérification des billets, régulation des flux et guidage des salles" },
          { strong: "Tenue des Lieux & Propreté", text: "Entretien régulier des espaces d'accueil, salles et comptoirs" },
          { strong: "Gestion des Imprévus", text: "Calme, diplomatie et sens de la médiation bienveillante" }
        ],
        interests: ["Cinéma & Culture", "Musique & Événements", "Football & Esprit d'équipe"],
        keywordsTitle: "Compétences Clés Accueil & Billetterie",
        kw1: "<strong>Accueil & Information :</strong> Accueil physique souriant, orientation du public, présentation de la programmation",
        kw2: "<strong>Billetterie & Encaissement :</strong> Vente aux guichets et bornes, gestion de caisse, vente additionnelle (confiserie)",
        kw3: "<strong>Régulation des Flux :</strong> Contrôle des accès, gestion des files d'attente lors des séances à forte affluence",
        kw4: "<strong>Langues & Communication :</strong> Français soigné, Anglais professionnel pour visiteurs internationaux",
        kw5: "<strong>Disponibilité :</strong> Parfaite adéquation avec les horaires de soirées, week-ends et vacances scolaires"
      },

      adidas: {
        brand: "adidas",
        roleRef: "CDI 35H - Lyon Part Dieu",
        jobRole: "Vendeur Polyvalent",
        title: "Vendeur Polyvalent — adidas (CDI 35H - Lyon Part Dieu)",
        profile: "Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, doté d'une excellente énergie relationnelle et passionné par le contact humain et le commerce de détail. Fort d'expériences concrètes dans le commerce en magasin, la logistique de distribution et la prospection terrain, je maîtrise l'ensemble des étapes de l'acte de vente : accueil personnalisé, identification fine des attentes, conseil produit sur-mesure, gestion fluide de la caisse et fidélisation. Dynamique, curieux et résilient, je m'épanouis dans les environnements rythmés et valorise l'esprit d'équipe, l'inclusion et le dépassement de soi. Je souhaite m'investir pleinement comme ambassadeur de votre marque afin de délivrer une expérience client mémorable et contribuer aux objectifs commerciaux du magasin.",
        expType: "retail",
        dispo: "<strong>Vente Polyvalente adidas</strong><br>Disponible immédiatement · CDI 35H · Flexibilité horaires magasin",
        skillsTitle: "Atouts & Savoir-Être adidas",
        skills: [
          { strong: "Sens du Service Client & Passion Sport", text: "Accueil inspirant, partage de valeurs, découverte des besoins et conseil équipement" },
          { strong: "Performance Commerciale & KPIs Retail", text: "Panier moyen, taux de transformation, indice de vente, encaissement fluide" },
          { strong: "Polyvalence Magasin & Logistique", text: "De la réception des livraisons jusqu'à la mise en rayon, facing et encaissement" },
          { strong: "Rebelle Optimiste & Esprit d'Équipe", text: "Entraide active, communication positive, respect de la diversité et inclusion" },
          { strong: "Rigueur & Sens du Détail", text: "Tenue irréprochable de l'espace de vente, exactitude de caisse et réassort continu" }
        ],
        interests: ["Sport, Football & Running", "Sneakers & Culture Streetwear", "Innovation textile & Durabilité"],
        keywordsTitle: "Compétences Clés & Savoir-Faire Retail adidas",
        kw1: "<strong>Vente Conseil & Ambassadeur :</strong> Accueil personnalisé, storytelling marque adidas, découverte des besoins, argumentation, closing",
        kw2: "<strong>Process de Vente Intégral :</strong> Réception livraisons, contrôle stocks, réassort, facing, tenue du magasin, encaissement rapide",
        kw3: "<strong>Indicateurs Commerciaux :</strong> Sensibilité aux KPI (panier moyen, taux de transformation, fidélisation adiClub)",
        kw4: "<strong>Valeurs & Esprit Collectif :</strong> Rebelle optimiste, culture du sport, diversité et inclusion, travail d'équipe bienveillant",
        kw5: "<strong>Engagement & Disponibilité :</strong> Flexibilité plannings, ponctualité, dynamisme et curiosité pour les technologies produits"
      },

      apple: {
        brand: "Apple Retail",
        roleRef: "Rôle #114438069",
        jobRole: "Spécialiste Apple Retail",
        title: "Spécialiste Apple Retail — Job Étudiant (Rôle #114438069)",
        profile: "Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, doté d'un excellent sens relationnel et passionné par les produits et l'écosystème Apple. Fort d'expériences réussies dans le commerce de proximité, la préparation logistique et la prospection B2B, je sais écouter avec bienveillance, cerner les attentes réelles de chaque personne et délivrer une expérience client humaine et personnalisée. Dynamique, curieux et rigoureux, je m'adapte avec aisance au rythme soutenu d'un espace de vente tout en gardant le sens de l'accueil. Je souhaite mettre mon enthousiasme, mon esprit d'équipe et mon sens du service au cœur de l'Apple Store pour fidéliser la clientèle et faire rayonner la marque.",
        expType: "retail",
        dispo: "<strong>Job Étudiant Apple Store</strong><br>Soirées, week-ends, vacances scolaires & plannings flexibles Apple Store",
        skillsTitle: "Atouts & Savoir-Être Apple",
        skills: [
          { strong: "Sens du Service Client Apple", text: "Accueil chaleureux, écoute active, découverte des besoins et personnalisation" },
          { strong: "Esprit d'Équipe & Inclusion", text: "Entraide, communication positive, respect des diversités et curiosité" },
          { strong: "Gestion du Rythme & Affluence", text: "Aisance en environnement dynamique et prise en charge fluide de plusieurs clients" },
          { strong: "Passion Écosystème Apple", text: "iPhone, Mac, iPad, Apple Watch, iCloud, AppleCare, Apple Pay" },
          { strong: "Rigueur & Confidentialité", text: "Exactitude en caisse, respect des consignes et protection des données" }
        ],
        interests: ["Technologies & Écosystème Apple", "Football & Esprit d'équipe", "Musique & Créativité"],
        keywordsTitle: "Compétences Clés pour Apple Retail",
        kw1: "<strong>Relation Client & Vente :</strong> Accueil d'excellence, écoute active, découverte des besoins, conseil personnalisé, fidélisation, closing",
        kw2: "<strong>Gestion d'Espace de Vente :</strong> Encaissement en pic d'affluence, réassort, mise en valeur des produits, rigueur de tenue de rayon",
        kw3: "<strong>Écosystème & Produits Apple :</strong> Prise en main iPhone, iPad, Mac, Apple Watch, AirPods, services iOS/macOS, iCloud, AppleCare",
        kw4: "<strong>Valeurs & Esprit d'Équipe :</strong> Entraide, communication bienveillante, respect de l'inclusion et de la diversité, curiosité",
        kw5: "<strong>Organisation & Flexibilité :</strong> Disponibilité soirs et week-ends, ponctualité, adaptabilité à un flux client élevé, autonomie"
      },

      retail_polyvalent: {
        brand: "Commerce & Retail",
        roleRef: "Réf. Magasin Lyon",
        jobRole: "Conseiller de Vente & Vendeur Polyvalent",
        title: "Conseiller de Vente & Relation Client — Vendeur Polyvalent",
        profile: "Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, doté d'une excellente énergie relationnelle et passionné par le contact direct et l'expérience client. Fort d'expériences réussies en magasin, en logistique de distribution et en prospection commerciale, je maîtrise l'ensemble de la relation client : accueil personnalisé, écoute active, vente conseil, tenue soignée de l'espace de vente et encaissement en pic d'affluence. Polyvalent, ponctuel et motivé, je m'intègre immédiatement dans votre équipe pour atteindre vos objectifs de satisfaction et de performance commerciale.",
        expType: "retail",
        dispo: "<strong>Vente & Relation Client</strong><br>Disponible immédiatement · Temps plein (35H) ou partiel · Soirs & Week-ends",
        skillsTitle: "Atouts & Savoir-Être Retail",
        skills: [
          { strong: "Sens du Service & Conseil", text: "Accueil chaleureux, écoute active, découverte des besoins et personnalisation" },
          { strong: "Performance & KPIs Retail", text: "Sensibilisation aux objectifs : panier moyen, taux de transformation, fidélisation" },
          { strong: "Dynamisme & Esprit d'Équipe", text: "Entraide permanente, optimisme, curiosité et respect de la diversité & inclusion" },
          { strong: "Gestion du Rythme & Affluence", text: "Sang-froid en pic d'activité, polyvalence caisse, conseil et réassort" },
          { strong: "Rigueur & Tenue du Magasin", text: "Encaissement exact, respect du merchandising et tenue irréprochable des zones" }
        ],
        interests: ["Sport & Esprit d'équipe", "Commerce & Expérience Client", "Nouvelles technologies"],
        keywordsTitle: "Compétences Clés & Savoir-Faire Retail",
        kw1: "<strong>Vente Conseil & Relation Client :</strong> Accueil haut de gamme, découverte des besoins, argumentation personnalisée, vente complémentaire, fidélisation",
        kw2: "<strong>Opérations en Magasin :</strong> Tenue de caisse rapide & exacte, réassort, facing merchandising, gestion des livraisons, inventaire",
        kw3: "<strong>Performance & Indicateurs Retail :</strong> Sensibilité aux KPI (panier moyen, taux de transformation, indice de vente), contribution aux objectifs d'équipe",
        kw4: "<strong>Esprit d'Équipe & Culture Retail :</strong> Collaboration active, communication constructive, respect de la diversité, dynamisme",
        kw5: "<strong>Flexibilité & Engagement :</strong> Disponibilité soirs, week-ends et temps plein/partiel, gestion efficace du stress en forte affluence, ponctualité"
      },

      sephora: {
        brand: "Sephora",
        roleRef: "Conseiller(ère) de Vente Lyon",
        jobRole: "Conseiller de Vente & Beauté",
        title: "Conseiller de Vente & Expérience Client — Sephora Lyon",
        profile: "Dynamique, à l'écoute et passionné par l'univers de la beauté et de l'expérience client haut de gamme, je souhaite rejoindre l'équipe <strong>Sephora Lyon</strong>. Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, j'allie rigueur d'organisation, sens de l'accueil chaleureux et aisance relationnelle. Fort d'expériences réussies dans la vente en magasin (gestion de caisse en forte affluence, réassort soigné) et l'écoute client personnalisée, j'ai à cœur d'offrir à chaque visiteur un moment privilégié et de valoriser l'audace et l'énergie emblématiques de Sephora.",
        expType: "retail",
        dispo: "<strong>Conseiller de Vente Sephora</strong><br>Disponible immédiatement · Plannings adaptables · Soirs & Week-ends",
        skillsTitle: "Atouts & Savoir-Être Sephora",
        skills: [
          { strong: "Expérience Client & Bienveillance", text: "Accueil enthousiaste, écoute active, découverte des envies et personnalisation" },
          { strong: "Storytelling & Passion Produit", text: "Mise en avant des nouveautés parfums, soins et maquillage, conseil expert" },
          { strong: "Dynamisme & Gestion du Flux", text: "Aisance en environnement très animé, gestion rapide et souriante des encaissements" },
          { strong: "Esprit d'Équipe & Inclusivité", text: "Entraide, ouverture d'esprit, célébration de toutes les beautés" },
          { strong: "Excellence du Merchandising", text: "Rangement parfait, réassort continu et propreté exemplaire des stands" }
        ],
        interests: ["Univers Beauté & Cosmétiques", "Mode, Tendances & Lifestyle", "Sport & Bien-être"],
        keywordsTitle: "Compétences Clés pour Sephora Retail",
        kw1: "<strong>Accueil & Célébration Client :</strong> Écoute empathique, découverte des besoins, conseil personnalisé, vente croisée, fidélisation",
        kw2: "<strong>Animation du Point de Vente :</strong> Présentation impeccable des marques, réassort constant, tenue des testeurs, merchandising",
        kw3: "<strong>Tenue de Caisse & Fluidité :</strong> Encaissement rapide, programme de fidélité, gestion bienveillante des flux d'affluence",
        kw4: "<strong>Culture Sephora :</strong> Audace, passion, inclusion, esprit d'équipe bienveillant et communication positive",
        kw5: "<strong>Disponibilité & Polyvalence :</strong> Adaptabilité immédiate aux horaires du magasin, enthousiasme et proactivité"
      },

      hermes: {
        brand: "Hermès",
        roleRef: "Expérience Client Lyon",
        jobRole: "Conseiller de Vente & Expérience Client",
        title: "Conseiller de Vente & Expérience Client — Hermès Lyon",
        profile: "Animé par le sens du détail, l'excellence du service et l'art de recevoir propre aux grandes maisons de luxe, je souhaite mettre mon savoir-être et ma rigueur au service de la boutique <strong>Hermès Lyon</strong>. Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, je combine une présentation soignée, une discrétion irréprochable et une écoute bienveillante. Mon parcours en commerce de détail et en relation client m'a appris à créer un climat de confiance immédiat, à porter une attention minutieuse à chaque geste et à incarner avec fierté des standards d'élégance et d'artisanat d'exception.",
        expType: "retail",
        dispo: "<strong>Maison de Luxe & Haute Vente</strong><br>Disponible immédiatement · Présentation soignée · Flexibilité horaire",
        skillsTitle: "Savoir-Être & Standards Luxe",
        skills: [
          { strong: "Art de Recevoir & Discrétion", text: "Accueil raffiné, écoute attentive, respect de l'intimité et du rythme du client" },
          { strong: "Sens du Détail & Rigueur", text: "Exigence de présentation, gestuelle soignée, soin apporté aux pièces et packaging" },
          { strong: "Sensibilité Artisanat & Matières", text: "Intérêt profond pour les savoir-faire d'exception, cuir, soie et objets de création" },
          { strong: "Clientèle Internationale & Langues", text: "Français maternel à l'élocution parfaite, anglais fluide pour visiteurs internationaux" },
          { strong: "Équipe & Harmonie en Boutique", text: "Entraide discrète, esprit de corps, respect absolu des valeurs de la Maison" }
        ],
        interests: ["Artisanat d'art & Savoir-faire d'exception", "Mode, Architecture & Design", "Littérature & Voyages"],
        keywordsTitle: "Compétences Clés Vente de Luxe",
        kw1: "<strong>Relation Clientèle Privilégiée :</strong> Accueil sur-mesure, écoute feutrée, storytelling de la Maison, fidélisation durable",
        kw2: "<strong>Tenue de l'Espace & Cérémonial :</strong> Respect des normes d'exposition, manipulation délicate des pièces, présentation parfaite",
        kw3: "<strong>Organisation & Confidentialité :</strong> Encaissement discret, gestion rigoureuse des stocks et des réservations clients",
        kw4: "<strong>Savoir-Être d'Excellence :</strong> Politesse exemplaire, posture soignée, bienveillance et maîtrise de soi en toutes circonstances",
        kw5: "<strong>Communication Multilingue :</strong> Accueil fluide d'une clientèle locale et internationale exigeante"
      },

      alternance_logiciel: {
        brand: "Entreprise IT / ESN",
        roleRef: "Alternance / Stage Bac+5",
        jobRole: "Développeur Logiciel",
        title: "Développeur Logiciel — Étudiant Master 1 (Cursus Bac+5)",
        profile: "Actuellement étudiant en <strong>Master 1 en Informatique à SUPINFO Lyon (cursus préparant au diplôme Bac+5)</strong> et titulaire d'une <strong>Licence en Génie Logiciel</strong> (IAI-TOGO), je dispose d'une solide expertise pratique en développement web et mobile (Flutter, iOS, Django, Laravel), en programmation orientée objet (Java, Python) et en gestion de bases de données (SQL). Mes expériences en ESN et en entreprise m'ont permis d'intervenir sur tout le cycle de vie applicatif : cadrage du besoin, architecture, développement hors ligne, recette fonctionnelle approfondie et publication sur les stores (App Store Connect). Rigoureux et adaptable, je recherche une <strong>alternance ou un stage</strong> à Lyon pour mettre mes compétences au service de projets innovants.",
        expType: "tech",
        dispo: "<strong>Disponibilité Alternance / Stage</strong><br>Rythme école/entreprise ou stage temps plein · Lyon & Région",
        skillsTitle: "Compétences Techniques",
        skills: [
          { strong: "Développement Back-End & Mobile", text: "Java, Python, Flutter, Dart, Firebase, iOS (App Store Connect, APNs)" },
          { strong: "Développement Web & Frameworks", text: "Django, Laravel, PHP, JavaScript, HTML5/CSS3, Audit UI/UX" },
          { strong: "BaaS, API & Systèmes", text: "Firebase (Auth, Firestore), FedaPay, REST APIs, Notifications APNs" },
          { strong: "Assurance Qualité (QA)", text: "Tests unitaires, recette fonctionnelle, cahiers de tests (100+ cas)" },
          { strong: "Bases de données & Méthodes", text: "MySQL, PostgreSQL, modélisation SQL, Git, Agile/Scrum" }
        ],
        interests: ["Intelligence Artificielle & Veille tech", "Football & Esprit d'équipe", "Musique & UI/UX Design"],
        keywordsTitle: "Compétences Clés (Mots-clés)",
        kw1: "<strong>Langages & Frameworks :</strong> Java, Python, Flutter, Dart, Django, Laravel, PHP, HTML, CSS, JavaScript",
        kw2: "<strong>Développement mobile & Cloud :</strong> iOS (App Store Connect, APNs), Android, Flutter, Firebase, FedaPay, offline-first, synchronisation",
        kw3: "<strong>QA, Tests & Qualité :</strong> Tests unitaires, recette fonctionnelle (103 cas de test), revues de code, audit UI/UX, refonte web",
        kw4: "<strong>Bases de données :</strong> MySQL, PostgreSQL, MariaDB, Firebase Firestore, modélisation relationnelle SQL",
        kw5: "<strong>Méthodologie & Gestion :</strong> Méthodes agiles (Scrum), sécurité informatique, gestion de release, prospection B2B, travail en équipe"
      },

      stage_mobile: {
        brand: "Éditeur Mobile / Agence",
        roleRef: "Stage / Alternance Mobile",
        jobRole: "Développeur Mobile Flutter & iOS",
        title: "Développeur Mobile Flutter & iOS — Étudiant Master 1 (Bac+5)",
        profile: "Étudiant en <strong>Master 1 à SUPINFO Lyon (Bac+5)</strong> et passionné par le développement d'applications mobiles performantes et réactives, je maîtrise l'écosystème <strong>Flutter, Dart, Firebase</strong> ainsi que le portage et le cycle de release <strong>iOS (App Store Connect, APNs)</strong>. Fort d'expériences concrètes en ESN (co-développement de POS, intégration de passerelles de paiement FedaPay, mode offline-first), je recherche un <strong>stage ou une alternance</strong> en développement mobile pour concevoir des applications scalables et centrées sur l'expérience utilisateur.",
        expType: "tech",
        dispo: "<strong>Disponibilité Mobile</strong><br>Stage ou Alternance · Lyon & Télétravail partiel possible",
        skillsTitle: "Compétences Mobile",
        skills: [
          { strong: "Mobile Cross-Platform", text: "Flutter, Dart, Provider, Riverpod, architecture offline-first" },
          { strong: "Écosystème iOS & Stores", text: "Xcode, App Store Connect, certificats, profils, APNs, TestFlight" },
          { strong: "Cloud & Backend BaaS", text: "Firebase (Firestore, Auth, Cloud Functions), REST API, FedaPay" },
          { strong: "UI/UX & Recette Mobile", text: "Design adaptatif Material/Cupertino, audits ergonomiques, 103 cas de test" },
          { strong: "Outils & DevOps Mobile", text: "Git, GitHub, CI/CD basique, modélisation SQL et SQLite" }
        ],
        interests: ["Écosystème iOS & Swift", "Football & Stratégie d'équipe", "Création d'apps mobiles"],
        keywordsTitle: "Compétences Clés Mobile",
        kw1: "<strong>Mobile & Écosystème :</strong> Flutter, Dart, iOS (App Store Connect, APNs, TestFlight), Android, Architecture Offline-first",
        kw2: "<strong>Cloud, BaaS & Paiement :</strong> Firebase (Firestore, Auth, Push), FedaPay, API REST, Intégration OTP",
        kw3: "<strong>Langages & Web :</strong> Python, Django, PHP, JavaScript, HTML5/CSS3, Audit UI/UX",
        kw4: "<strong>Bases de données :</strong> Firebase Firestore, PostgreSQL, MySQL, modélisation relationnelle",
        kw5: "<strong>Méthodes & Outils :</strong> Git/GitHub, Agile/Scrum, CI/CD mobile, qualité logicielle, travail en équipe"
      },

      stage_qa: {
        brand: "Équipe Qualité / ESN",
        roleRef: "Stage / Alternance QA",
        jobRole: "Ingénieur QA & Qualité Logicielle",
        title: "Ingénieur QA & Qualité Logicielle — Étudiant Master 1 (Bac+5)",
        profile: "Étudiant en <strong>Master 1 en Informatique à SUPINFO Lyon (Bac+5)</strong> avec une solide formation en génie logiciel, je combine compétences de développement (Java, Python, SQL) et expertise opérationnelle en <strong>Assurance Qualité (QA) et recette fonctionnelle</strong>. Ayant rédigé et exécuté plus d'une centaine de cas de test sur des plateformes web et mobiles, et maîtrisé les critères d'acceptation stricts d'Apple, je recherche une <strong>opportunité en alternance ou stage QA</strong> pour fiabiliser et automatiser vos processus de tests.",
        expType: "tech",
        dispo: "<strong>Disponibilité QA</strong><br>Alternance ou Stage de fin d'études · Lyon & Région",
        skillsTitle: "Compétences QA & Tests",
        skills: [
          { strong: "Recette Fonctionnelle & Cahiers", text: "Élaboration de plans de test, exécution de 103 cas de test, non-régression" },
          { strong: "Conformité Stores & Guidelines", text: "Audit et respect des règles strictes de validation Apple App Store" },
          { strong: "Audit UI/UX & Anomalies", text: "Détection des bugs graphiques, ergonomie des parcours, reporting Jira/GitHub" },
          { strong: "Développement & Automatisation", text: "Bases solides en Java, Python, SQL, compréhension des architectures" },
          { strong: "Méthodologie Qualité", text: "Agile/Scrum, revues de code, documentation technique, rigueur d'analyse" }
        ],
        interests: ["Qualité logicielle & Cybersécurité", "Jeux de stratégie & Échecs", "Veille technologique"],
        keywordsTitle: "Compétences Clés Assurance Qualité",
        kw1: "<strong>Assurance Qualité (QA) :</strong> Cahiers & plans de test, recette fonctionnelle, non-régression, reporting d'anomalies",
        kw2: "<strong>Conformité & Stores :</strong> Validation App Store Apple, audit UI/UX, respect des cahiers des charges",
        kw3: "<strong>Langages & Automatisation :</strong> Java, Python, SQL, Dart/Flutter, notions de tests unitaires et d'intégration",
        kw4: "<strong>Bases de données :</strong> PostgreSQL, MySQL, requêtage SQL avancé pour vérification de cohérence des données",
        kw5: "<strong>Méthodologie :</strong> Méthodes agiles (Scrum), Git/GitHub, documentation technique, rigueur d'analyse"
      }
    };

    // UPDATE TITLE FROM HELPER INPUTS
    function updateCVTitleFromInputs() {
      const brand = document.getElementById('input-brand').value.trim();
      const roleRef = document.getElementById('input-role-ref').value.trim();
      const jobRole = document.getElementById('input-job-role').value.trim();

      let computedTitle = jobRole;
      if (brand) computedTitle += " — " + brand;
      if (roleRef) computedTitle += " (" + roleRef + ")";

      document.getElementById('input-cv-title').value = computedTitle;
      document.getElementById('cv-subtitle').innerText = computedTitle;
      autoSaveCV();
    }

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
        const btn = event.target.closest('.btn-preset');
        if (btn) btn.classList.add('active');
      }

      const data = cvPresets[key];
      if (!data) return;

      // Inputs
      document.getElementById('input-brand').value = data.brand || "";
      document.getElementById('input-role-ref').value = data.roleRef || "";
      document.getElementById('input-job-role').value = data.jobRole || "";
      document.getElementById('input-cv-title').value = data.title;
      document.getElementById('cv-subtitle').innerText = data.title;

      document.getElementById('input-cv-profile').value = data.profile.replace(/<[^>]*>/g, '');
      document.getElementById('cv-profile-p').innerHTML = data.profile;

      // Dispo sidebar
      document.getElementById('sb-dispo-item').innerHTML = data.dispo;

      // Sidebar skills
      document.getElementById('sb-skills-title').innerText = data.skillsTitle;
      for (let i = 0; i < 5; i++) {
        const itemEl = document.getElementById('sb-skill-' + (i + 1));
        if (itemEl && data.skills[i]) {
          itemEl.innerHTML = '<strong>' + data.skills[i].strong + '</strong>' + data.skills[i].text;
        }
      }

      // Sidebar interests
      if (data.interests && data.interests.length >= 3) {
        document.getElementById('sb-int-1').innerText = data.interests[0];
        document.getElementById('sb-int-2').innerText = data.interests[1];
        document.getElementById('sb-int-3').innerText = data.interests[2];
      }

      // Experiences Container
      const expContainer = document.getElementById('experiences-container');
      if (data.expType === 'tutorat') {
        expContainer.innerHTML = tutoratExpHTML;
      } else if (data.expType === 'macdo') {
        expContainer.innerHTML = macdoExpHTML;
      } else if (data.expType === 'retail') {
        expContainer.innerHTML = retailExpHTML;
      } else {
        expContainer.innerHTML = techExpHTML;
      }

      // Keywords Title & Lines
      document.getElementById('sec-keywords-title').innerText = data.keywordsTitle;
      document.getElementById('kw-line-1').innerHTML = data.kw1;
      document.getElementById('kw-line-2').innerHTML = data.kw2;
      document.getElementById('kw-line-3').innerHTML = data.kw3;
      document.getElementById('kw-line-4').innerHTML = data.kw4;
      document.getElementById('kw-line-5').innerHTML = data.kw5;

      // Rebind contenteditable listeners
      bindEditableListeners();

      // Update Direct PDF download button
      const presetPdfMap = {
        soutien_scolaire: 'CV_Rodrigue_HESSOU_Soutien_Scolaire.pdf',
        macdo: 'CV_Rodrigue_HESSOU_Restauration_MacDo.pdf',
        hote_caisse_rayon: 'CV_Rodrigue_HESSOU_Retail_Polyvalent.pdf',
        agent_accueil: 'CV_Rodrigue_HESSOU_Retail_Polyvalent.pdf',
        apple_part_time: 'CV_Rodrigue_HESSOU_Apple_Retail.pdf',
        adidas_part_dieu: 'CV_Rodrigue_HESSOU_Retail_Polyvalent.pdf',
        retail_general: 'CV_Rodrigue_HESSOU_Retail_Polyvalent.pdf',
        stage_bac5_dev: 'CV_Rodrigue_HESSOU.pdf',
        alternance_bac5_dev: 'CV_Rodrigue_HESSOU.pdf'
      };
      const directPdf = presetPdfMap[key] || 'CV_Rodrigue_HESSOU.pdf';
      const directBtn = document.getElementById('btn-download-preset-pdf');
      if (directBtn) {
        directBtn.href = directPdf;
        directBtn.setAttribute('download', directPdf);
      }

      const label = key.toUpperCase().replace('_', ' ');
      showToast("Modèle " + label + " activé avec succès !");
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
      showToast("💡 Astuce : Dans la fenêtre d'impression, cochez 'Graphiques d'arrière-plan' pour garder le bandeau bleu !");
      setTimeout(() => {
        window.print();
      }, 400);
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
      setTimeout(() => t.classList.remove('show'), 3200);
    }

    // AUTOSAVE
    function autoSaveCV() {
      try {
        localStorage.setItem('rodrigue_cv_saved', document.getElementById('printable-cv').innerHTML);
      } catch(e) {}
    }

    function bindEditableListeners() {
      document.querySelectorAll('[contenteditable="true"]').forEach(el => {
        el.removeEventListener('input', autoSaveCV);
        el.addEventListener('input', autoSaveCV);
      });
    }

    window.addEventListener('DOMContentLoaded', () => {
      // Default load Soutien Scolaire
      loadCVPreset('soutien_scolaire');
      bindEditableListeners();
    });

    function resetCVToDefault() {
      localStorage.removeItem('rodrigue_cv_saved');
      loadCVPreset('soutien_scolaire');
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

print("editeur_cv.html generated cleanly with full student job presets!")
