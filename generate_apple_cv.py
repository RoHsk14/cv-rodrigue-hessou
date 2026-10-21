import base64
import subprocess
import fitz

with open('photo.jpg', 'rb') as f:
    photo_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>CV - Rodrigue HESSOU - Spécialiste Apple Retail</title>
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

  /* LEFT SIDEBAR */
  .sidebar {{
    width: 63mm;
    background-color: #1f2937;
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

  /* RIGHT MAIN CONTENT */
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

  /* EXPERIENCES */
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

  /* FORMATION */
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

  /* KEY COMPETENCES */
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
        <strong>Job Étudiant (Rôle #114438069)</strong>
        Soirées, week-ends, vacances scolaires & plannings flexibles Apple Store
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
        Niveau B1/B2 — accueil et conseil d'une clientèle internationale
      </div>
    </div>

    <!-- COMPÉTENCES RELATIONNELLES & VENTE -->
    <div class="sidebar-section">
      <div class="sidebar-title">Atouts & Savoir-Être</div>
      <div class="sidebar-item">
        <strong>Sens du Service Client</strong>
        Accueil chaleureux, écoute active, découverte des besoins et personnalisation
      </div>
      <div class="sidebar-item">
        <strong>Esprit d'Équipe & Inclusion</strong>
        Entraide, communication positive, respect des diversités et curiosité
      </div>
      <div class="sidebar-item">
        <strong>Gestion du Rythme</strong>
        Aisance en environnement dynamique et gestion simultanée de plusieurs clients
      </div>
      <div class="sidebar-item">
        <strong>Passion Écosystème Apple</strong>
        iPhone, Mac, iPad, Apple Watch, iCloud, AppleCare, Apple Pay
      </div>
      <div class="sidebar-item">
        <strong>Rigueur & Confidentialité</strong>
        Exactitude en caisse, respect des consignes et protection des données
      </div>
    </div>

    <!-- QUALITÉS -->
    <div class="sidebar-section">
      <div class="sidebar-title">Qualités</div>
      <ul class="sidebar-list">
        <li>Empathie, sourire et relationnel facile</li>
        <li>Curiosité naturelle et envie d'apprendre</li>
        <li>Sens du détail et exigence de qualité</li>
        <li>Ponctualité, adaptabilité et proactivité</li>
      </ul>
    </div>

    <!-- CENTRES D'INTÉRÊT -->
    <div class="sidebar-section">
      <div class="sidebar-title">Centres d'intérêt</div>
      <div class="sidebar-item compact">Technologies & Écosystème Apple</div>
      <div class="sidebar-item compact">Football & Esprit d'équipe</div>
      <div class="sidebar-item compact">Musique & Créativité</div>
    </div>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="main-content">
    <!-- HEADER -->
    <header class="header">
      <h1>Rodrigue HESSOU</h1>
      <div class="subtitle">Spécialiste Apple Retail — Job Étudiant (Rôle #114438069)</div>
    </header>

    <!-- PROFIL -->
    <section class="main-section">
      <div class="main-section-title">Profil</div>
      <p class="profile-text">
        Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, doté d'un excellent sens relationnel et passionné par les produits et l'écosystème Apple. Fort d'expériences réussies dans le commerce de proximité, la préparation logistique et la prospection B2B, je sais écouter avec bienveillance, cerner les attentes réelles de chaque personne et délivrer une expérience client humaine et personnalisée. Dynamique, curieux et rigoureux, je m'adapte avec aisance au rythme soutenu d'un espace de vente tout en gardant le sens de l'accueil. Je souhaite mettre mon enthousiasme, mon esprit d'équipe et mon sens du service au cœur de l'Apple Store pour fidéliser la clientèle et faire rayonner la marque.
      </p>
    </section>

    <!-- EXPÉRIENCES PROFESSIONNELLES -->
    <section class="main-section">
      <div class="main-section-title">Expériences Professionnelles</div>

      <!-- SUPERMARCHÉ CHAMPION -->
      <div class="experience-item">
        <div class="item-title">Employé Commercial & Polyvalent — Vente & Relation Client</div>
        <div class="item-subrow">
          <span>Supermarché Champion</span>
          <span>2024</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Accueil & Orientation :</strong> Accueil chaleureux des visiteurs, orientation immédiate, écoute attentive et accompagnement personnalisé dans le magasin.</li>
          <li><strong>Gestion de Caisse & Affluence :</strong> Encaissement fluide et rapide lors des pics de forte affluence avec exactitude, rigueur et sourire.</li>
          <li><strong>Tenue de Rayon & Réassort :</strong> Mise en rayon quotidienne, contrôle des dates de péremption, agencement soigné et entretien irréprochable de l'espace commercial.</li>
          <li><strong>Travail d'Équipe :</strong> Entraide continue avec les collègues pour assurer la fluidité du point de vente et la satisfaction immédiate des clients.</li>
        </ul>
      </div>

      <!-- PRÉPARATEUR DE COMMANDES (2025) -->
      <div class="experience-item">
        <div class="item-title">Préparateur de Commandes & Relation Client</div>
        <div class="item-subrow">
          <span>Plateforme Logistique & Distribution</span>
          <span>2025</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Préparation & Rigueur :</strong> Préparation soignée et contrôle qualité des commandes clients dans le respect des délais et des standards d'excellence.</li>
          <li><strong>Organisation & Coordination :</strong> Planification des livraisons et suivi des expéditions pour garantir une ponctualité exemplaire.</li>
          <li><strong>Remise Client & Closing :</strong> Remise des commandes auprès des clients, closing, écoute des retours, fidélisation et résolution proactive des imprévus.</li>
        </ul>
      </div>

      <!-- NATAAN GROUP -->
      <div class="experience-item">
        <div class="item-title">Chargé de Prospection Commerciale & Déploiement Mobile</div>
        <div class="item-subrow">
          <span>Nataan Group (ESN) — Lomé, Togo</span>
          <span>Juil. 2026 – Sept. 2026</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Prospection B2B & Conseil :</strong> Qualification et accompagnement personnalisé de <strong>100 professionnels et commerçants</strong> ; écoute de leurs besoins et démonstration de solutions adaptées.</li>
          <li><strong>Application POS & Écosystème Apple :</strong> Co-développement d'une solution de boutique / POS ; conformité aux exigences d'ergonomie et de fluidité de l'écosystème <strong>Apple (iOS / App Store)</strong>.</li>
          <li><strong>Assurance Qualité & Service :</strong> Vérification minutieuse des parcours utilisateurs (103 cas de test) pour garantir une expérience fluide, intuitive et sans friction.</li>
          <li><strong>Archivage & Données Clients :</strong> Structuration et fiabilisation de données pour des comptes partenaires dans le strict respect de la confidentialité.</li>
        </ul>
      </div>

      <!-- DAROLLO & ATANYS -->
      <div class="experience-item">
        <div class="item-title">Conseiller Applicatif & Analyse des Besoins Utilisateurs</div>
        <div class="item-subrow">
          <span>Darollo Technologies & ATANYS</span>
          <span>2025</span>
        </div>
        <ul class="item-bullets">
          <li>Écoute et analyse des attentes des utilisateurs finaux pour concevoir des parcours simples, accessibles et intuitifs.</li>
          <li>Pédagogie et sens de la démonstration pour guider les utilisateurs dans la prise en main des outils numériques.</li>
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

    <!-- COMPÉTENCES CLÉS (MOTS-CLÉS) -->
    <section class="main-section">
      <div class="main-section-title">Compétences Clés pour Apple Retail</div>
      <div class="keywords-block">
        <div class="keyword-line">
          <strong>Relation Client & Vente :</strong> Accueil d'excellence, écoute active, découverte des besoins, conseil personnalisé, fidélisation, closing
        </div>
        <div class="keyword-line">
          <strong>Gestion d'Espace de Vente :</strong> Encaissement en pic d'affluence, réassort, mise en valeur des produits, rigueur de tenue de rayon
        </div>
        <div class="keyword-line">
          <strong>Écosystème & Produits Apple :</strong> Prise en main iPhone, iPad, Mac, Apple Watch, AirPods, services iOS/macOS, iCloud, AppleCare
        </div>
        <div class="keyword-line">
          <strong>Valeurs & Esprit d'Équipe :</strong> Entraide, communication bienveillante, respect de l'inclusion et de la diversité, intelligence relationnelle
        </div>
        <div class="keyword-line">
          <strong>Organisation & Flexibilité :</strong> Disponibilité soirs et week-ends, ponctualité, adaptabilité à un flux client élevé, autonomie
        </div>
      </div>
    </section>
  </main>

</body>
</html>
"""

with open('CV_Rodrigue_HESSOU_Apple_Retail.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("CV_Rodrigue_HESSOU_Apple_Retail.html updated with Role number and 2025!")
