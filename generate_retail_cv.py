import base64
import subprocess
import fitz

with open('photo.jpg', 'rb') as f:
    photo_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>CV - Rodrigue HESSOU - Conseiller de Vente & Vendeur Polyvalent</title>
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
        <strong>Vente & Relation Client</strong>
        Disponible immédiatement · Adaptabilité horaire (soirées, week-ends, 35H ou temps partiel)
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
        Niveau B1/B2 — accueil et conseil d'une clientèle internationale
      </div>
    </div>

    <!-- ATOUTS & SAVOIR-ÊTRE RETAIL -->
    <div class="sidebar-section">
      <div class="sidebar-title">Atouts & Savoir-Être</div>
      <div class="sidebar-item">
        <strong>Sens du Service & Conseil</strong>
        Accueil chaleureux, écoute active, découverte des besoins et personnalisation
      </div>
      <div class="sidebar-item">
        <strong>Performance & KPIs Retail</strong>
        Sensibilisation aux objectifs : panier moyen, taux de transformation, fidélisation
      </div>
      <div class="sidebar-item">
        <strong>Dynamisme & Esprit d'Équipe</strong>
        Entraide permanente, optimisme, curiosité et respect de la diversité & inclusion
      </div>
      <div class="sidebar-item">
        <strong>Gestion du Rythme & Affluence</strong>
        Sang-froid en pic d'activité, polyvalence caisse, conseil et réassort
      </div>
      <div class="sidebar-item">
        <strong>Rigueur & Tenue du Magasin</strong>
        Encaissement exact, respect du merchandising et tenue irréprochable des zones
      </div>
    </div>

    <!-- QUALITÉS -->
    <div class="sidebar-section">
      <div class="sidebar-title">Qualités</div>
      <ul class="sidebar-list">
        <li>Sourire, enthousiasme et relationnel naturel</li>
        <li>Ambassadeur de marque engagé et proactif</li>
        <li>Sens du détail et exigence d'excellence</li>
        <li>Ponctualité, résilience et esprit d'apprentissage</li>
      </ul>
    </div>

    <!-- CENTRES D'INTÉRÊT -->
    <div class="sidebar-section">
      <div class="sidebar-title">Centres d'intérêt</div>
      <div class="sidebar-item compact">Sport, Football & Esprit d'équipe</div>
      <div class="sidebar-item compact">Mode, Lifestyle & Tendances</div>
      <div class="sidebar-item compact">Nouvelles technologies & Innovation</div>
    </div>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="main-content">
    <!-- HEADER -->
    <header class="header">
      <h1>Rodrigue HESSOU</h1>
      <div class="subtitle">Conseiller de Vente & Relation Client — Vendeur Polyvalent</div>
    </header>

    <!-- PROFIL -->
    <section class="main-section">
      <div class="main-section-title">Profil Professionnel</div>
      <p class="profile-text">
        Étudiant en <strong>Master 1 à SUPINFO Lyon</strong>, doté d'une excellente énergie relationnelle et passionné par le contact humain et le commerce de détail. Fort d'expériences concrètes dans le commerce en magasin, la logistique de distribution et la prospection terrain, je maîtrise l'ensemble des étapes de l'acte de vente : accueil personnalisé, identification fine des attentes, conseil produit sur-mesure, gestion fluide de la caisse et fidélisation. Dynamique, curieux et résilient, je m'épanouis dans les environnements rythmés et valorise l'esprit d'équipe, l'inclusion et le dépassement de soi. Je souhaite m'investir pleinement comme ambassadeur de votre marque afin de délivrer une expérience client mémorable et contribuer aux objectifs commerciaux du magasin.
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
          <li><strong>Accueil & Conseil Client :</strong> Accueil personnalisé des visiteurs, écoute attentive des besoins, orientation immédiate et valorisation des offres du magasin.</li>
          <li><strong>Encaissement & Gestion d'Affluence :</strong> Gestion rapide et rigoureuse des encaissements lors des pics de forte affluence ; fidélisation et gestion bienveillante des réclamations.</li>
          <li><strong>Tenue de Rayon & Merchandising :</strong> Réassort quotidien, respect des standards de facing et de propreté, contrôle minutieux des stocks et des dates de péremption.</li>
          <li><strong>Travail d'Équipe & Polyvalence :</strong> Entraide active avec l'équipe pour garantir la fluidité opérationnelle et la satisfaction totale de chaque client.</li>
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
          <li><strong>Rigueur Opérationnelle :</strong> Réception, contrôle conformité, préparation minutieuse et emballage des commandes selon les normes d'exigence et de sécurité.</li>
          <li><strong>Gestion des Flux & Cadence :</strong> Coordination des flux de marchandises et respect strict des délais de livraison dans un environnement à haut rythme.</li>
          <li><strong>Remise Client & Closing :</strong> Remise soignée des commandes aux clients, écoute des retours, résolution proactive des imprévus et fidélisation.</li>
        </ul>
      </div>

      <!-- NATAAN GROUP -->
      <div class="experience-item">
        <div class="item-title">Chargé de Prospection Commerciale & Déploiement POS</div>
        <div class="item-subrow">
          <span>Nataan Group (ESN) — Lomé, Togo</span>
          <span>Juil. 2026 – Sept. 2026</span>
        </div>
        <ul class="item-bullets">
          <li><strong>Développement Commercial B2B :</strong> Prospection directe et qualification approfondie de <strong>100 commerçants et professionnels</strong> de proximité ; démonstration de valeur et closing d'offres.</li>
          <li><strong>Solution d'Encaissement & Retail :</strong> Déploiement de l'application de caisse/point de vente <em>BoutiK</em> ; accompagnement des commerçants sur la gestion des encaissements et le suivi des stocks.</li>
          <li><strong>Sensibilisation aux KPIs Retail :</strong> Analyse des leviers de vente (panier moyen, fréquence d'achat, rapidité d'encaissement) et optimisation des parcours clients.</li>
          <li><strong>Service & Qualité :</strong> Écoute active des retours utilisateurs (103 tests fonctionnels exécutés) pour assurer une satisfaction et une adoption optimales.</li>
        </ul>
      </div>

      <!-- DAROLLO & ATANYS -->
      <div class="experience-item">
        <div class="item-title">Conseiller Utilisateurs & Analyse des Besoins</div>
        <div class="item-subrow">
          <span>Darollo Technologies & ATANYS</span>
          <span>2025</span>
        </div>
        <ul class="item-bullets">
          <li>Écoute empathique, diagnostic précis des attentes utilisateurs et formulation de recommandations adaptées.</li>
          <li>Sens de la pédagogie et démonstration claire pour valoriser les bénéfices concrets des produits et services.</li>
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

    <!-- COMPÉTENCES CLÉS RETAIL -->
    <section class="main-section">
      <div class="main-section-title">Compétences Clés & Savoir-Faire Retail</div>
      <div class="keywords-block">
        <div class="keyword-line">
          <strong>Vente Conseil & Relation Client :</strong> Accueil haut de gamme, découverte des besoins, argumentation personnalisée, vente complémentaire, fidélisation
        </div>
        <div class="keyword-line">
          <strong>Opérations en Magasin :</strong> Tenue de caisse rapide & exacte, réassort, facing merchandising, gestion des livraisons, inventaire et réapprovisionnement
        </div>
        <div class="keyword-line">
          <strong>Performance & Indicateurs Retail :</strong> Sensibilité aux KPI (panier moyen, taux de transformation, indice de vente), contribution aux objectifs d'équipe
        </div>
        <div class="keyword-line">
          <strong>Esprit d'Équipe & Culture Retail :</strong> Collaboration active, communication constructive, respect de la diversité, dynamisme et culture du sport/lifestyle
        </div>
        <div class="keyword-line">
          <strong>Flexibilité & Engagement :</strong> Disponibilité soirs, week-ends et temps plein/partiel, gestion efficace du stress en forte affluence, ponctualité exemplaire
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
