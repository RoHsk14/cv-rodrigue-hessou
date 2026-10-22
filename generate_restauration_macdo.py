import base64
import subprocess
import fitz

with open('photo.jpg', 'rb') as f:
    photo_b64 = base64.b64encode(f.read()).decode('utf-8')

# 1. CV MACDONALD'S / RESTAURATION RAPIDE
cv_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>CV - Rodrigue HESSOU - Équipier Polyvalent de Restauration</title>
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

    <!-- DISPONIBILITÉ RESTAURATION -->
    <div class="sidebar-section">
      <div class="sidebar-title">Disponibilités</div>
      <div class="sidebar-item">
        <strong>Temps Partiel Étudiant</strong>
        Soirées (rushs & fermetures), week-ends complets, jours fériés et vacances scolaires
      </div>
    </div>

    <!-- LANGUES -->
    <div class="sidebar-section">
      <div class="sidebar-title">Langues</div>
      <div class="sidebar-item">
        <strong>Français</strong>
        Langue maternelle — élocution soignée et aisance relationnelle
      </div>
      <div class="sidebar-item">
        <strong>Anglais</strong>
        Niveau B1/B2 — prise de commande clientèle internationale
      </div>
    </div>

    <!-- ATOUTS RESTAURATION RAPIDE -->
    <div class="sidebar-section">
      <div class="sidebar-title">Atouts Opérationnels</div>
      <div class="sidebar-item">
        <strong>Gestion du Rythme & Rushs</strong>
        Sang-froid en pic d'affluence, rapidité d'exécution et dynamisme continu
      </div>
      <div class="sidebar-item">
        <strong>Hygiène & Sécurité (HACCP)</strong>
        Respect scrupuleux des normes sanitaires, propreté irréprochable et traçabilité
      </div>
      <div class="sidebar-item">
        <strong>Polyvalence Salle / Cuisine / Drive</strong>
        Assemblage sandwichs, friture, caisse, accueil bornes et propreté salle
      </div>
      <div class="sidebar-item">
        <strong>Esprit d'Équipe & Communication</strong>
        Coordination rapide, solidarité entre équipiers et sourire communicatif
      </div>
    </div>

    <!-- QUALITÉS -->
    <div class="sidebar-section">
      <div class="sidebar-title">Qualités</div>
      <ul class="sidebar-list">
        <li>Ponctualité stricte et assiduité</li>
        <li>Énergie, enthousiasme et endurance physique</li>
        <li>Rigueur, propreté et respect des procédures</li>
        <li>Sens de l'accueil et bienveillance client</li>
      </ul>
    </div>

    <!-- CENTRES D'INTÉRÊT -->
    <div class="sidebar-section">
      <div class="sidebar-title">Centres d'intérêt</div>
      <div class="sidebar-item compact">Football & Esprit d'équipe</div>
      <div class="sidebar-item compact">Course à pied & Endurance</div>
      <div class="sidebar-item compact">Cuisine & Gastronomie</div>
    </div>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="main-content">
    <!-- HEADER -->
    <header class="header">
      <h1>Rodrigue HESSOU</h1>
      <div class="subtitle">Équipier Polyvalent de Restauration Rapide — Job Étudiant (McDonald's Lyon)</div>
    </header>

    <!-- PROFIL -->
    <section class="main-section">
      <div class="main-section-title">Profil Professionnel</div>
      <p class="profile-text">
        Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, dynamique, rigoureux et résistant au stress, je recherche un poste d'<strong>Équipier Polyvalent de Restauration Rapide</strong>. Fort d'une expérience concrète du contact client et de la gestion de caisse en période de forte affluence (Supermarché Champion en 2024) ainsi que de la logistique à cadence soutenue (préparation de commandes en 2025), j'ai développé une grande réactivité et le goût du travail en équipe rythmée. Rigoureux sur les normes d'hygiène (HACCP) et doté d'un relationnel chaleureux, je souhaite m'investir pleinement au sein de votre restaurant afin d'offrir un service rapide, impeccable et convivial à chaque client.
      </p>
    </section>

    <!-- EXPÉRIENCES PROFESSIONNELLES -->
    <section class="main-section">
      <div class="main-section-title">Expériences Professionnelles</div>

      <!-- SUPERMARCHÉ CHAMPION -->
      <div class="experience-item">
        <div class="item-title">Employé Commercial & Polyvalent — Caisse & Gestion des Flux</div>
        <div class="item-subrow">
          <span>Supermarché Champion</span>
          <span>2024</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Encaissement en Pic de Rush :</strong> Enregistrement rapide et sans erreur des commandes en période de forte affluence ; tenue de caisse exacte et sens du sourire.</li>
          <li><strong>Accueil & Orientation Client :</strong> Prise en charge bienveillante, écoute active des demandes et gestion fluide des réclamations avec calme et courtoisie.</li>
          <li><strong>Entretien & Propreté :</strong> Maintien constant de la propreté des postes de travail et de l'espace de vente dans le respect des règles d'hygiène.</li>
          <li><strong>Travail d'Équipe & Entraide :</strong> Coordination avec les équipiers pour fluidifier le passage des clients et limiter le temps d'attente.</li>
        </ul>
      </div>

      <!-- PREPARATEUR LOGISTIQUE -->
      <div class="experience-item">
        <div class="item-title">Préparateur de Commandes — Cadence & Rigueur</div>
        <div class="item-subrow">
          <span>Plateforme Logistique & Distribution</span>
          <span>2025</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Respect des Cadences :</strong> Préparation et conditionnement minutieux de commandes à rythme soutenu tout en maintenant un niveau de qualité constant.</li>
          <li><strong>Hygiène & Sécurité :</strong> Application stricte des consignes de sécurité, de rangement et de manipulation des produits.</li>
          <li><strong>Endurance & Réactivité :</strong> Aptitude physique au travail dynamique debout et esprit de cohésion collective.</li>
        </ul>
      </div>

      <!-- NATAAN GROUP -->
      <div class="experience-item">
        <div class="item-title">Chargé de Prospection Commerciale & Déploiement POS</div>
        <div class="item-subrow">
          <span>Nataan Group (ESN)</span>
          <span>Juil. 2026 – Sept. 2026</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Relationnel Client Terrain :</strong> Contact direct avec <strong>100 commerçants et restaurateurs</strong> ; écoute de leurs besoins et présentation de solutions de caisse.</li>
          <li><strong>Rigueur Opérationnelle :</strong> Sens du détail, organisation des priorités et fiabilité dans l'exécution des missions.</li>
        </ul>
      </div>

      <!-- DAROLLO & ATANYS -->
      <div class="experience-item">
        <div class="item-title">Conseiller Utilisateurs & Sens du Service</div>
        <div class="item-subrow">
          <span>Darollo Technologies & ATANYS</span>
          <span>2025</span>
        </div>
        <ul class="item-bullets">
          <li>Écoute attentive, sens du service et volonté constante de satisfaire l'utilisateur final.</li>
        </ul>
      </div>
    </section>

    <!-- FORMATION -->
    <section class="main-section">
      <div class="main-section-title">Formation</div>
      <div class="formation-list">
        <div class="formation-item">
          <div class="formation-title">Master 1 en Informatique (Cursus Bac+5)</div>
          <div class="formation-subrow">
            <span>SUPINFO Lyon — Lyon, France</span>
            <span>Depuis Oct. 2026</span>
          </div>
        </div>

        <div class="formation-item">
          <div class="formation-title">Licence en Génie Logiciel</div>
          <div class="formation-subrow">
            <span>IAI-TOGO (Institut Africain d'Informatique)</span>
            <span>2022 – 2025</span>
          </div>
        </div>

        <div class="formation-item">
          <div class="formation-title">Baccalauréat (BAC 2)</div>
          <div class="formation-subrow">
            <span>LPL Le Rossignol</span>
            <span>2021 – 2022</span>
          </div>
        </div>
      </div>
    </section>

    <!-- COMPETENCES CLES RESTAURATION -->
    <section class="main-section">
      <div class="main-section-title">Compétences Clés Restauration Rapide</div>
      <div class="keywords-block">
        <div class="keyword-line">
          <strong>Service Client & Comptoir :</strong> Accueil chaleureux, prise de commande aux bornes/comptoir, encaissement rapide, service à table et Drive
        </div>
        <div class="keyword-line">
          <strong>Cuisine & Préparation :</strong> Assemblage sandwichs, cuisson/friture, garniture selon fiches techniques, respect des temps de conservation
        </div>
        <div class="keyword-line">
          <strong>Hygiène & Sécurité (HACCP) :</strong> Respect de la chaîne du chaud/froid, nettoyage méthodique des postes et de la salle, tri sélectif
        </div>
        <div class="keyword-line">
          <strong>Gestion du Rush & Collectif :</strong> Esprit d'équipe solidaire, rapidité d'exécution, gestion positive du stress, communication fluide
        </div>
        <div class="keyword-line">
          <strong>Disponibilité & Flexibilité :</strong> Adaptabilité immédiate aux plannings modulables (soirées, week-ends complets, fermetures)
        </div>
      </div>
    </section>
  </main>

</body>
</html>
"""

with open('CV_Rodrigue_HESSOU_Restauration_MacDo.html', 'w', encoding='utf-8') as f:
    f.write(cv_html)

# 2. LETTRE DE MOTIVATION MCDONALD'S
letter_html = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Lettre de Motivation - Rodrigue HESSOU - Équipier Polyvalent McDonald's</title>
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
        <div class="sender-subtitle">Candidat Équipier Polyvalent de Restauration — Job Étudiant</div>
        <div class="sender-detail">429 Cours Émile Zola</div>
        <div class="sender-detail">69100 Villeurbanne – Lyon</div>
        <div class="sender-detail">+33 7 44 11 75 73</div>
        <div class="sender-detail">rodriguehessou14@gmail.com</div>
      </div>

      <div class="recipient-card">
        <div class="recipient-name">MCDONALD'S FRANCE</div>
        <div class="recipient-detail">À l'attention de la Direction du Restaurant</div>
        <div class="recipient-detail">Restaurant McDonald's Lyon (Part-Dieu / Charpennes / Villeurbanne)</div>
        <div class="recipient-detail">Lyon, France</div>
      </div>
    </div>

    <!-- META: DATE & OBJET -->
    <div class="meta-block">
      <div class="date-line">À Lyon, le 22 octobre 2026</div>
      <div class="object-line">
        <strong>Objet :</strong> Candidature au poste d'Équipier Polyvalent de Restauration Rapide (Job Étudiant / Temps Partiel)
      </div>
    </div>

    <!-- CORPS DE LA LETTRE -->
    <div class="letter-content">
      <div class="salutation">Madame, Monsieur,</div>

      <p>
        Actuellement étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, je souhaite vivement rejoindre votre équipe en tant qu'<strong>Équipier Polyvalent au sein de votre restaurant McDonald's</strong>. Attiré par le dynamisme de votre enseigne, la rigueur de votre organisation et la qualité de votre service client, je souhaite mettre mon énergie, ma ponctualité et mon esprit d'équipe au service de votre activité quotidienne.
      </p>

      <p>
        Mes précédentes expériences m'ont permis d'acquérir une excellente réactivité sur le terrain. Lors de mon activité au <strong>Supermarché Champion en 2024</strong>, j'ai géré l'accueil et l'encaissement de nombreux clients durant les pics de forte affluence. Cette immersion m'a appris à exécuter les tâches avec rapidité et exactitude, tout en conservant un accueil souriant et courtois en toutes circonstances. J'y ai également développé une grande rigueur dans le maintien de la propreté et la tenue des postes de travail.
      </p>

      <p>
        Par ailleurs, mon travail en <strong>plateforme logistique en 2025</strong> a confirmé ma capacité à soutenir des cadences rapides et à appliquer scrupuleusement les consignes d'organisation et de sécurité. Polyvalent et doté d'une forte faculté d'adaptation, je suis prêt à intervenir sur tous les postes de votre restaurant : <strong>accueil au comptoir et aux bornes, préparation et assemblage des commandes en cuisine, service en salle et au Drive, ainsi qu'entretien régulier des équipements dans le respect strict des normes HACCP</strong>.
      </p>

      <p>
        Ce qui me motive chez McDonald's, c'est l'intensité du travail en équipe et l'engagement collectif pour satisfaire chaque visiteur en un temps record. Ponctuel, enthousiaste et communicatif, je m'intègre avec facilité et contribue à maintenir une ambiance de travail solidaire et motivante, même lors des rushs les plus intenses.
      </p>

      <p>
        Parfaitement conscient des exigences d'un contrat étudiant en restauration, je vous garantis une <strong>grande flexibilité horaire</strong> : je suis disponible en soirée (fermetures incluses), les week-ends complets ainsi que pendant toutes les vacances scolaires.
      </p>

      <p>
        Je serais très heureux de vous rencontrer à l'occasion d'un entretien pour vous démontrer ma motivation et mon envie de m'investir au sein de votre équipe. En vous remerciant de votre considération, je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.
      </p>
    </div>
  </div>

  <!-- CLOSING & SIGNATURE -->
  <div class="closing-block">
    <div class="signature-box">
      <div class="signature-name">Rodrigue HESSOU</div>
      <div class="signature-title">Candidat Équipier Polyvalent · McDonald's Lyon</div>
    </div>
  </div>

</body>
</html>
"""

with open('Lettre_de_Motivation_MacDo_Rodrigue_HESSOU.html', 'w', encoding='utf-8') as f:
    f.write(letter_html)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Build CV PDF
subprocess.run([
    chrome_path, "--headless", "--disable-gpu", "--no-pdf-header-footer",
    "--print-to-pdf=CV_Rodrigue_HESSOU_Restauration_MacDo.pdf",
    "CV_Rodrigue_HESSOU_Restauration_MacDo.html"
], check=True)

# Build Letter PDF
subprocess.run([
    chrome_path, "--headless", "--disable-gpu", "--no-pdf-header-footer",
    "--print-to-pdf=Lettre_de_Motivation_MacDo_Rodrigue_HESSOU.pdf",
    "Lettre_de_Motivation_MacDo_Rodrigue_HESSOU.html"
], check=True)

# Verify 1 page
doc1 = fitz.open("CV_Rodrigue_HESSOU_Restauration_MacDo.pdf")
doc2 = fitz.open("Lettre_de_Motivation_MacDo_Rodrigue_HESSOU.pdf")
print("CV MacDo page count:", len(doc1))
print("Letter MacDo page count:", len(doc2))
assert len(doc1) == 1
assert len(doc2) == 1
print("MACDONALD'S PERFECT 1-PAGE A4!")
