import base64
import subprocess
import fitz

with open('photo.jpg', 'rb') as f:
    photo_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>CV - Rodrigue HESSOU - Vendeur Polyvalent & Employé Commercial</title>
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
    padding: 7mm 7.5mm 7mm 7.5mm;
    display: flex;
    flex-direction: row;
    gap: 5mm;
    overflow: hidden;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  /* LEFT SIDEBAR */
  .sidebar {{
    width: 63mm;
    background-color: #1e293b;
    border-radius: 4px;
    padding: 4.5mm 4.2mm;
    color: #f1f5f9;
    display: flex;
    flex-direction: column;
    gap: 3.2mm;
    flex-shrink: 0;
  }}

  .photo-container {{
    text-align: center;
    margin-bottom: 0.1mm;
  }}

  .photo {{
    width: 37mm;
    height: 47mm;
    object-fit: cover;
    border-radius: 5px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    display: block;
    margin: 0 auto;
  }}

  .sidebar-section {{
    display: flex;
    flex-direction: column;
    gap: 1.1mm;
  }}

  .sidebar-title {{
    font-size: 9.6pt;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    padding-bottom: 0.5mm;
    border-bottom: 1px solid #5b7fa6;
    margin-bottom: 0.5mm;
  }}

  .sidebar-item {{
    font-size: 8.2pt;
    line-height: 1.23;
    color: #cbd5e1;
  }}

  .sidebar-item strong {{
    color: #ffffff;
    font-weight: 700;
    display: block;
    font-size: 8.4pt;
  }}

  .sidebar-item.compact {{
    line-height: 1.2;
  }}

  .sidebar-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 1mm;
  }}

  .sidebar-list li {{
    font-size: 8.15pt;
    line-height: 1.2;
    color: #cbd5e1;
    position: relative;
    padding-left: 3.2mm;
  }}

  .sidebar-list li::before {{
    content: "•";
    position: absolute;
    left: 0;
    color: #94a3b8;
    font-size: 8.8pt;
    line-height: 1;
  }}

  /* RIGHT MAIN CONTENT */
  .main-content {{
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 2.5mm;
    min-width: 0;
  }}

  .header {{
    margin-top: 0.1mm;
    margin-bottom: 0.1mm;
  }}

  .header h1 {{
    font-size: 20pt;
    font-weight: 700;
    color: #1e293b;
    line-height: 1.1;
    letter-spacing: -0.3px;
  }}

  .header .subtitle {{
    font-size: 10.8pt;
    font-weight: 700;
    color: #2e75b6;
    margin-top: 0.5mm;
  }}

  .main-section {{
    display: flex;
    flex-direction: column;
    gap: 1.3mm;
  }}

  .main-section-title {{
    font-size: 10.2pt;
    font-weight: 700;
    color: #2e75b6;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    padding-bottom: 0.5mm;
    border-bottom: 1.5px solid #2e75b6;
  }}

  .profile-text {{
    font-size: 8.25pt;
    line-height: 1.28;
    color: #262626;
    text-align: justify;
  }}

  /* EXPERIENCES */
  .experience-item {{
    display: flex;
    flex-direction: column;
    gap: 0.4mm;
  }}

  .item-title {{
    font-size: 8.9pt;
    font-weight: 700;
    color: #262626;
  }}

  .item-subrow {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.1pt;
    font-style: italic;
    color: #595959;
  }}

  .item-bullets {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.45mm;
    margin-top: 0.15mm;
  }}

  .item-bullets li {{
    font-size: 8.05pt;
    line-height: 1.2;
    color: #262626;
    position: relative;
    padding-left: 3.2mm;
    text-align: justify;
  }}

  .item-bullets li::before {{
    content: "•";
    position: absolute;
    left: 0;
    color: #2e75b6;
    font-size: 8.6pt;
    line-height: 1.1;
  }}

  /* FORMATION */
  .formation-list {{
    display: flex;
    flex-direction: column;
    gap: 1mm;
  }}

  .formation-item {{
    display: flex;
    flex-direction: column;
    gap: 0.2mm;
  }}

  .formation-title {{
    font-size: 8.8pt;
    font-weight: 700;
    color: #262626;
  }}

  .formation-subrow {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8pt;
    font-style: italic;
    color: #595959;
  }}

  /* KEY COMPETENCES */
  .keywords-block {{
    display: flex;
    flex-direction: column;
    gap: 0.6mm;
  }}

  .keyword-line {{
    font-size: 8.05pt;
    line-height: 1.2;
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
      <div class="sidebar-item">Né le 14/03/2006 (20 ans)</div>
    </div>

    <!-- DISPONIBILITÉS -->
    <div class="sidebar-section">
      <div class="sidebar-title">Disponibilités</div>
      <div class="sidebar-item">
        <strong>Rythme Fixe (Semestre Garanti)</strong>
        - <strong>1 sem. sur 2 :</strong> 100% disponible (Lun à Dim, matins/journées/soirs, 35H)<br>
        - <strong>Semaines de cours :</strong> Vendredi soirs, Samedis et Dimanches complets<br>
        - Opérationnel immédiatement pour contrat étudiant, mi-temps ou intérim
      </div>
    </div>

    <!-- LANGUES -->
    <div class="sidebar-section">
      <div class="sidebar-title">Langues</div>
      <div class="sidebar-item">
        <strong>Français</strong>
        Langue maternelle — élocution soignée, écoute et politesse
      </div>
      <div class="sidebar-item">
        <strong>Anglais</strong>
        Niveau B1/B2 — accueil et orientation d'une clientèle internationale
      </div>
    </div>

    <!-- SAVOIR-ÊTRE RETAIL -->
    <div class="sidebar-section">
      <div class="sidebar-title">Savoir-Être Retail</div>
      <div class="sidebar-item">
        <strong>Accueil & Sens du Service</strong>
        Sourire constant, politesse, écoute active et orientation client
      </div>
      <div class="sidebar-item">
        <strong>Caisse & Fiabilité</strong>
        Encaissement rapide, rigueur des comptes et gestion de l'affluence
      </div>
      <div class="sidebar-item">
        <strong>Mise en Rayon & Merchandising</strong>
        Réassort soigné, facing impeccable, contrôle des dates et étiquetage
      </div>
      <div class="sidebar-item">
        <strong>Dynamisme & Esprit d'Équipe</strong>
        Polyvalence, entraide permanente et respect des consignes
      </div>
      <div class="sidebar-item">
        <strong>Endurance & Ponctualité</strong>
        Résistance au port de charges, travail debout et assiduité exemplaire
      </div>
    </div>

    <!-- QUALITÉS -->
    <div class="sidebar-section">
      <div class="sidebar-title">Qualités</div>
      <ul class="sidebar-list">
        <li>Sourire, sens du contact et relationnel facile</li>
        <li>Excellente endurance et sang-froid aux heures de rush</li>
        <li>Rigueur, honnêteté et propreté de travail</li>
        <li>Ponctualité stricte et adaptabilité rapide</li>
      </ul>
    </div>

    <!-- CENTRES D'INTÉRÊT -->
    <div class="sidebar-section">
      <div class="sidebar-title">Centres d'intérêt</div>
      <div class="sidebar-item compact">Sport & Football (esprit d'équipe, discipline)</div>
      <div class="sidebar-item compact">Commerce de détail & relation client</div>
      <div class="sidebar-item compact">Outils digitaux & nouvelles technologies</div>
    </div>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="main-content">
    <!-- HEADER -->
    <header class="header">
      <h1>Rodrigue HESSOU</h1>
      <div class="subtitle">Vendeur Polyvalent & Employé Commercial — Job Étudiant (Temps Partiel / Intérim)</div>
    </header>

    <!-- PROFIL -->
    <section class="main-section">
      <div class="main-section-title">Profil & Engagement</div>
      <p class="profile-text">
        Étudiant à <strong>SUPINFO Lyon</strong> avec un <strong>calendrier semestriel fixe (1 semaine sur 2 libre à 100% du lundi au dimanche + week-ends réguliers)</strong>, je recherche un poste d'<strong>Employé Commercial / Vendeur Polyvalent</strong> pour l'ensemble de l'année universitaire. Fort d'expériences concrètes sur le terrain en magasin (caisse, réassort, facing) et en logistique (préparation de commandes à cadence soutenue), je suis immédiatement opérationnel. Dynamique, ponctuel et doté d'un excellent sens du service client, je garde mon sang-froid en pic d'affluence et m'investis avec rigueur pour assurer la bonne tenue des rayons, la fluidité des encaissements et la satisfaction de chaque visiteur.
      </p>
    </section>

    <!-- EXPÉRIENCES PROFESSIONNELLES -->
    <section class="main-section">
      <div class="main-section-title">Expériences Professionnelles</div>

      <!-- SUPERMARCHÉ CHAMPION -->
      <div class="experience-item">
        <div class="item-title">Employé Commercial Polyvalent — Caisse, Rayon & Service Client</div>
        <div class="item-subrow">
          <span>Supermarché Champion</span>
          <span>2024</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Accueil & Renseignement :</strong> Accueil chaleureux des clients, orientation précise dans les rayons, écoute attentive et réponse aux demandes avec le sourire.</li>
          <li><strong>Tenue de Caisse & Encaissement :</strong> Encaissement rapide et fiable (espèces, CB), fluidification active des files d'attente en heures de pointe et exactitude des comptes.</li>
          <li><strong>Mise en Rayon & Merchandising :</strong> Réassort quotidien des linéaires, facing impeccable, contrôle rigoureux du balisage des prix et respect des dates de péremption (FIFO).</li>
          <li><strong>Tenue du Magasin :</strong> Maintien d'une zone de vente propre et ordonnée, réception des livraisons et polyvalence constante en renfort d'équipe.</li>
        </ul>
      </div>

      <!-- PLATEFORME LOGISTIQUE -->
      <div class="experience-item">
        <div class="item-title">Préparateur de Commandes & Logistique de Réassort</div>
        <div class="item-subrow">
          <span>Plateforme Logistique & Distribution</span>
          <span>2025</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Réception & Rangement :</strong> Déchargement des arrivages, contrôle de conformité des colis et mise en stock méthodique en réserve.</li>
          <li><strong>Préparation & Cadence :</strong> Prélèvement précis des références en stock, conditionnement soigné des commandes et respect strict des cadences et normes de sécurité.</li>
          <li><strong>Endurance & Rigueur :</strong> Excellente résistance physique au port de charges, travail debout prolongé et efficacité en rythme soutenu.</li>
        </ul>
      </div>

      <!-- NATAAN GROUP -->
      <div class="experience-item">
        <div class="item-title">Conseiller Commercial & Déploiement Systèmes de Caisse de Proximité</div>
        <div class="item-subrow">
          <span>Nataan Group — Lomé, Togo</span>
          <span>Juil. 2026 – Sept. 2026</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Accompagnement Commerçants :</strong> Formation et accompagnement direct de <strong>100 commerçants de proximité</strong> sur des logiciels de caisse et de gestion des stocks.</li>
          <li><strong>Sens du Commerce Terrain :</strong> Écoute des besoins quotidiens des vendeurs (rapidité d'encaissement, suivi des ventes, réassort) et apport d'assistance réactive.</li>
          <li><strong>Fluidité de Service :</strong> Optimisation des gestes d'encaissement pour garantir un passage en caisse rapide et sans erreur.</li>
        </ul>
      </div>

      <!-- DAROLLO & ATANYS -->
      <div class="experience-item">
        <div class="item-title">Conseiller Relation Utilisateurs & Service Client</div>
        <div class="item-subrow">
          <span>Darollo Technologies & ATANYS</span>
          <span>2025</span>
        </div>
        <ul class="item-bullets">
          <li>Accueil, écoute empathique, diagnostic précis des demandes et apport de solutions personnalisées.</li>
          <li>Sens de la pédagogie, politesse constante et engagement quotidien pour la satisfaction client.</li>
        </ul>
      </div>
    </section>

    <!-- FORMATION -->
    <section class="main-section">
      <div class="main-section-title">Formation</div>
      <div class="formation-list">
        <div class="formation-item">
          <div class="formation-title">Master 1 en Informatique (Rythme alterné : 1 sem. cours / 1 sem. libre)</div>
          <div class="formation-subrow">
            <span>SUPINFO Lyon — Lyon, France</span>
            <span>Depuis Oct. 2026</span>
          </div>
        </div>

        <div class="formation-item">
          <div class="formation-title">Licence en Informatique / Génie Logiciel</div>
          <div class="formation-subrow">
            <span>IAI (Institut Africain d'Informatique)</span>
            <span>2022 – 2025</span>
          </div>
        </div>

        <div class="formation-item">
          <div class="formation-title">Baccalauréat</div>
          <div class="formation-subrow">
            <span>LPL Le Rossignol</span>
            <span>2021 – 2022</span>
          </div>
        </div>
      </div>
    </section>

    <!-- COMPÉTENCES CLÉS RETAIL -->
    <section class="main-section">
      <div class="main-section-title">Compétences Clés & Savoir-Faire Magasin</div>
      <div class="keywords-block">
        <div class="keyword-line">
          <strong>Relation Client & Service :</strong> Accueil souriant, écoute active, politesse, orientation en rayon, fidélisation et gestion bienveillante des retours
        </div>
        <div class="keyword-line">
          <strong>Caisse & Encaissement :</strong> Encaissement rapide et fiable, ouverture/fermeture de caisse, fluidification des files en forte affluence
        </div>
        <div class="keyword-line">
          <strong>Mise en Rayon & Merchandising :</strong> Réassort quotidien, facing soigné, contrôle rigoureux du balisage et rotation des dates (FIFO)
        </div>
        <div class="keyword-line">
          <strong>Manutention & Logistique :</strong> Déchargement de palettes, port de charges, rangement de réserve, préparation de commandes et consignes de sécurité
        </div>
        <div class="keyword-line">
          <strong>Stabilité & Disponibilité :</strong> Calendrier semestriel garanti (1 sem./2 libre à 35H + week-ends), ponctualité stricte et dynamisme d'équipe
        </div>
      </div>
    </section>
  </main>

</body>
</html>
"""

with open('CV_Rodrigue_HESSOU_Retail_Polyvalent.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("CV_Rodrigue_HESSOU_Retail_Polyvalent.html written!")

# Generate PDF with Google Chrome
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
pdf_path = "CV_Rodrigue_HESSOU_Retail_Polyvalent.pdf"

cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    "CV_Rodrigue_HESSOU_Retail_Polyvalent.html"
]

subprocess.run(cmd, check=True)
print(f"PDF generated: {pdf_path}")

doc = fitz.open(pdf_path)
page_count = len(doc)
print(f"Page count: {page_count}")
assert page_count == 1, f"Expected 1 page, got {page_count}"

# Generate preview PNG
page = doc[0]
pix = page.get_pixmap(dpi=150)
preview_path = "CV_Rodrigue_HESSOU_Retail_Polyvalent_preview.png"
pix.save(preview_path)
print(f"Preview image saved: {preview_path}")
