import os
import base64
import subprocess
import fitz

# Read photo
with open('photo.jpg', 'rb') as f:
    photo_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>CV - Rodrigue HESSOU</title>
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
    padding: 8.5mm 8.5mm 8.5mm 8.5mm;
    display: flex;
    flex-direction: row;
    gap: 6mm;
    overflow: hidden;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  /* LEFT SIDEBAR */
  .sidebar {{
    width: 63mm;
    background-color: #1f2937;
    border-radius: 4px;
    padding: 5.5mm 5mm;
    color: #f1f5f9;
    display: flex;
    flex-direction: column;
    gap: 4.2mm;
    flex-shrink: 0;
  }}

  .photo-container {{
    text-align: center;
    margin-bottom: 0.5mm;
  }}

  .photo {{
    width: 39mm;
    height: 51mm;
    object-fit: cover;
    border-radius: 5px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    display: block;
    margin: 0 auto;
  }}

  .sidebar-section {{
    display: flex;
    flex-direction: column;
    gap: 1.4mm;
  }}

  .sidebar-title {{
    font-size: 10pt;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    padding-bottom: 0.8mm;
    border-bottom: 1px solid #5b7fa6;
    margin-bottom: 0.8mm;
  }}

  .sidebar-item {{
    font-size: 8.4pt;
    line-height: 1.28;
    color: #cbd5e1;
  }}

  .sidebar-item strong {{
    color: #ffffff;
    font-weight: 700;
    display: block;
    font-size: 8.6pt;
  }}

  .sidebar-item.compact {{
    line-height: 1.25;
  }}

  .sidebar-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 1.2mm;
  }}

  .sidebar-list li {{
    font-size: 8.4pt;
    line-height: 1.24;
    color: #cbd5e1;
    position: relative;
    padding-left: 3.5mm;
  }}

  .sidebar-list li::before {{
    content: "•";
    position: absolute;
    left: 0;
    color: #60a5fa;
    font-size: 9.5pt;
    line-height: 1;
  }}

  /* RIGHT MAIN CONTENT */
  .main-content {{
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 3.2mm;
    min-width: 0;
  }}

  .header {{
    margin-top: 0.5mm;
    margin-bottom: 0.5mm;
  }}

  .header h1 {{
    font-size: 21pt;
    font-weight: 700;
    color: #1e293b;
    line-height: 1.1;
    letter-spacing: -0.3px;
  }}

  .header .subtitle {{
    font-size: 11.5pt;
    font-weight: 700;
    color: #2e75b6;
    margin-top: 0.8mm;
  }}

  .main-section {{
    display: flex;
    flex-direction: column;
    gap: 1.8mm;
  }}

  .main-section-title {{
    font-size: 10.8pt;
    font-weight: 700;
    color: #2e75b6;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    padding-bottom: 0.7mm;
    border-bottom: 1.5px solid #2e75b6;
  }}

  .profile-text {{
    font-size: 8.5pt;
    line-height: 1.34;
    color: #262626;
    text-align: justify;
  }}

  /* EXPERIENCES */
  .experience-item {{
    display: flex;
    flex-direction: column;
    gap: 0.7mm;
  }}

  .item-title {{
    font-size: 9.2pt;
    font-weight: 700;
    color: #262626;
  }}

  .item-subrow {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.3pt;
    font-style: italic;
    color: #595959;
  }}

  .item-bullets {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.6mm;
    margin-top: 0.2mm;
  }}

  .item-bullets li {{
    font-size: 8.25pt;
    line-height: 1.25;
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
    font-size: 9pt;
    line-height: 1.1;
  }}

  /* FORMATION */
  .formation-list {{
    display: flex;
    flex-direction: column;
    gap: 1.5mm;
  }}

  .formation-item {{
    display: flex;
    flex-direction: column;
    gap: 0.3mm;
  }}

  .formation-title {{
    font-size: 9.1pt;
    font-weight: 700;
    color: #262626;
  }}

  .formation-subrow {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.3pt;
    font-style: italic;
    color: #595959;
  }}

  /* KEY COMPETENCES */
  .keywords-block {{
    display: flex;
    flex-direction: column;
    gap: 0.9mm;
  }}

  .keyword-line {{
    font-size: 8.25pt;
    line-height: 1.25;
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

    <!-- LANGUES -->
    <div class="sidebar-section">
      <div class="sidebar-title">Langues</div>
      <div class="sidebar-item">
        <strong>Français</strong>
        Langue maternelle — courant
      </div>
      <div class="sidebar-item">
        <strong>Anglais</strong>
        Niveau B1 — intermédiaire
      </div>
    </div>

    <!-- COMPÉTENCES TECHNIQUES -->
    <div class="sidebar-section">
      <div class="sidebar-title">Compétences Techniques</div>
      <div class="sidebar-item">
        <strong>Développement Mobile</strong>
        Flutter, Dart, Firebase, iOS (App Store Connect, APNs, OTP), Mode hors ligne
      </div>
      <div class="sidebar-item">
        <strong>Développement Web</strong>
        Django, Laravel, PHP, Python, JavaScript, HTML5/CSS3, Audit UI/UX
      </div>
      <div class="sidebar-item">
        <strong>BaaS, API & Paiement</strong>
        Firebase (Auth, Firestore), FedaPay, REST APIs, Notifications APNs
      </div>
      <div class="sidebar-item">
        <strong>Assurance Qualité (QA)</strong>
        Recette fonctionnelle, cahiers de tests (100+ cas), conformité Apple
      </div>
      <div class="sidebar-item">
        <strong>Bases de données</strong>
        MySQL, PostgreSQL, MariaDB, modélisation relationnelle SQL
      </div>
      <div class="sidebar-item">
        <strong>Méthodologie & Business</strong>
        Git/GitHub, Agile/Scrum, Prospection B2B, Archivage client
      </div>
    </div>

    <!-- QUALITÉS -->
    <div class="sidebar-section">
      <div class="sidebar-title">Qualités</div>
      <ul class="sidebar-list">
        <li>Travail en équipe et collaboration</li>
        <li>Rigueur, autonomie et organisation</li>
        <li>Sens du détail et de la qualité (QA)</li>
        <li>Capacité d'adaptation et proactivité</li>
      </ul>
    </div>

    <!-- CENTRES D'INTÉRÊT -->
    <div class="sidebar-section">
      <div class="sidebar-title">Centres d'intérêt</div>
      <div class="sidebar-item compact">Football</div>
      <div class="sidebar-item compact">Musique</div>
      <div class="sidebar-item compact">Veille technologique & UI/UX</div>
    </div>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="main-content">
    <!-- HEADER -->
    <header class="header">
      <h1>Rodrigue HESSOU</h1>
      <div class="subtitle">Développeur Logiciel — Web & Mobile</div>
    </header>

    <!-- PROFIL -->
    <section class="main-section">
      <div class="main-section-title">Profil</div>
      <p class="profile-text">
        Actuellement étudiant en <strong>Master à SUPINFO Lyon</strong> et titulaire d'une <strong>Licence en Génie Logiciel</strong> (IAI-TOGO), je dispose d'une solide expertise pratique en développement web et mobile (Flutter, iOS, Django, Laravel), en assurance qualité logicielle (QA) et en gestion de bases de données. Mes expériences en ESN et en entreprise m'ont permis d'intervenir sur l'ensemble du cycle de vie des applications : conception, développement hors ligne avec synchronisation, intégration de passerelles de paiement (FedaPay), recette fonctionnelle et publication sur l'App Store (App Store Connect). Rigoureux et adaptable, je recherche une opportunité (stage ou alternance) à Lyon pour mettre mes compétences au service de projets innovants.
      </p>
    </section>

    <!-- EXPÉRIENCES PROFESSIONNELLES -->
    <section class="main-section">
      <div class="main-section-title">Expériences Professionnelles</div>

      <!-- NATAN GROUP -->
      <div class="experience-item">
        <div class="item-title">Stagiaire — Développement Mobile, QA & Business Development</div>
        <div class="item-subrow">
          <span>Nataan Group (ESN) — Lomé, Togo</span>
          <span>Juil. 2026 – Sept. 2026</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Application BoutiK :</strong> Co-développement d'une application mobile de gestion de boutique / POS sous <strong>Flutter</strong>, connectée à <strong>Firebase</strong> et intégrant la passerelle de paiement <strong>FedaPay</strong>.</li>
          <li><strong>Portage & Release iOS :</strong> Portage iOS, mise en conformité avec les guidelines Apple, gestion de l'authentification OTP, push notifications <strong>APNs</strong> et publication en production via <strong>App Store Connect</strong>.</li>
          <li><strong>Assurance Qualité & Web :</strong> Conduite de la recette fonctionnelle complète d'un site institutionnel (exécution de <strong>103 cas de test</strong>), audit ergonomique UI/UX et refonte web.</li>
          <li><strong>Business Development & Données :</strong> Prospection commerciale B2B qualifiée (<strong>100 prospects ciblés</strong>) et réalisation de prestations d'archivage client.</li>
        </ul>
      </div>

      <!-- ATANYS -->
      <div class="experience-item">
        <div class="item-title">Stagiaire en Développement Web</div>
        <div class="item-subrow">
          <span>ATANYS — Lomé, Togo</span>
          <span>Sept. 2025 – Déc. 2025</span>
        </div>
        <ul class="item-bullets">
          <li>Conception et développement d'une plateforme web de gestion et de signalement des objets perdus et retrouvés.</li>
          <li>Participation à l'ensemble du cycle de développement : analyse des besoins, modélisation de la base de données, développement et tests.</li>
        </ul>
      </div>

      <!-- DAROLLO -->
      <div class="experience-item">
        <div class="item-title">Stagiaire en Développement d'Applications</div>
        <div class="item-subrow">
          <span>Darollo Technologies Corporation — Lomé, Togo</span>
          <span>Juil. 2025 – Août 2025</span>
        </div>
        <ul class="item-bullets">
          <li>Développement d'une application mobile Flutter dédiée aux tailleurs pour la gestion de leur activité (prise de mesures, suivi des commandes, notifications de livraison).</li>
          <li>Implémentation du fonctionnement hors ligne avec synchronisation automatique des données dès rétablissement de la connexion internet.</li>
        </ul>
      </div>

      <!-- ONG-CRISTO -->
      <div class="experience-item">
        <div class="item-title">Stagiaire en Gestion de Données</div>
        <div class="item-subrow">
          <span>ONG-CRISTO — Lomé, Togo</span>
          <span>Juil. 2024 – Sept. 2024</span>
        </div>
        <ul class="item-bullets">
          <li>Mise en place d'un système de gestion automatisée de la collecte d'informations pour un cabinet de recherche.</li>
          <li>Structuration et fiabilisation des données collectées sur le terrain.</li>
        </ul>
      </div>
    </section>

    <!-- FORMATION -->
    <section class="main-section">
      <div class="main-section-title">Formation</div>
      <div class="formation-list">
        <div class="formation-item">
          <div class="formation-title">Master en Informatique / Génie Logiciel</div>
          <div class="formation-subrow">
            <span>SUPINFO Lyon — Lyon, France</span>
            <span>Depuis Oct. 2026</span>
          </div>
        </div>

        <div class="formation-item">
          <div class="formation-title">Licence en Génie Logiciel</div>
          <div class="formation-subrow">
            <span>IAI-TOGO (Institut Africain d'Informatique) — Lomé, Togo</span>
            <span>Nov. 2022 – Déc. 2025</span>
          </div>
        </div>

        <div class="formation-item">
          <div class="formation-title">Baccalauréat (BAC 2)</div>
          <div class="formation-subrow">
            <span>LPL Le Rossignol — Lomé, Togo</span>
            <span>Sept. 2021 – Juin 2022</span>
          </div>
        </div>
      </div>
    </section>

    <!-- COMPÉTENCES CLÉS (MOTS-CLÉS) -->
    <section class="main-section">
      <div class="main-section-title">Compétences Clés (Mots-clés)</div>
      <div class="keywords-block">
        <div class="keyword-line">
          <strong>Langages & Frameworks :</strong> Flutter, Dart, Django, Laravel, PHP, Python, HTML, CSS, JavaScript
        </div>
        <div class="keyword-line">
          <strong>Développement mobile & Cloud :</strong> iOS (App Store Connect, APNs), Android, Flutter, Firebase, FedaPay, offline-first, synchronisation
        </div>
        <div class="keyword-line">
          <strong>QA, Audit & Web :</strong> Recette fonctionnelle (103 cas de test), audit UI/UX, refonte web, conformité logicielle
        </div>
        <div class="keyword-line">
          <strong>Bases de données :</strong> MySQL, PostgreSQL, MariaDB, Firebase Firestore, modélisation de données, SQL
        </div>
        <div class="keyword-line">
          <strong>Sécurité & Gestion :</strong> Sécurité informatique, gestion de projet logiciel, méthodes agiles, prospection B2B, travail en équipe
        </div>
      </div>
    </section>
  </main>

</body>
</html>
"""

with open('CV_Rodrigue_HESSOU.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("CV_Rodrigue_HESSOU.html written successfully!")
