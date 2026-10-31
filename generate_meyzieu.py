import base64
import subprocess
import fitz

with open('photo.jpg', 'rb') as f:
    photo_b64 = base64.b64encode(f.read()).decode('utf-8')

# ==========================================
# 1. CV MEYZIEU - AGENT DES ÉCOLES & RESTAURATION SCOLAIRE
# ==========================================
cv_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>CV - Rodrigue HESSOU - Agent des écoles et de restauration scolaire</title>
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
    justify-content: space-between;
    font-size: 8.5pt;
    line-height: 1.25;
  }}

  .photo-container {{
    text-align: center;
    margin-bottom: 2mm;
  }}

  .photo-container img {{
    width: 28mm;
    height: 28mm;
    border-radius: 50%;
    object-fit: cover;
    border: 1.8px solid #94a3b8;
  }}

  .sidebar h3 {{
    font-size: 9.5pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #38bdf8;
    border-bottom: 1px solid #475569;
    padding-bottom: 1mm;
    margin-top: 2.2mm;
    margin-bottom: 1.8mm;
    font-weight: 700;
  }}

  .contact-item {{
    margin-bottom: 1.2mm;
    word-break: break-all;
    font-size: 8.5pt;
  }}

  .contact-item strong {{
    color: #cbd5e1;
    display: block;
    font-size: 7.8pt;
    text-transform: uppercase;
  }}

  .skill-badge {{
    display: inline-block;
    background: #334155;
    color: #f8fafc;
    padding: 1.1mm 2.2mm;
    border-radius: 3px;
    margin: 0.7mm 0.7mm 0.7mm 0;
    font-size: 8pt;
  }}

  .lang-item, .qual-item {{
    margin-bottom: 1.1mm;
    font-size: 8.2pt;
  }}

  .main-content {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  .header {{
    border-bottom: 2px solid #0284c7;
    padding-bottom: 2mm;
    margin-bottom: 1.5mm;
  }}

  .header h1 {{
    font-size: 19pt;
    font-weight: 700;
    color: #0f172a;
    letter-spacing: -0.3px;
    line-height: 1.1;
  }}

  .header h2 {{
    font-size: 10.8pt;
    font-weight: 700;
    color: #0284c7;
    text-transform: uppercase;
    margin-top: 1mm;
    letter-spacing: 0.3px;
  }}

  .header .ref-pill {{
    display: inline-block;
    background-color: #f1f5f9;
    color: #475569;
    font-size: 8.2pt;
    font-weight: 700;
    padding: 0.6mm 2mm;
    border-radius: 3px;
    border: 1px solid #cbd5e1;
    margin-top: 1mm;
  }}

  .profile-summary {{
    font-size: 8.6pt;
    line-height: 1.28;
    color: #334155;
    margin-top: 1.5mm;
    text-align: justify;
  }}

  .section {{
    margin-top: 1.8mm;
  }}

  .section-title {{
    font-size: 10.2pt;
    font-weight: 700;
    color: #0f172a;
    text-transform: uppercase;
    border-bottom: 1.2px solid #e2e8f0;
    padding-bottom: 0.8mm;
    margin-bottom: 1.6mm;
    letter-spacing: 0.4px;
    display: flex;
    align-items: center;
    gap: 1.5mm;
  }}

  .section-title::before {{
    content: "";
    display: inline-block;
    width: 3.5mm;
    height: 3.5mm;
    background-color: #0284c7;
    border-radius: 1px;
  }}

  .job-item {{
    margin-bottom: 2.2mm;
  }}

  .job-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 9pt;
  }}

  .job-role {{
    font-weight: 700;
    color: #0f172a;
  }}

  .job-company {{
    color: #0284c7;
    font-weight: 700;
  }}

  .job-date {{
    font-size: 8.2pt;
    color: #64748b;
    font-style: italic;
  }}

  .job-desc {{
    font-size: 8.3pt;
    line-height: 1.24;
    color: #334155;
    margin-top: 0.8mm;
    padding-left: 2.8mm;
  }}

  .job-desc li {{
    margin-bottom: 0.6mm;
    list-style-type: square;
  }}

  .job-desc li::marker {{
    color: #0284c7;
    font-size: 0.75em;
  }}

  .edu-item {{
    margin-bottom: 1.4mm;
  }}

  .edu-degree {{
    font-size: 8.8pt;
    font-weight: 700;
    color: #0f172a;
  }}

  .edu-school {{
    font-size: 8.2pt;
    color: #475569;
  }}
</style>
</head>
<body>

  <!-- SIDEBAR (GAUCHE) -->
  <aside class="sidebar">
    <div>
      <div class="photo-container">
        <img src="data:image/jpeg;base64,{photo_b64}" alt="Rodrigue HESSOU">
      </div>

      <h3>Contact</h3>
      <div class="contact-item">
        <strong>Adresse</strong>
        Lyon (69000), France<br>
        <em>Accès rapide Métropole / Meyzieu</em>
      </div>
      <div class="contact-item">
        <strong>Téléphone</strong>
        +33 7 44 11 75 73
      </div>
      <div class="contact-item">
        <strong>Email</strong>
        rodriguehessou14@gmail.com
      </div>
      <div class="contact-item">
        <strong>Disponibilité</strong>
        Immédiate (Temps complet)
      </div>

      <h3>Compétences Hygiène & Service</h3>
      <div>
        <span class="skill-badge">Respect normes HACCP</span>
        <span class="skill-badge">Entretien des locaux</span>
        <span class="skill-badge">Protocoles sanitaires</span>
        <span class="skill-badge">Remise en température</span>
        <span class="skill-badge">Service à table / Ligne</span>
        <span class="skill-badge">Gestion plonge & tri</span>
        <span class="skill-badge">Encadrement bienveillant</span>
        <span class="skill-badge">Surveillance cour & réfectoire</span>
      </div>

      <h3>Qualités Humaines</h3>
      <div class="qual-item">&bull; Sens aigu du service public</div>
      <div class="qual-item">&bull; Écoute, pédagogie & patience</div>
      <div class="qual-item">&bull; Ponctualité & rigueur (dès 6h)</div>
      <div class="qual-item">&bull; Dynamisme & résistance au rush</div>
      <div class="qual-item">&bull; Esprit d'équipe solidaire</div>

      <h3>Langues</h3>
      <div class="lang-item"><strong>Français :</strong> Courant / Langue de travail</div>
      <div class="lang-item"><strong>Anglais :</strong> Niveau B2 opérationnel</div>
    </div>

    <div>
      <h3>Atouts Pratiques</h3>
      <div style="font-size: 7.9pt; color: #94a3b8; line-height: 1.2;">
        Ponctuel sur les plages 6h-9h et 9h-15h. Bonne condition physique, port de charges et gestes sécuritaires validés.
      </div>
    </div>
  </aside>

  <!-- CONTENU PRINCIPAL (DROITE) -->
  <main class="main-content">
    <div>
      <header class="header">
        <h1>Rodrigue HESSOU</h1>
        <h2>Agent des Écoles & de Restauration Scolaire</h2>
        <div class="ref-pill">Candidature Réf. : Poste numéro 3245-09_PT &bull; Ville de Meyzieu</div>
        <p class="profile-summary">
          Candidat rigoureux, ponctuel et doté d'un excellent relationnel avec les enfants, je propose mes services à la Ville de Meyzieu. Fort d'une expérience concrète en milieu scolaire (tutorat et accompagnement pédagogique de groupes d'élèves), en logistique rigoureuse et en polyvalence terrain (respect scrupuleux des règles d'hygiène, nettoyage, cadence et accueil), j'ai à cœur d'assurer l'entretien irréprochable des classes, la surveillance sécurisante des récréations et le bon déroulement du service de restauration scolaire dans le strict respect de la méthode HACCP.
        </p>
      </header>

      <!-- EXPERIENCES PROFESSIONNELLES -->
      <section class="section">
        <h3 class="section-title">Expériences Professionnelles & Terrain</h3>

        <!-- Soutien Scolaire / Encadrement Enfants -->
        <div class="job-item">
          <div class="job-header">
            <div>
              <span class="job-role">Tuteur & Animateur de Soutien Scolaire</span> &mdash; <span class="job-company">Acadomia & Cours Particuliers</span>
            </div>
            <span class="job-date">2024 - 2026 | Lyon</span>
          </div>
          <ul class="job-desc">
            <li><strong>Encadrement et posture bienveillante :</strong> Accueil, écoute active et accompagnement d'enfants et adolescents dans un climat sécurisant et structuré.</li>
            <li><strong>Médiation et respect des règles :</strong> Gestion de groupe, maintien de l'attention et transmission positive des règles de vie collective.</li>
            <li><strong>Communication adaptée :</strong> Échange constructif avec les parents et les équipes éducatives sur le bien-être et le suivi des élèves.</li>
          </ul>
        </div>

        <!-- Logistique & Entretien / Rigueur -->
        <div class="job-item">
          <div class="job-header">
            <div>
              <span class="job-role">Préparateur de Commandes & Logistique</span> &mdash; <span class="job-company">Plateforme Logistique</span>
            </div>
            <span class="job-date">2025 | Région Lyonnaise</span>
          </div>
          <ul class="job-desc">
            <li><strong>Organisation et ponctualité :</strong> Prise de poste matinale dès les premières heures, réactivité et gestion efficace du temps.</li>
            <li><strong>Règles d'hygiène et de sécurité :</strong> Respect strict des protocoles de manutention, nettoyage et rangement méthodique de l'espace de travail.</li>
            <li><strong>Sens du collectif :</strong> Coordination avec les équipes d'exploitation pour garantir le respect rigoureux des délais et des normes.</li>
          </ul>
        </div>

        <!-- Employé Polyvalent / Hygiène & Service -->
        <div class="job-item">
          <div class="job-header">
            <div>
              <span class="job-role">Employé Polyvalent & Tenue des Espaces</span> &mdash; <span class="job-company">Supermarché Champion</span>
            </div>
            <span class="job-date">2024</span>
          </div>
          <ul class="job-desc">
            <li><strong>Nettoyage et entretien des locaux :</strong> Désinfection, balayage, lavage des surfaces de circulation et maintien d'une propreté exemplaire.</li>
            <li><strong>Respect de la chaîne du froid & HACCP :</strong> Contrôle systématique des dates limites de consommation (DLC) et retrait immédiat des denrées non conformes.</li>
            <li><strong>Gestion des pics d'affluence :</strong> Esprit d'équipe, rapidité d'exécution et courtoisie permanente au service des usagers.</li>
          </ul>
        </div>

        <!-- Polyvalence Projets / Rigueur -->
        <div class="job-item">
          <div class="job-header">
            <div>
              <span class="job-role">Assistant Déploiement Terrain & Recette</span> &mdash; <span class="job-company">Nataan Group</span>
            </div>
            <span class="job-date">2026</span>
          </div>
          <ul class="job-desc">
            <li><strong>Application rigoureuse de cahiers des charges :</strong> Suivi méthodique de plus de 100 protocoles de contrôle qualité sans écart.</li>
            <li><strong>Aisance relationnelle :</strong> Contact direct avec différents interlocuteurs, écoute et sens du service.</li>
          </ul>
        </div>
      </section>

      <!-- FORMATION -->
      <section class="section">
        <h3 class="section-title">Formation & Diplômes</h3>
        <div class="edu-item">
          <div class="job-header">
            <span class="edu-degree">Cursus Universitaire Bac+4 / Bac+5 (Master)</span>
            <span class="job-date">2026 - Présent</span>
          </div>
          <div class="edu-school">SUPINFO Lyon &bull; Rigueur d'analyse, autonomie et organisation personnelle</div>
        </div>

        <div class="edu-item">
          <div class="job-header">
            <span class="edu-degree">Licence Professionnelle (Mention Bien)</span>
            <span class="job-date">2022 - 2025</span>
          </div>
          <div class="edu-school">IAI-TOGO &bull; Méthode, assiduité et travail en équipe</div>
        </div>

        <div class="edu-item">
          <div class="job-header">
            <span class="edu-degree">Baccalauréat Scientifique</span>
            <span class="job-date">2021 - 2022</span>
          </div>
          <div class="edu-school">Lycée Le Rossignol &bull; Maîtrise des protocoles et rigueur scientifique</div>
        </div>
      </section>
    </div>

    <!-- PIED DE CV -->
    <div style="border-top: 1px solid #e2e8f0; padding-top: 1.5mm; font-size: 7.8pt; color: #64748b; display: flex; justify-content: space-between;">
      <span>Candidature Ville de Meyzieu &bull; Réf. 3245-09_PT</span>
      <span>Disponible immédiatement &bull; Permis / Mobilité Métropole de Lyon</span>
    </div>
  </main>

</body>
</html>
"""

with open('CV_Rodrigue_HESSOU_Meyzieu.html', 'w', encoding='utf-8') as f:
    f.write(cv_html)

# ==========================================
# 2. LETTRE DE MOTIVATION MEYZIEU
# ==========================================
letter_html = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Lettre de Motivation - Rodrigue HESSOU - Agent des écoles et de restauration scolaire - Ville de Meyzieu</title>
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
    padding: 16mm 20mm 15mm 20mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    line-height: 1.42;
  }

  .header-block {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 5mm;
  }

  .sender-info {
    font-size: 9.8pt;
    color: #1e293b;
    line-height: 1.35;
  }

  .sender-name {
    font-size: 13.5pt;
    font-weight: 700;
    color: #0f172a;
    letter-spacing: -0.2px;
    margin-bottom: 1.5mm;
  }

  .recipient-info {
    font-size: 9.8pt;
    color: #1e293b;
    line-height: 1.35;
    text-align: right;
    max-width: 85mm;
  }

  .recipient-title {
    font-weight: 700;
    color: #0f172a;
    font-size: 10.5pt;
  }

  .date-place {
    text-align: right;
    font-size: 9.5pt;
    color: #64748b;
    margin-bottom: 4.5mm;
    font-style: italic;
  }

  .subject-block {
    background-color: #f8fafc;
    border-left: 3.5px solid #0284c7;
    padding: 2.8mm 4mm;
    margin-bottom: 5mm;
    font-size: 10pt;
    color: #0f172a;
  }

  .subject-title {
    font-weight: 700;
  }

  .ref-line {
    font-size: 9pt;
    color: #475569;
    margin-top: 0.8mm;
  }

  .salutation {
    font-size: 10.2pt;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 3.5mm;
  }

  .letter-body {
    font-size: 9.7pt;
    color: #334155;
    text-align: justify;
    line-height: 1.44;
    display: flex;
    flex-direction: column;
    gap: 3.2mm;
  }

  .letter-body p {
    margin: 0;
  }

  .valediction {
    font-size: 9.7pt;
    color: #334155;
    margin-top: 1mm;
  }

  .signature-block {
    display: flex;
    justify-content: flex-end;
    margin-top: 3mm;
  }

  .signature-box {
    text-align: right;
  }

  .signature-name {
    font-size: 11pt;
    font-weight: 700;
    color: #0f172a;
  }

  .signature-subtitle {
    font-size: 8.8pt;
    color: #64748b;
    margin-top: 0.8mm;
  }

  .footer-note {
    border-top: 1px solid #e2e8f0;
    padding-top: 2.5mm;
    font-size: 8pt;
    color: #94a3b8;
    display: flex;
    justify-content: space-between;
  }
</style>
</head>
<body>

  <div>
    <!-- EN-TETE : EXPEDITEUR / DESTINATAIRE -->
    <div class="header-block">
      <div class="sender-info">
        <div class="sender-name">Rodrigue HESSOU</div>
        <div>Lyon, France</div>
        <div>Téléphone : +33 7 44 11 75 73</div>
        <div>Email : rodriguehessou14@gmail.com</div>
        <div>Disponibilité : Immédiate (Temps complet)</div>
      </div>

      <div class="recipient-info">
        <div class="recipient-title">À l'attention de Monsieur le Maire</div>
        <div>Hôtel de Ville &mdash; Direction des Ressources Humaines</div>
        <div>Place de l'Europe &mdash; CS 30401</div>
        <div>69330 MEYZIEU CEDEX</div>
      </div>
    </div>

    <!-- DATE ET LIEU -->
    <div class="date-place">
      Fait à Lyon, le 31 octobre 2026
    </div>

    <!-- OBJET ET REFERENCE OBLIGATOIRE -->
    <div class="subject-block">
      <div class="subject-title">Objet : Candidature au poste d'Agent des écoles et de restauration scolaire (H/F)</div>
      <div class="ref-line"><strong>Référence interne obligatoire :</strong> Poste numéro 3245-09_PT &bull; Cadre d'emplois des adjoints techniques territoriaux</div>
    </div>

    <!-- CORPS DE LA LETTRE -->
    <div class="salutation">Monsieur le Maire,</div>

    <div class="letter-body">
      <p>
        Particulièrement motivé à l'idée de contribuer activement à la qualité du service public d'accueil et d'épanouissement des jeunes Meyziards, j'ai l'honneur de vous adresser ma candidature pour le poste d'Agent des écoles et de restauration scolaire au sein des établissements de la Ville de Meyzieu (référence interne 3245-09_PT).
      </p>

      <p>
        La polyvalence et l'amplitude des missions décrites correspondent parfaitement à mes compétences et à mes valeurs. Conscient qu'un environnement scolaire propre et accueillant est indispensable au bien-être des enfants et des enseignants, je maîtrise l'ensemble des protocoles de nettoyage, de désinfection et d'entretien des locaux (classes, couloirs, sanitaires). Ponctuel, rigoureux et autonome, je suis pleinement disposé à assurer les interventions matinales dès 6h00 dans le respect le plus strict des consignes de sécurité et d'hygiène.
      </p>

      <p>
        Sur le volet de la restauration collective, mon expérience professionnelle m'a habitué aux exigences de la méthode HACCP, à la vérification scrupuleuse des dates de péremption, à la remise en température des préparations culinaires, à la distribution soignée des repas ainsi qu'à la tenue impeccable de la plonge et au tri des déchets. Lors des temps de repas et des récréations méridiennes, mon sens de l'écoute, ma patience et mon expérience confirmée dans l'encadrement d'enfants (notamment lors de séances de soutien scolaire et d'animation de groupes) me permettent de veiller avec fermeté et bienveillance à la sécurité physique et affective des élèves.
      </p>

      <p>
        Doté d'une excellente condition physique, d'une grande adaptabilité et d'un esprit d'équipe solidaire, je m'intègre avec enthousiasme et respect auprès des équipes pédagogiques et des agents territoriaux pour faire de la journée d'école un moment serein et agréable pour chaque enfant.
      </p>

      <p>
        Disponible immédiatement pour rejoindre vos services, je me tiens à votre entière disposition pour tout entretien à votre convenance afin de vous exposer de vive voix ma détermination et mon engagement au service de la collectivité de Meyzieu.
      </p>

      <p class="valediction">
        Je vous prie d'agréer, Monsieur le Maire, l'expression de ma très haute considération.
      </p>
    </div>

    <!-- SIGNATURE -->
    <div class="signature-block">
      <div class="signature-box">
        <div class="signature-name">Rodrigue HESSOU</div>
        <div class="signature-subtitle">Candidat &bull; Agent des écoles et de restauration scolaire</div>
      </div>
    </div>
  </div>

  <!-- PIED DE PAGE -->
  <div class="footer-note">
    <span>Candidature Ville de Meyzieu &bull; Réf. 3245-09_PT</span>
    <span>Pièces jointes : Curriculum Vitæ adapté & Lettre de motivation</span>
  </div>

</body>
</html>
"""

with open('Lettre_de_Motivation_Meyzieu_Rodrigue_HESSOU.html', 'w', encoding='utf-8') as f:
    f.write(letter_html)

# ==========================================
# 3. CONVERSION EN PDF AVEC CHROME HEADLESS
# ==========================================
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Convert CV
cmd_cv = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--print-to-pdf=CV_Rodrigue_HESSOU_Meyzieu.pdf",
    "CV_Rodrigue_HESSOU_Meyzieu.html"
]
subprocess.run(cmd_cv, check=True)

# Convert Letter
cmd_letter = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--print-to-pdf=Lettre_de_Motivation_Meyzieu_Rodrigue_HESSOU.pdf",
    "Lettre_de_Motivation_Meyzieu_Rodrigue_HESSOU.html"
]
subprocess.run(cmd_letter, check=True)

# ==========================================
# 4. VERIFICATION PYMUPDF (EXACT 1 PAGE A4)
# ==========================================
doc_cv = fitz.open('CV_Rodrigue_HESSOU_Meyzieu.pdf')
print(f"CV Meyzieu pages: {len(doc_cv)}")
doc_letter = fitz.open('Lettre_de_Motivation_Meyzieu_Rodrigue_HESSOU.pdf')
print(f"Lettre Meyzieu pages: {len(doc_letter)}")

# Render preview image
page_cv = doc_cv[0]
pix_cv = page_cv.get_pixmap(dpi=150)
pix_cv.save("CV_Rodrigue_HESSOU_Meyzieu_preview.png")

page_letter = doc_letter[0]
pix_letter = page_letter.get_pixmap(dpi=150)
pix_letter.save("Lettre_de_Motivation_Meyzieu_Rodrigue_HESSOU_preview.png")

print("Files generated and verified successfully!")
