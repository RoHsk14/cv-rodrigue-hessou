html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Éditeur de Lettre de Motivation - Rodrigue HESSOU</title>
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
    --success: #10b981;
    --border: #cbd5e1;
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
  .sheet-container {
    width: 210mm;
    min-height: 297mm;
    background: #ffffff;
    color: #262626;
    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.1);
    border-radius: 2px;
    font-family: 'Carlito', 'Calibri', 'Segoe UI', Arial, sans-serif;
    padding: 18mm 22mm 16mm 22mm;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    line-height: 1.44;
    position: relative;
  }

  /* EDITABLE STYLING IN PREVIEW */
  [contenteditable="true"] {
    outline: none;
    transition: background 0.15s ease, box-shadow 0.15s ease;
    border-radius: 3px;
    padding: 1px 3px;
    margin: -1px -3px;
  }

  [contenteditable="true"]:hover {
    background-color: rgba(46, 117, 182, 0.08);
    cursor: text;
  }

  [contenteditable="true"]:focus {
    background-color: rgba(46, 117, 182, 0.12);
    box-shadow: 0 0 0 2px rgba(46, 117, 182, 0.4);
  }

  /* HEADER BLOCK */
  .doc-header {
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

  .recipient-company {
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
  .doc-meta {
    margin-bottom: 3.8mm;
  }

  .doc-date {
    text-align: right;
    font-size: 9.2pt;
    color: #64748b;
    margin-bottom: 2.5mm;
  }

  .doc-object {
    font-size: 10pt;
    color: #1e293b;
    padding: 2.2mm 3.5mm;
    background-color: #f1f5f9;
    border-radius: 4px;
  }

  .doc-object strong {
    color: #2e75b6;
    font-weight: 700;
  }

  /* LETTER BODY */
  .doc-body {
    display: flex;
    flex-direction: column;
    gap: 3.2mm;
    font-size: 9.35pt;
    color: #262626;
    text-align: justify;
    line-height: 1.42;
  }

  .doc-salutation {
    font-size: 9.8pt;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 0.5mm;
  }

  .doc-body p strong {
    color: #1e293b;
    font-weight: 700;
  }

  /* CLOSING & SIGNATURE */
  .doc-closing {
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

  /* PRINT MEDIA STYLES - 1 PAGE STRICT */
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

    .sheet-container {
      width: 210mm !important;
      height: 297mm !important;
      min-height: 297mm !important;
      max-height: 297mm !important;
      margin: 0 auto !important;
      padding: 18mm 22mm 16mm 22mm !important;
      box-shadow: none !important;
      border: none !important;
      page-break-after: avoid !important;
      page-break-inside: avoid !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      color-adjust: exact !important;
    }

    .recipient-card {
      background-color: #f8fafc !important;
      border-left: 3px solid #2e75b6 !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      color-adjust: exact !important;
    }

    .doc-object {
      background-color: #f1f5f9 !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      color-adjust: exact !important;
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

  <!-- TOP BAR -->
  <header class="top-navbar">
    <div class="nav-brand">
      <div class="nav-logo">RH</div>
      <div class="nav-title">
        <h1>Éditeur de Lettre de Motivation</h1>
        <p>Rodrigue HESSOU — Modèles Soutien Scolaire, Fast-Food, Retail & Tech</p>
      </div>
    </div>

    <div class="nav-actions">
      <a id="btn-download-preset-pdf" href="Lettre_de_Motivation_Soutien_Scolaire_Rodrigue_HESSOU.pdf" download class="btn btn-secondary" title="Télécharger le fichier PDF officiel pré-généré">
        ⚡ PDF Officiel Direct
      </a>
      <button class="btn btn-secondary" onclick="copyLetterText()">
        📋 Copier le texte
      </button>
      <button class="btn btn-primary" onclick="printToPDF()">
        🖨️ Télécharger en PDF
      </button>
    </div>
  </header>

  <!-- MAIN WORKSPACE -->
  <div class="workspace">

    <!-- CONTROLS SIDEBAR -->
    <aside class="editor-sidebar">
      <div class="sidebar-inner">

        <!-- PRESETS -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">⚡ Modèles Prédéfinis</span>
            <span class="card-badge">1 clic</span>
          </div>

          <div class="category-title">🎓 Jobs Étudiants Polyvalents</div>
          <div class="preset-grid">
            <button class="btn-preset active" onclick="loadPreset('soutien_scolaire')">
              <span>🎓 Soutien Scolaire & Tutorat (Maths / Sciences)</span>
            </button>
            <button class="btn-preset" onclick="loadPreset('macdo')">
              <span>🍔 McDonald's & Fast-Food (Équipier Polyvalent)</span>
            </button>
            <button class="btn-preset" onclick="loadPreset('hote_caisse')">
              <span>🛒 Hôte de Caisse (Grande Distribution)</span>
            </button>
            <button class="btn-preset" onclick="loadPreset('agent_accueil')">
              <span>🎟️ Agent d'Accueil & Cinéma (UGC / Événements)</span>
            </button>
          </div>

          <div class="category-title" style="margin-top: 6px;">👟 Vente, Commerce & Marques</div>
          <div class="preset-grid">
            <button class="btn-preset" onclick="loadPreset('adidas')">
              <span>👟 adidas Part-Dieu (Vendeur Polyvalent)</span>
            </button>
            <button class="btn-preset" onclick="loadPreset('apple')">
              <span>🍏 Apple Retail (Spécialiste #114438069)</span>
            </button>
            <button class="btn-preset" onclick="loadPreset('retail_polyvalent')">
              <span>🛍️ Conseiller de Vente (Commerce Généraliste)</span>
            </button>
            <button class="btn-preset" onclick="loadPreset('sephora')">
              <span>💄 Sephora Lyon (Conseiller de Vente Beauté)</span>
            </button>
            <button class="btn-preset" onclick="loadPreset('hermes')">
              <span>👜 Hermès Lyon (Luxe & Expérience Client)</span>
            </button>
          </div>

          <div class="category-title" style="margin-top: 6px;">💼 Tech & Ingénierie Bac+5</div>
          <div class="preset-grid">
            <button class="btn-preset" onclick="loadPreset('capgemini')">
              <span>🏢 Capgemini Lyon (Java / PLM)</span>
            </button>
            <button class="btn-preset" onclick="loadPreset('mobile')">
              <span>📱 Dév. Mobile (Flutter / iOS)</span>
            </button>
            <button class="btn-preset" onclick="loadPreset('fullstack')">
              <span>🌐 Dév. Web / Full-Stack</span>
            </button>
            <button class="btn-preset" onclick="loadPreset('qa')">
              <span>🧪 QA & Recette Logicielle</span>
            </button>
          </div>
        </div>

        <!-- ENTREPRISE, ROLE & CANDIDATURE -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">🏷️ Offre, Établissement & Rôle</span>
          </div>
          <div class="quick-helper-box">
            Renseignez l'intitulé du poste et le <strong>numéro de rôle ou référence d'offre</strong> pour actualiser automatiquement l'objet et le destinataire.
          </div>
          <div class="form-row">
            <div class="form-group">
              <label>Nom de la structure</label>
              <input type="text" id="input-company" value="Organisme de Soutien Scolaire / Familles" oninput="syncField('company', this.value)">
            </div>
            <div class="form-group">
              <label>N° Rôle / Référence</label>
              <input type="text" id="input-role-ref" value="Tutorat Lyon" placeholder="ex: 114438069, Réf. Part-Dieu..." oninput="updateLetterObjectFromInputs()">
            </div>
          </div>
          <div class="form-group">
            <label>Intitulé du poste</label>
            <input type="text" id="input-job-title" value="Enseignant / Tuteur en Soutien Scolaire" oninput="updateLetterObjectFromInputs()">
          </div>
          <div class="form-group">
            <label>Destinataire / Service</label>
            <input type="text" id="input-recipient" value="À l'attention de l'équipe Recrutement Pédagogique" oninput="syncField('recipient', this.value)">
          </div>
          <div class="form-row">
            <div class="form-group">
              <label>Adresse Établissement</label>
              <input type="text" id="input-comp-addr" value="Agence Acadomia / Complétude / Anacours" oninput="syncField('compAddr', this.value)">
            </div>
            <div class="form-group">
              <label>Code Postal & Ville</label>
              <input type="text" id="input-comp-city" value="Lyon, France" oninput="syncField('compCity', this.value)">
            </div>
          </div>
        </div>

        <!-- OBJET & DATE -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">🎯 Objet & Lieu de Rédaction</span>
          </div>
          <div class="form-group">
            <label>Ligne d'Objet Complète</label>
            <input type="text" id="input-object" value="Candidature comme Enseignant / Tuteur en Soutien Scolaire (Mathématiques & Sciences)" oninput="syncField('object', this.value)">
          </div>
          <div class="form-row">
            <div class="form-group">
              <label>Lieu de rédaction</label>
              <input type="text" id="input-place" value="À Lyon" oninput="syncDate()">
            </div>
            <div class="form-group">
              <label>Date</label>
              <input type="text" id="input-date" value="22 octobre 2026" oninput="syncDate()">
            </div>
          </div>
        </div>

        <!-- SENDER DETAILS -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">👤 Mes Coordonnées</span>
          </div>
          <div class="form-group">
            <label>Nom & Prénom</label>
            <input type="text" id="input-sender-name" value="Rodrigue HESSOU" oninput="syncField('senderName', this.value)">
          </div>
          <div class="form-group">
            <label>Titre / Statut</label>
            <input type="text" id="input-sender-title" value="Professeur Particulier & Tuteur de Soutien Scolaire (Bac+5)" oninput="syncField('senderTitle', this.value)">
          </div>
          <div class="form-row">
            <div class="form-group">
              <label>Adresse</label>
              <input type="text" id="input-sender-addr" value="429 Cours Émile Zola" oninput="syncField('senderAddr', this.value)">
            </div>
            <div class="form-group">
              <label>Ville</label>
              <input type="text" id="input-sender-city" value="69100 Villeurbanne – Lyon" oninput="syncField('senderCity', this.value)">
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label>Téléphone</label>
              <input type="text" id="input-sender-phone" value="+33 7 44 11 75 73" oninput="syncField('senderPhone', this.value)">
            </div>
            <div class="form-group">
              <label>Email</label>
              <input type="email" id="input-sender-email" value="rodriguehessou14@gmail.com" oninput="syncField('senderEmail', this.value)">
            </div>
          </div>
        </div>

        <!-- ACTIONS & RESET -->
        <div style="display: flex; gap: 8px;">
          <button class="btn btn-outline" style="flex: 1;" onclick="resetToDefault()">
            🔄 Réinitialiser
          </button>
          <button class="btn btn-secondary" style="flex: 1;" onclick="printToPDF()">
            🖨️ Imprimer / PDF
          </button>
        </div>

      </div>
    </aside>

    <!-- RIGHT PREVIEW SHEET -->
    <main class="preview-panel">
      <div class="preview-notice">
        <span>💡 <strong>Astuce :</strong> Vous pouvez modifier les textes <em>directement</em> sur la feuille en cliquant dessus, ou utiliser le formulaire à gauche.</span>
      </div>

      <!-- A4 PAPER SHEET -->
      <div class="sheet-container" id="printable-letter">
        
        <div>
          <!-- HEADER EXPEDITEUR / DESTINATAIRE -->
          <div class="doc-header">
            <div class="sender-info">
              <div class="sender-name" id="doc-sender-name" contenteditable="true">Rodrigue HESSOU</div>
              <div class="sender-subtitle" id="doc-sender-title" contenteditable="true">Professeur Particulier & Tuteur de Soutien Scolaire (Bac+5)</div>
              <div class="sender-detail" id="doc-sender-addr" contenteditable="true">429 Cours Émile Zola</div>
              <div class="sender-detail" id="doc-sender-city" contenteditable="true">69100 Villeurbanne – Lyon</div>
              <div class="sender-detail" id="doc-sender-phone" contenteditable="true">+33 7 44 11 75 73</div>
              <div class="sender-detail" id="doc-sender-email" contenteditable="true">rodriguehessou14@gmail.com</div>
            </div>

            <div class="recipient-card">
              <div class="recipient-company" id="doc-company" contenteditable="true">Organisme de Soutien Scolaire / Familles</div>
              <div class="recipient-detail" id="doc-recipient" contenteditable="true">À l'attention de l'équipe Recrutement Pédagogique</div>
              <div class="recipient-detail" id="doc-comp-addr" contenteditable="true">Agence Acadomia / Complétude / Anacours</div>
              <div class="recipient-detail" id="doc-comp-city" contenteditable="true">Lyon, France</div>
            </div>
          </div>

          <!-- DATE & OBJET -->
          <div class="doc-meta">
            <div class="doc-date" id="doc-date-line" contenteditable="true">À Lyon, le 22 octobre 2026</div>
            <div class="doc-object">
              <strong>Objet :</strong> <span id="doc-object" contenteditable="true">Candidature comme Enseignant / Tuteur en Soutien Scolaire (Mathématiques & Sciences)</span>
            </div>
          </div>

          <!-- CORPS DU TEXTE -->
          <div class="doc-body" id="doc-body">
            <div class="doc-salutation" contenteditable="true">Madame, Monsieur,</div>

            <p id="p1" contenteditable="true">
              Passionné par la transmission des connaissances, la pédagogie positive et l'accompagnement des jeunes vers la réussite, je vous présente avec enthousiasme ma candidature en tant qu'<strong>Enseignant en Soutien Scolaire et Aide aux Devoirs</strong>. Actuellement étudiant en <strong>Master 1 à SUPINFO Lyon (Bac+5 en Informatique)</strong> et titulaire d'une <strong>Licence en Génie Logiciel</strong> précédée d'un Baccalauréat Scientifique, je souhaite mettre ma rigueur méthodologique et ma bienveillance au service de vos élèves.
            </p>

            <p id="p2" contenteditable="true">
              Mon parcours académique m'a conféré une solide maîtrise des matières scientifiques (<strong>Mathématiques, Algorithmique, Physique et Numérique</strong>), ainsi qu'une démarche de travail structurée. Au-delà des connaissances théoriques, je suis convaincu que la clé de la réussite scolaire réside dans la relation de confiance établie avec l'élève : savoir écouter sans juger, identifier la source précise des blocages (manque de confiance, lacunes de cours ou mauvaise organisation) et réexpliquer les notions sous des angles concrets et imagés.
            </p>

            <p id="p3" contenteditable="true">
              Mes expériences m'ont permis de développer de réelles compétences pédagogiques. J'ai notamment formé plus de <strong>100 utilisateurs</strong> aux fonctionnalités d'outils numériques en adaptant mon discours au rythme de chacun, et animé des ateliers individuels de renforcement. Habitué à structurer des séances de travail complètes (rappel des points clés du cours, exercices d'application guidés, puis mise en autonomie progressive), j'accorde une importance essentielle à l'acquisition d'une méthode de travail pérenne.
            </p>

            <p id="p4" contenteditable="true">
              Mon approche s'adresse aussi bien aux élèves de <strong>collège</strong> nécessitant un cadre rassurant pour consolider leurs bases et préparer le Brevet, qu'aux lycéens préparant les épreuves du <strong>Baccalauréat</strong> ou souhaitant se perfectionner en spécialité Mathématiques et NSI. Je m'assure toujours d'un dialogue fluide et régulier avec les parents pour faire part des progrès réalisés.
            </p>

            <p id="p5" contenteditable="true">
              Ponctuel, patient, motivant et à l'écoute, je suis disponible sur toute l'agglomération lyonnaise (Villeurbanne, Lyon) ainsi qu'en distanciel, sur les créneaux de fin d'après-midi, mercredis, week-ends et vacances scolaires.
            </p>

            <p id="p6" contenteditable="true">
              Je serais ravi d'échanger avec vous lors d'un entretien afin de vous détailler mon approche pédagogique. En vous remerciant pour votre bienveillante attention, je vous prie d'agréer, Madame, Monsieur, mes salutations respectueuses.
            </p>
          </div>
        </div>

        <!-- SIGNATURE -->
        <div class="doc-closing">
          <div class="signature-box">
            <div class="signature-name" id="doc-sig-name" contenteditable="true">Rodrigue HESSOU</div>
            <div class="signature-title" id="doc-sig-title" contenteditable="true">Étudiant Master 1 SUPINFO Lyon · Tuteur Pédagogique</div>
          </div>
        </div>

      </div>
    </main>

  </div>

  <!-- TOAST -->
  <div class="toast" id="toast">Message</div>

  <script>
    // PRESETS DATA
    const presets = {
      soutien_scolaire: {
        company: "Organisme de Soutien Scolaire / Familles",
        roleRef: "Tutorat Lyon",
        jobTitle: "Enseignant / Tuteur en Soutien Scolaire",
        recipient: "À l'attention de l'équipe Recrutement Pédagogique",
        compAddr: "Agence Acadomia / Complétude / Anacours",
        compCity: "Lyon, France",
        senderTitle: "Professeur Particulier & Tuteur de Soutien Scolaire (Bac+5)",
        sigTitle: "Étudiant Master 1 SUPINFO Lyon · Tuteur Pédagogique",
        object: "Candidature comme Enseignant / Tuteur en Soutien Scolaire (Mathématiques & Sciences)",
        p1: "Passionné par la transmission des connaissances, la pédagogie positive et l'accompagnement des jeunes vers la réussite, je vous présente avec enthousiasme ma candidature en tant qu'<strong>Enseignant en Soutien Scolaire et Aide aux Devoirs</strong>. Actuellement étudiant en <strong>Master 1 à SUPINFO Lyon (Bac+5 en Informatique)</strong> et titulaire d'une <strong>Licence en Génie Logiciel</strong> précédée d'un Baccalauréat Scientifique, je souhaite mettre ma rigueur méthodologique et ma bienveillance au service de vos élèves.",
        p2: "Mon parcours académique m'a conféré une solide maîtrise des matières scientifiques (<strong>Mathématiques, Algorithmique, Physique et Numérique</strong>), ainsi qu'une démarche de travail structurée. Au-delà des connaissances théoriques, je suis convaincu que la clé de la réussite scolaire réside dans la relation de confiance établie avec l'élève : savoir écouter sans juger, identifier la source précise des blocages (manque de confiance, lacunes de cours ou mauvaise organisation) et réexpliquer les notions sous des angles concrets et imagés.",
        p3: "Mes expériences m'ont permis de développer de réelles compétences pédagogiques. J'ai notamment formé plus de <strong>100 utilisateurs</strong> aux fonctionnalités d'outils numériques en adaptant mon discours au rythme de chacun, et animé des ateliers individuels de renforcement. Habitué à structurer des séances de travail complètes (rappel des points clés du cours, exercices d'application guidés, puis mise en autonomie progressive), j'accorde une importance essentielle à l'acquisition d'une méthode de travail pérenne.",
        p4: "Mon approche s'adresse aussi bien aux élèves de <strong>collège</strong> nécessitant un cadre rassurant pour consolider leurs bases et préparer le Brevet, qu'aux lycéens préparant les épreuves du <strong>Baccalauréat</strong> ou souhaitant se perfectionner en spécialité Mathématiques et NSI. Je m'assure toujours d'un dialogue fluide et régulier avec les parents pour faire part des progrès réalisés.",
        p5: "Ponctuel, patient, motivant et à l'écoute, je suis disponible sur toute l'agglomération lyonnaise (Villeurbanne, Lyon) ainsi qu'en distanciel, sur les créneaux de fin d'après-midi, mercredis, week-ends et vacances scolaires.",
        p6: "Je serais ravi d'échanger avec vous lors d'un entretien afin de vous détailler mon approche pédagogique. En vous remerciant pour votre bienveillante attention, je vous prie d'agréer, Madame, Monsieur, mes salutations respectueuses."
      },

      macdo: {
        company: "MCDONALD'S FRANCE",
        roleRef: "Job Étudiant Soirs & WE",
        jobTitle: "Équipier Polyvalent de Restauration Rapide",
        recipient: "À l'attention de la Direction du Restaurant",
        compAddr: "Restaurant McDonald's Lyon (Part-Dieu / Charpennes / Villeurbanne)",
        compCity: "Lyon, France",
        senderTitle: "Candidat Équipier Polyvalent de Restauration — Job Étudiant",
        sigTitle: "Candidat Équipier Polyvalent · McDonald's Lyon",
        object: "Candidature au poste d'Équipier Polyvalent de Restauration Rapide (Job Étudiant / Temps Partiel)",
        p1: "Actuellement étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, je souhaite vivement rejoindre votre équipe en tant qu'<strong>Équipier Polyvalent au sein de votre restaurant McDonald's</strong>. Attiré par le dynamisme de votre enseigne, la rigueur de votre organisation et la qualité de votre service client, je souhaite mettre mon énergie, ma ponctualité et mon esprit d'équipe au service de votre activité quotidienne.",
        p2: "Mes précédentes expériences m'ont permis d'acquérir une excellente réactivité sur le terrain. Lors de mon activité au <strong>Supermarché Champion en 2024</strong>, j'ai géré l'accueil et l'encaissement de nombreux clients durant les pics de forte affluence. Cette immersion m'a appris à exécuter les tâches avec rapidité et exactitude, tout en conservant un accueil souriant et courtois en toutes circonstances. J'y ai également développé une grande rigueur dans le maintien de la propreté et la tenue des postes de travail.",
        p3: "Par ailleurs, mon travail en <strong>plateforme logistique en 2025</strong> a confirmé ma capacité à soutenir des cadences rapides et à appliquer scrupuleusement les consignes d'organisation et de sécurité. Polyvalent et doté d'une forte faculté d'adaptation, je suis prêt à intervenir sur tous les postes de votre restaurant : <strong>accueil au comptoir et aux bornes, préparation et assemblage des commandes en cuisine, service en salle et au Drive, ainsi qu'entretien régulier des équipements dans le respect strict des normes HACCP</strong>.",
        p4: "Ce qui me motive chez McDonald's, c'est l'intensité du travail en équipe et l'engagement collectif pour satisfaire chaque visiteur en un temps record. Ponctuel, enthousiaste et communicatif, je m'intègre avec facilité et contribue à maintenir une ambiance de travail solidaire et motivante, même lors des rushs les plus intenses.",
        p5: "Parfaitement conscient des exigences d'un contrat étudiant en restauration, je vous garantis une <strong>grande flexibilité horaire</strong> : je suis disponible en soirée (fermetures incluses), les week-ends complets ainsi que pendant toutes les vacances scolaires.",
        p6: "Je serais très heureux de vous rencontrer à l'occasion d'un entretien pour vous démontrer ma motivation et mon envie de m'investir au sein de votre équipe. En vous remerciant de votre considération, je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées."
      },

      hote_caisse: {
        company: "CARREFOUR / MONOPRIX / AUCHAN",
        roleRef: "Job Étudiant Caisse",
        jobTitle: "Hôte de Caisse & Employé Commercial",
        recipient: "À l'attention du Responsable des Caisses & Recrutement",
        compAddr: "Magasin Lyon (Part-Dieu / Villeurbanne / Presqu'île)",
        compCity: "Lyon, France",
        senderTitle: "Candidat Hôte de Caisse & Employé Commercial Polyvalent",
        sigTitle: "Candidat Hôte de Caisse · Job Étudiant",
        object: "Candidature au poste d'Hôte de Caisse et Employé Commercial Polyvalent (Job Étudiant)",
        p1: "Étudiant sérieux et dynamique en <strong>Master 1 à SUPINFO Lyon</strong>, je vous soumets ma candidature pour un poste d'<strong>Hôte de Caisse et Employé Commercial Polyvalent</strong> au sein de votre magasin. Fort d'une expérience directe réussie au Supermarché Champion et de mon passage en logistique de distribution, je serai immédiatement opérationnel au sein de votre ligne de caisses.",
        p2: "Au <strong>Supermarché Champion en 2024</strong>, j'ai assuré la gestion des encaissements lors de forts pics d'affluence avec exactitude, rapidité et un sens permanent de l'amabilité. Cette expérience m'a appris à gérer le flux avec sérénité, à vérifier scrupuleusement les moyens de paiement et à renseigner chaque client avec le sourire. J'y ai également effectué des missions de réassort, de facing et de contrôle des dates limites de péremption (DLC).",
        p3: "Rigoureux, ponctuel et doté d'une excellente présentation, je valorise la relation client de proximité et le travail en équipe. Mon sens des responsabilités me permet d'assurer une tenue de caisse irréprochable et de respecter scrupuleusement les consignes de sécurité financière de votre magasin.",
        p4: "Disponible immédiatement pour un contrat étudiant à temps partiel (soirées, samedis, dimanches matin et vacances scolaires), je m'adapte avec souplesse à votre planning.",
        p5: "Je me tiens à votre disposition pour convenir d'un entretien et vous exprimer de vive voix ma motivation. Je vous prie d'agréer, Madame, Monsieur, mes salutations respectueuses.",
        p6: ""
      },

      agent_accueil: {
        company: "CINÉMAS UGC / PATHÉ / ÉVÉNEMENTIEL",
        roleRef: "Accueil & Billetterie",
        jobTitle: "Agent d'Accueil & de Billetterie",
        recipient: "À l'attention du Responsable d'Exploitation",
        compAddr: "Cinéma / Salle de Spectacles Lyon",
        compCity: "Lyon, France",
        senderTitle: "Candidat Agent d'Accueil & de Service — Job Étudiant",
        sigTitle: "Candidat Agent d'Accueil · Job Étudiant",
        object: "Candidature au poste d'Agent d'Accueil, de Billetterie et de Service (Job Étudiant)",
        p1: "Passionné par le contact avec le public, la culture et l'univers du spectacle, c'est avec un grand enthousiasme que je vous adresse ma candidature pour le poste d'<strong>Agent d'Accueil, de Billetterie et de Service</strong> au sein de votre établissement lyonnais. Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, je souhaite mettre ma courtoisie, mon dynamisme et mon sens du service au cœur de l'expérience de vos spectateurs.",
        p2: "Mes expériences professionnelles dans le commerce et la relation client m'ont appris à délivrer un accueil chaleureux et irréprochable en toutes circonstances. Au contact direct du public lors de mon activité au Supermarché Champion, j'ai développé une grande aisance relationnelle, le sens de l'orientation et la gestion rapide de la billetterie et des encaissements en période de forte affluence.",
        p3: "Polyvalent et proactif, je suis en mesure d'assurer aussi bien l'accueil physique et l'information des spectateurs, le contrôle des billets aux accès, la vente au comptoir confiserie/snacks, que l'entretien et la vérification des salles avant et après chaque séance. Mon bon niveau d'anglais me permet par ailleurs de renseigner efficacement les spectateurs internationaux.",
        p4: "Reconnu pour ma ponctualité, mon sourire et ma capacité à travailler en équipe dans une ambiance festive et rythmée, je suis disponible sur tous vos créneaux clés : soirées, fins de semaine, jours fériés et vacances scolaires.",
        p5: "Je serais ravi de vous rencontrer lors d'un entretien pour vous témoigner de vive voix de mon engagement à faire vivre une expérience mémorable à vos spectateurs. Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.",
        p6: ""
      },

      adidas: {
        company: "ADIDAS FRANCE",
        roleRef: "CDI 35H - Lyon Part Dieu",
        jobTitle: "Vendeur Polyvalent adidas (H/F/D)",
        recipient: "À l'attention de l'équipe Recrutement Retail",
        compAddr: "CC Westfield La Part-Dieu, 17 Rue Dr Bouchut",
        compCity: "69003 Lyon",
        senderTitle: "Candidat Vendeur Polyvalent — adidas Lyon Part-Dieu",
        sigTitle: "Candidat Vendeur Polyvalent · adidas Lyon Part-Dieu",
        object: "Candidature au poste de Vendeur Polyvalent adidas (H/F/D) — CDI 35H — Lyon Part-Dieu",
        p1: "Passionné par l'univers du sport, l'énergie du lifestyle urbain et les marques qui inspirent le dépassement de soi, c'est avec un enthousiasme sincère que je vous propose ma candidature pour le poste de <strong>Vendeur Polyvalent au sein du magasin adidas Lyon Part-Dieu</strong>. La vision d'adidas — celle d'une communauté de rebelles optimistes qui changent la vie à travers le sport tout en innovant pour la durabilité et l'inclusion — résonne profondément avec mon dynamisme personnel et mon goût du collectif.",
        p2: "Mon parcours m'a permis d'acquérir une solide expérience opérationnelle du commerce et du contact client direct. Lors de mon activité au <strong>Supermarché Champion en 2024</strong>, j'ai développé une grande réactivité sur le terrain : accueil chaleureux, orientation immédiate, gestion d'encaissements rapides et sans erreur lors de forts pics d'affluence, et maintien rigoureux de la propreté et du facing des rayons. Cette immersion m'a appris à garder le sourire, le sang-froid et une écoute active bienveillante en toutes circonstances.",
        p3: "Complétée par une expérience en <strong>plateforme logistique et distribution en 2025</strong>, où j'ai assuré la réception, le contrôle qualité et la remise client avec une rigueur exemplaire, j'ai également piloté chez <strong>Nataan Group</strong> la prospection terrain de plus de <strong>100 commerçants</strong> pour le déploiement d'une solution de point de vente. Cette dernière mission m'a sensibilisé aux <strong>indicateurs clés de performance retail (KPI)</strong> : optimisation du panier moyen, indice de vente, taux de transformation et fidélisation par une expérience client personnalisée.",
        p4: "Rejoindre l'équipe adidas de Lyon Part-Dieu, c'est l'opportunité de devenir un <strong>ambassadeur passionné de la marque</strong>, d'accompagner chaque consommateur de l'accueil jusqu'à l'encaissement, et de contribuer activement à toutes les étapes du magasin (réception des livraisons, mise en rayon, conseil technique et closing). Curieux et résilient, je suis impatient de suivre votre programme certifiant et d'approfondir mes connaissances sur vos innovations produits (technologies running, textile durable, gammes Originals et Performance).",
        p5: "Fidèle aux valeurs de diversité et d'égalité portées par adidas, j'ai à cœur d'apporter mon esprit d'équipe, ma rigueur et ma motivation communicative au service de vos objectifs collectifs. Je suis disponible immédiatement pour un contrat 35H et m'adapte aisément aux plannings du magasin.",
        p6: "Dans l'attente d'un échange lors duquel je serai ravi de vous faire partager mon énergie et mes motivations, je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations sportives et respectueuses."
      },

      apple: {
        company: "APPLE RETAIL FRANCE",
        roleRef: "Rôle #114438069",
        jobTitle: "Spécialiste Apple Retail",
        recipient: "À l'attention de l'équipe Recrutement",
        compAddr: "Apple Store Lyon (Part-Dieu / Confluence)",
        compCity: "Lyon, France",
        senderTitle: "Candidat Spécialiste Apple Retail — Job Étudiant",
        sigTitle: "Candidat Spécialiste Apple Retail · Job Étudiant",
        object: "Candidature au poste de Spécialiste Apple Retail (Job Étudiant / Temps Partiel) — Réf. 114438069",
        p1: "Passionné par l'univers Apple, son sens unique de l'innovation et sa culture de l'excellence humaine, c'est avec un vif enthousiasme que je vous adresse ma candidature pour le poste de <strong>Spécialiste au sein de l'Apple Store de Lyon</strong>. Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, je combine une grande curiosité pour les technologies et un sens naturel du contact humain, des qualités que je souhaite mettre au service de vos clients pour enrichir leur expérience au quotidien.",
        p2: "Mon parcours m'a permis de développer une expérience concrète et éprouvée du commerce et de la relation client. Lors de mon activité au <strong>Supermarché Champion en 2024</strong>, j'ai exercé dans un environnement commercial dynamique et exigeant : accueil chaleureux, orientation immédiate, gestion d'encaissements rapides et rigoureux lors des pics de forte affluence, et maintien d'une tenue de rayon irréprochable. Cette expérience m'a appris à gérer le rythme avec calme, efficacité et un sens permanent de l'empathie.",
        p3: "Par ailleurs, mon expérience en <strong>plateforme logistique et distribution en 2025</strong> m'a apporté une rigueur exemplaire dans la préparation, le suivi précis des commandes et la remise soignée auprès des clients, garantissant un closing de qualité. Chez <strong>Nataan Group</strong>, j'ai prospecté et accompagné plus de 100 professionnels pour le déploiement d'une application POS sous iOS, en veillant au strict respect des standards de fluidité et d'ergonomie propres à l'écosystème Apple.",
        p4: "Ce qui m'attire particulièrement chez Apple Retail, c'est la dimension de conseil désintéressé : poser les bonnes questions, écouter avec bienveillance et proposer la solution personnalisée qui transforme le quotidien d'une personne. Véritable utilisateur au quotidien (iPhone, Mac, iPad, Apple Watch, iCloud, AppleCare), je partage naturellement mes connaissances et mon enthousiasme avec mes collègues et les visiteurs de la Product Zone.",
        p5: "Disponible immédiatement pour des horaires adaptés aux besoins du magasin (soirées, fins de semaine et périodes de forte activité), je partage pleinement vos valeurs d'inclusion, de diversité et d'entraide collective.",
        p6: "Je me tiens à votre disposition pour convenir d'un entretien et vous exprimer de vive voix ma motivation à rejoindre l'équipe Apple Store. Je vous prie d'agréer, Madame, Monsieur, mes salutations distinguées."
      },

      retail_polyvalent: {
        company: "[Enseigne / Magasin]",
        roleRef: "Réf. Offre Magasin",
        jobTitle: "Conseiller de Vente / Vendeur Polyvalent",
        recipient: "À l'attention de l'équipe Recrutement",
        compAddr: "[Adresse du magasin]",
        compCity: "Lyon",
        senderTitle: "Conseiller de Vente & Relation Client — Vendeur Polyvalent",
        sigTitle: "Candidat Conseiller de Vente & Vendeur Polyvalent",
        object: "Candidature au poste de Conseiller de Vente / Vendeur Polyvalent (Réf. Offre Magasin)",
        p1: "Particulièrement sensible à l'excellence de l'expérience client, au rayonnement des marques de référence et aux univers de vente dynamiques, c'est avec une vive motivation que je vous propose ma candidature pour le poste de <strong>Conseiller de Vente / Vendeur Polyvalent</strong> au sein de votre point de vente lyonnais. Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, je combine rigueur méthodologique, grand sens du relationnel et passion pour le contact direct avec le public.",
        p2: "Mes expériences sur le terrain m'ont permis de développer une réelle maîtrise des métiers du commerce de détail. Au <strong>Supermarché Champion en 2024</strong>, j'ai assuré au quotidien l'accueil chaleureux des clients, l'orientation personnalisée en rayon, l'encaissement rapide et fiable durant les pics de forte affluence, ainsi que la tenue soignée des linéaires (réassort, facing et gestion des stocks). Cette expérience m'a appris à gérer le rythme avec calme, efficacité et un sens permanent du sourire.",
        p3: "Par ailleurs, mon travail en <strong>plateforme logistique et distribution en 2025</strong> a renforcé mon sens de l'organisation, mon respect des flux et la rigueur du contrôle qualité jusqu'à la remise au client final. Chez <strong>Nataan Group</strong>, j'ai également prospecté et conseillé plus de <strong>100 commerçants de proximité</strong> pour l'adoption d'une solution d'encaissement et de gestion de caisse, ce qui m'a sensibilisé aux <strong>indicateurs de performance commerciale (KPI retail)</strong> tels que le panier moyen, la vente complémentaire et le taux de fidélisation.",
        p4: "Devenir ambassadeur de votre enseigne représente pour moi l'opportunité de mettre mon enthousiasme et ma polyvalence au service de votre clientèle. De la réception des livraisons jusqu'à la conclusion de la vente, j'aime comprendre les envies de chaque visiteur pour lui apporter un conseil personnalisé et valoriser l'histoire ainsi que les standards de qualité de votre enseigne.",
        p5: "Reconnu pour mon esprit d'équipe, ma curiosité, ma ponctualité et mon respect bienveillant de la diversité, je m'adapte avec aisance à vos contraintes de plannings (disponible immédiatement, en semaine comme le week-end).",
        p6: "Je serais honoré d'échanger avec vous lors d'un prochain entretien pour vous démontrer ma motivation à contribuer au succès de votre équipe. En vous remerciant de l'attention portée à ma candidature, je vous prie d'agréer, Madame, Monsieur, mes salutations respectueuses."
      },

      sephora: {
        company: "SEPHORA FRANCE",
        roleRef: "Conseiller(ère) de Vente Lyon",
        jobTitle: "Conseiller(ère) de Vente & Beauté",
        recipient: "À l'attention de l'équipe Recrutement Magasin",
        compAddr: "Centre Commercial La Part-Dieu / Rue de la République",
        compCity: "69002 Lyon",
        senderTitle: "Candidat Conseiller de Vente & Beauté — Sephora Lyon",
        sigTitle: "Candidat Conseiller de Vente & Beauté · Sephora",
        object: "Candidature au poste de Conseiller(ère) de Vente & Beauté — Sephora Lyon",
        p1: "Inspiré par l'énergie unique, la créativité et la culture inclusive de <strong>Sephora</strong>, c'est avec un grand enthousiasme que je vous soumets ma candidature pour le poste de <strong>Conseiller de Vente au sein de votre boutique lyonnaise</strong>. Étudiant en Master 1 à SUPINFO Lyon, doté d'une forte sensibilité relationnelle et d'une présentation soignée, je souhaite mettre mon dynamisme et mon sens du service au cœur de votre univers beauté.",
        p2: "Mon parcours dans la vente en magasin (Supermarché Champion en 2024) m'a permis de développer une excellente réactivité face aux flux d'affluence : accueil souriant de chaque visiteur, écoute bienveillante, tenue rigoureuse et rapide de caisse, et réassort continu des stands pour garantir une expérience d'achat agréable et impeccable. J'accorde une attention méticuleuse au merchandising et à la mise en valeur des produits.",
        p3: "Par ailleurs, mes missions de conseil auprès de plus de 100 professionnels chez Nataan Group m'ont appris à identifier précisément les besoins de chaque interlocuteur et à formuler des recommandations personnalisées. Je suis également sensibilisé aux <strong>indicateurs clés du commerce retail</strong> : panier moyen, vente complémentaire et développement de la fidélité client.",
        p4: "Rejoindre Sephora, c'est l'opportunité de célébrer la beauté sous toutes ses formes, d'accompagner chaque client avec audace et générosité, et de contribuer à une atmosphère d'équipe stimulante et bienveillante.",
        p5: "Je suis disponible immédiatement, adaptable aux horaires du magasin (week-ends et soirées), et motivé à relever vos challenges commerciaux avec passion.",
        p6: "Je me tiens à votre entière disposition pour convenir d'un entretien et vous exprimer de vive voix ma motivation. Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées."
      },

      hermes: {
        company: "HERMÈS SELLIER",
        roleRef: "Expérience Client Lyon",
        jobTitle: "Conseiller de Vente & Expérience Client",
        recipient: "À l'attention de la Direction de Boutique",
        compAddr: "96 Rue du Président Édouard Herriot",
        compCity: "69002 Lyon",
        senderTitle: "Candidat Conseiller de Vente & Expérience Client — Hermès Lyon",
        sigTitle: "Candidat Conseiller de Vente · Hermès Lyon",
        object: "Candidature au poste de Conseiller de Vente & Expérience Client — Hermès Lyon",
        p1: "Profondément admiratif de l'artisanat d'exception, de la créativité foisonnante et de l'art de recevoir incarnés par la <strong>Maison Hermès</strong>, c'est avec un profond respect que je vous adresse ma candidature pour une fonction de <strong>Conseiller de Vente & Expérience Client au sein de votre magasin lyonnais</strong>. Étudiant en Master 1 à SUPINFO Lyon, je combine une rigueur d'esprit sans faille, une élocution irréprochable et un sens inné de la bienveillance.",
        p2: "Mes expériences professionnelles dans le commerce de détail et la logistique m'ont appris à placer l'exigence du geste et le respect de chaque client au centre de mes priorités. Au contact direct du public, j'ai développé une écoute feutrée, le sens de l'accueil personnalisé et le calme nécessaire pour faire de chaque visite un moment unique et mémorable.",
        p3: "Habitué à la gestion minutieuse des stocks et au soin apporté à la manipulation de produits précieux, j'accorde une importance majeure à la tenue de l'espace de vente, à la discrétion et à la confidentialité. Mon bilinguisme français-anglais me permet en outre d'échanger avec aisance et courtoisie auprès d'une clientèle locale et internationale.",
        p4: "Incarner les valeurs humanistes, la passion des matières nobles et l'élégance de la Maison Hermès constituerait pour moi un engagement sincère et une fierté quotidienne.",
        p5: "Disponible immédiatement, je serais honoré de vous rencontrer lors d'un entretien pour vous témoigner de vive voix mon engagement et mon savoir-être.",
        p6: "Je vous prie d'agréer, Madame, Monsieur, l'expression de ma très haute considération."
      },

      capgemini: {
        company: "CAPGEMINI FRANCE",
        roleRef: "Java / PLM Lyon",
        jobTitle: "Développeur Logiciel (Java / Back-End)",
        recipient: "À l'attention de l'équipe Recrutement",
        compAddr: "43 Rue Pré-Gaudry",
        compCity: "69007 Lyon",
        senderTitle: "Développeur Logiciel — Étudiant Master 1 (Cursus Bac+5)",
        sigTitle: "Étudiant Master 1 SUPINFO Lyon (Bac+5) · Développeur Logiciel",
        object: "Candidature au poste de Développeur Logiciel (Java / Back-End & Environnements Complexes)",
        p1: "Fortement attiré par l'envergure internationale de <strong>Capgemini France</strong>, par l'excellence de ses pratiques d'ingénierie et par la diversité de ses projets de transformation applicative, je souhaite vous soumettre ma candidature pour le poste de <strong>Développeur Logiciel</strong> au sein de vos équipes lyonnaises. Actuellement en <strong>Master 1 Informatique à SUPINFO Lyon (préparant un diplôme Bac+5)</strong> et titulaire d'une Licence en Génie Logiciel, je souhaite mettre ma solide pratique du développement logiciel, de la qualité de code et du travail collaboratif au service de vos projets clients.",
        p2: "Mon parcours technique et mes expériences en ESN et en entreprise m'ont permis de développer des compétences directement transférables aux exigences de votre poste. Récemment chez <strong>Nataan Group</strong> et <strong>ATANYS</strong>, j'ai participé activement à l'ensemble du cycle de vie des applications : analyse fonctionnelle des besoins clients, modélisation relationnelle de bases de données (<strong>SQL, PostgreSQL, MySQL</strong>) et développement d'architectures logicielles fiables. Formé aux concepts avancés de la programmation orientée objet, je maîtrise le développement back-end (<strong>Java, Python</strong>) et dispose d'une forte capacité d'adaptation face à des environnements techniques exigeants.",
        p3: "Particulièrement sensible à la robustesse et à la maintenabilité des solutions, j'ai mené avec succès des campagnes complètes de <strong>recette fonctionnelle et de tests (plus de 100 cas de test exécutés)</strong>, tout en appliquant au quotidien les bonnes pratiques de développement : revues de code, conception de tests unitaires et refactorisation propre. Habitué à évoluer dans un cadre <strong>Agile (Scrum)</strong>, j'accorde une importance majeure à la rédaction d'une documentation technique claire, au suivi rigoureux des évolutions applicatives et à l'amélioration continue des processus de livraison.",
        p4: "Rejoindre les équipes de <strong>Capgemini à Lyon</strong> représente pour moi une formidable opportunité professionnelle au sein de laquelle <strong>mon esprit d'analyse, ma rigueur méthodologique et ma curiosité pour les systèmes d'entreprise (notamment les écosystèmes EAM et PLM)</strong> pourront pleinement se déployer. Mes qualités relationnelles ainsi que mon niveau d'anglais professionnel me permettront de collaborer efficacement avec vos experts métiers et vos équipes multidisciplinaires.",
        p5: "Intégrer vos équipes constitue l'environnement idéal pour apporter une contribution concrète à vos réalisations tout en développant une expertise pointue au contact de professionnels chevronnés.",
        p6: "Je me tiens à votre entière disposition pour convenir d'un entretien afin de vous exposer de vive voix mes motivations et l'adéquation de mon profil avec vos attentes. Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées."
      },

      mobile: {
        company: "[Nom de l'entreprise]",
        roleRef: "Stage / Alternance",
        jobTitle: "Développeur Mobile (Flutter / iOS / Android)",
        recipient: "À l'attention de l'équipe Mobile",
        compAddr: "[Adresse de l'entreprise]",
        compCity: "Lyon",
        senderTitle: "Développeur Mobile — Étudiant Master 1 (Bac+5)",
        sigTitle: "Étudiant Master 1 SUPINFO Lyon · Dév. Mobile",
        object: "Candidature au poste de Développeur Mobile (Flutter / iOS / Android)",
        p1: "Passionné par l'écosystème mobile et le développement d'applications performantes et intuitives, je souhaite vous soumettre ma candidature pour le poste de <strong>Développeur Mobile (Flutter / iOS)</strong>. Actuellement en <strong>Master 1 Informatique à SUPINFO Lyon (Bac+5)</strong> et titulaire d'une Licence en Génie Logiciel, je mets à votre disposition mon expérience pratique dans la conception, le portage et le déploiement d'applications mobiles complètes sur les stores.",
        p2: "Lors de mon récent stage chez <strong>Nataan Group</strong>, j'ai co-développé l'application mobile BoutiK sous <strong>Flutter</strong> avec backend <strong>Firebase</strong> et intégration de paiements (FedaPay). J'y ai piloté le portage sous iOS, la conformité aux guidelines Apple, l'intégration des notifications push <strong>APNs</strong> et la mise en production sur <strong>App Store Connect</strong>. Précédemment chez Darollo Technologies, j'ai conçu une application Flutter avec architecture <em>offline-first</em> et synchronisation automatique de données.",
        p3: "Au-delà du développement pur, j'accorde une importance capitale à l'assurance qualité et à l'expérience utilisateur. J'ai notamment conduit des audits UI/UX et la recette fonctionnelle complète de plateformes (plus de 100 cas de test). Habitué au travail collaboratif en méthode Agile (Scrum) et à l'utilisation rigoureuse de Git, je m'engage à produire un code testé, maintenable et documenté.",
        p4: "Rejoindre vos équipes représente pour moi une opportunité unique d'apporter mon expertise sur Flutter et iOS, tout en participant activement à vos futurs déploiements mobiles avec proactivité et rigueur.",
        p5: "Disponible pour un stage ou une alternance, je m'adapte avec rapidité à votre stack technique et à vos méthodes de travail.",
        p6: "Je reste à votre entière disposition pour tout échange et vous prie d'agréer, Madame, Monsieur, mes sincères salutations."
      },

      fullstack: {
        company: "[Nom de l'entreprise]",
        roleRef: "Stage / Alternance",
        jobTitle: "Développeur Full-Stack (Python / Django / Laravel / Web)",
        recipient: "À l'attention du Responsable Technique",
        compAddr: "[Adresse de l'entreprise]",
        compCity: "Lyon",
        senderTitle: "Développeur Full-Stack — Étudiant Master 1 (Bac+5)",
        sigTitle: "Étudiant Master 1 SUPINFO Lyon · Dév. Full-Stack",
        object: "Candidature au poste de Développeur Full-Stack (Python / Django / Laravel / Web)",
        p1: "Fortement motivé par le développement d'applications web modernes, évolutives et sécurisées, je vous propose ma candidature pour le poste de <strong>Développeur Full-Stack</strong>. Actuellement étudiant en <strong>Master 1 Informatique à SUPINFO Lyon (cursus Bac+5)</strong> et diplômé d'une Licence en Génie Logiciel, je possède une expérience éprouvée sur l'ensemble de la chaîne de développement web et back-end.",
        p2: "Mon parcours m'a permis de maîtriser des frameworks robustes tels que <strong>Django, Laravel</strong> ainsi que les langages <strong>Python, PHP et JavaScript</strong>. Chez ATANYS, j'ai conçu et déployé de bout en bout une plateforme web complète (analyse des besoins, modélisation de bases SQL sous MySQL/PostgreSQL, développement back/front et tests). Plus récemment, j'ai enrichi cette expertise par l'audit ergonomique UI/UX et la refonte de sites web institutionnels.",
        p3: "Rigoureux sur la qualité logicielle, je maîtrise l'intégration de tests automatisés, la sécurité applicative et la structuration des bases de données relationnelles. À l'aise dans les environnements Agiles, j'accorde une grande attention aux revues de code, au versioning Git et à la documentation technique.",
        p4: "Intégrer votre équipe me permettra d'apporter mon dynamisme, ma capacité d'apprentissage rapide et ma rigueur technique pour concevoir des fonctionnalités à fort impact pour vos utilisateurs.",
        p5: "Disponible immédiatement à Lyon pour une alternance ou un stage, je serais ravi de m'investir sur vos projets de grande envergure.",
        p6: "Je me tiens à votre disposition pour convenir d'un entretien et vous prie d'agréer, Madame, Monsieur, mes salutations distinguées."
      },

      qa: {
        company: "[Nom de l'entreprise]",
        roleRef: "Stage / Alternance QA",
        jobTitle: "Ingénieur QA & Qualité Logicielle",
        recipient: "À l'attention du Responsable Qualité / QA",
        compAddr: "[Adresse de l'entreprise]",
        compCity: "Lyon",
        senderTitle: "Ingénieur QA & Testeur — Étudiant Master 1 (Bac+5)",
        sigTitle: "Étudiant Master 1 SUPINFO Lyon · Ingénieur QA",
        object: "Candidature au poste d'Ingénieur QA / Testeur Logiciel & Recette",
        p1: "Convaincu que la qualité logicielle est le pilier central de la satisfaction utilisateur et de la performance technique, je vous adresse ma candidature pour le poste d'<strong>Ingénieur QA / Développeur Test & Qualité</strong>. Étudiant en <strong>Master 1 Informatique à SUPINFO Lyon (Bac+5)</strong>, j'allie une solide culture de développement logiciel à une expertise pratique de la recette fonctionnelle.",
        p2: "Chez Nataan Group, j'ai pris en charge la recette fonctionnelle complète d'un site institutionnel avec la conception, l'exécution et le suivi de <strong>103 cas de test</strong>, garantissant une conformité rigoureuse avec le cahier des charges et la détection précoce des régressions. J'ai également géré la mise en conformité stricte d'une application mobile pour sa validation sur l'App Store d'Apple.",
        p3: "Grâce à mon bagage de développeur (Java, Python, SQL), je comprends en profondeur les architectures applicatives, ce qui me permet d'échanger efficacement avec les équipes de développement, de participer aux revues de code et de mettre en place des tests unitaires pertinents.",
        p4: "Ma rigueur d'analyse, mon souci du détail et mon esprit d'équipe seront des atouts immédiats pour renforcer la fiabilité de vos livraisons logicielles.",
        p5: "Disponible pour un stage ou une alternance à Lyon, je souhaite contribuer activement à l'excellence de vos produits.",
        p6: "Je me tiens à votre entière disposition pour un entretien et vous prie d'agréer, Madame, Monsieur, mes salutations respectueuses."
      }
    };

    // UPDATE OBJECT FROM HELPER INPUTS
    function updateLetterObjectFromInputs() {
      const jobTitle = document.getElementById('input-job-title').value.trim();
      const roleRef = document.getElementById('input-role-ref').value.trim();

      let computedObject = "Candidature au poste de " + jobTitle;
      if (roleRef) {
        computedObject += " (Réf. " + roleRef + ")";
      }

      document.getElementById('input-object').value = computedObject;
      document.getElementById('doc-object').innerText = computedObject;
      autoSaveLetter();
    }

    // SYNC FORM TO PREVIEW
    function syncField(field, value) {
      if (field === 'company') {
        document.getElementById('doc-company').innerText = value;
      } else if (field === 'recipient') {
        document.getElementById('doc-recipient').innerText = value;
      } else if (field === 'compAddr') {
        document.getElementById('doc-comp-addr').innerText = value;
      } else if (field === 'compCity') {
        document.getElementById('doc-comp-city').innerText = value;
      } else if (field === 'object') {
        document.getElementById('doc-object').innerText = value;
      } else if (field === 'senderName') {
        document.getElementById('doc-sender-name').innerText = value;
        document.getElementById('doc-sig-name').innerText = value;
      } else if (field === 'senderTitle') {
        document.getElementById('doc-sender-title').innerText = value;
      } else if (field === 'senderAddr') {
        document.getElementById('doc-sender-addr').innerText = value;
      } else if (field === 'senderCity') {
        document.getElementById('doc-sender-city').innerText = value;
      } else if (field === 'senderPhone') {
        document.getElementById('doc-sender-phone').innerText = value;
      } else if (field === 'senderEmail') {
        document.getElementById('doc-sender-email').innerText = value;
      }
      autoSaveLetter();
    }

    function syncDate() {
      const place = document.getElementById('input-place').value;
      const date = document.getElementById('input-date').value;
      document.getElementById('doc-date-line').innerText = place + ", le " + date;
      autoSaveLetter();
    }

    // LOAD PRESET
    function loadPreset(key) {
      document.querySelectorAll('.btn-preset').forEach(b => b.classList.remove('active'));
      if (event && event.target) {
        const btn = event.target.closest('.btn-preset');
        if (btn) btn.classList.add('active');
      }

      const p = presets[key];
      if (!p) return;

      document.getElementById('input-company').value = p.company;
      document.getElementById('doc-company').innerText = p.company;

      document.getElementById('input-role-ref').value = p.roleRef || "";
      document.getElementById('input-job-title').value = p.jobTitle || "";

      document.getElementById('input-recipient').value = p.recipient;
      document.getElementById('doc-recipient').innerText = p.recipient;

      document.getElementById('input-comp-addr').value = p.compAddr;
      document.getElementById('doc-comp-addr').innerText = p.compAddr;

      document.getElementById('input-comp-city').value = p.compCity;
      document.getElementById('doc-comp-city').innerText = p.compCity;

      document.getElementById('input-sender-title').value = p.senderTitle;
      document.getElementById('doc-sender-title').innerText = p.senderTitle;
      document.getElementById('doc-sig-title').innerText = p.sigTitle;

      document.getElementById('input-object').value = p.object;
      document.getElementById('doc-object').innerText = p.object;

      document.getElementById('p1').innerHTML = p.p1;
      document.getElementById('p2').innerHTML = p.p2;
      document.getElementById('p3').innerHTML = p.p3;
      document.getElementById('p4').innerHTML = p.p4;
      document.getElementById('p5').innerHTML = p.p5;
      document.getElementById('p6').innerHTML = p.p6;

      // Update direct PDF download button
      const presetLetterPdfFiles = {
        soutien_scolaire: 'Lettre_de_Motivation_Soutien_Scolaire_Rodrigue_HESSOU.pdf',
        macdo: 'Lettre_de_Motivation_MacDo_Rodrigue_HESSOU.pdf',
        apple_retail: 'Lettre_de_Motivation_Apple_Retail_Rodrigue_HESSOU.pdf',
        adidas_retail: 'Lettre_de_Motivation_Adidas_Rodrigue_HESSOU.pdf',
        retail_polyvalent: 'Lettre_de_Motivation_Retail_Polyvalent.pdf',
        capgemini_stage: 'Lettre_de_Motivation_Rodrigue_HESSOU.pdf',
        dev_alternance: 'Lettre_de_Motivation_Rodrigue_HESSOU.pdf'
      };
      const directBtn = document.getElementById('btn-download-preset-pdf');
      if (directBtn) {
        const file = presetLetterPdfFiles[key] || 'Lettre_de_Motivation_Rodrigue_HESSOU.pdf';
        directBtn.href = file;
        directBtn.setAttribute('download', file);
      }

      const label = key.toUpperCase();
      showToast("Modèle " + label + " chargé avec succès !");
      autoSaveLetter();
    }

    // PRINT / EXPORT
    function printToPDF() {
      showToast("💡 Astuce : Dans la fenêtre d'impression, vérifiez que 'Graphiques d'arrière-plan' est coché !");
      setTimeout(() => {
        window.print();
      }, 350);
    }

    function copyLetterText() {
      const el = document.getElementById('printable-letter');
      const text = el.innerText;
      navigator.clipboard.writeText(text).then(() => {
        showToast("Texte de la lettre copié dans le presse-papier !");
      }).catch(() => {
        showToast("Erreur lors de la copie du texte.");
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
    function autoSaveLetter() {
      try {
        localStorage.setItem('rodrigue_letter_saved', document.getElementById('printable-letter').innerHTML);
      } catch(e) {}
    }

    function resetToDefault() {
      localStorage.removeItem('rodrigue_letter_saved');
      loadPreset('soutien_scolaire');
      showToast("Lettre réinitialisée aux paramètres par défaut.");
    }

    window.addEventListener('DOMContentLoaded', () => {
      loadPreset('soutien_scolaire');
      document.querySelectorAll('[contenteditable="true"]').forEach(el => {
        el.addEventListener('input', autoSaveLetter);
      });
    });
  </script>

</body>
</html>
"""

with open('editeur_lettre_motivation.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("editeur_lettre_motivation.html updated with student jobs!")
