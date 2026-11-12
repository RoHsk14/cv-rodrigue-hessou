import base64
import subprocess
import fitz

with open('photo.jpg', 'rb') as f:
    photo_b64 = base64.b64encode(f.read()).decode('utf-8')

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def generate_cv(filename_base, title_sub, profile_text):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CV - Rodrigue HESSOU - Software Engineer</title>
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
    gap: 3.5mm;
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
    gap: 1.1mm;
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
    font-size: 8.2pt;
    line-height: 1.24;
    color: #cbd5e1;
  }}

  .sidebar-item strong {{
    color: #ffffff;
    font-weight: 700;
    display: block;
    font-size: 8.4pt;
  }}

  .sidebar-item a {{
    color: #93c5fd;
    text-decoration: none;
    word-break: break-all;
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
    gap: 2.6mm;
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

  .header .tagline {{
    font-size: 8.4pt;
    font-weight: 600;
    color: #475569;
    margin-top: 0.4mm;
  }}

  .main-section {{
    display: flex;
    flex-direction: column;
    gap: 1.4mm;
  }}

  .main-section-title {{
    font-size: 10.4pt;
    font-weight: 700;
    color: #2e75b6;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    padding-bottom: 0.5mm;
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
    gap: 0.45mm;
  }}

  .item-title {{
    font-size: 8.95pt;
    font-weight: 700;
    color: #262626;
  }}

  .item-subrow {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.15pt;
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
    font-size: 8.1pt;
    line-height: 1.22;
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
    gap: 0.15mm;
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
    font-size: 8.05pt;
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
      <div class="sidebar-item">69100 Villeurbanne – Lyon, France</div>
      <div class="sidebar-item">+33 7 44 11 75 73</div>
      <div class="sidebar-item">rodriguehessou14@gmail.com</div>
      <div class="sidebar-item">Portfolio: <a href="https://cv-rodrigue-hessou.vercel.app" target="_blank">cv-rodrigue-hessou.vercel.app</a></div>
      <div class="sidebar-item">GitHub: <a href="https://github.com/RoHsk14" target="_blank">github.com/RoHsk14</a></div>
      <div class="sidebar-item">LinkedIn: <a href="https://www.linkedin.com/in/rodrigue-hessou-aa2b11416" target="_blank">in/rodrigue-hessou</a></div>
    </div>

    <!-- LANGUAGES -->
    <div class="sidebar-section">
      <div class="sidebar-title">Languages</div>
      <div class="sidebar-item">
        <strong>French</strong>
        Native speaker — fluent & articulate
      </div>
      <div class="sidebar-item">
        <strong>English</strong>
        B1/B2 — Technical documentation, professional working proficiency
      </div>
    </div>

    <!-- TECH SPECIALIZATIONS -->
    <div class="sidebar-section">
      <div class="sidebar-title">Core Specializations</div>
      <div class="sidebar-item">
        <strong>Infrastructure & Network Security</strong>
        Linux Hardening, TCP/IP, VLAN, Wireshark, Nmap, Cryptography (TLS/AES), Passkeys (FIDO2)
      </div>
      <div class="sidebar-item">
        <strong>Software Engineering & Backend</strong>
        Java, Python, C/C++, PostgreSQL, MySQL, Relational SQL, REST APIs, Docker
      </div>
      <div class="sidebar-item">
        <strong>Mobile & Cloud Computing</strong>
        Flutter, Dart, iOS (App Store Connect, APNs), Android, Firebase, Cloud
      </div>
      <div class="sidebar-item">
        <strong>Engineering Practices & QA</strong>
        Agile/Scrum, OWASP Top 10 Audits, Functional QA (103 Test Cases), Git/GitHub CI
      </div>
    </div>

    <!-- SOFT SKILLS -->
    <div class="sidebar-section">
      <div class="sidebar-title">Strengths</div>
      <ul class="sidebar-list">
        <li>Cross-functional teamwork & communication</li>
        <li>Analytical rigor & clean code standards</li>
        <li>Attention to detail & software quality</li>
        <li>High adaptability & fast technical learning</li>
      </ul>
    </div>

    <!-- INTERESTS -->
    <div class="sidebar-section">
      <div class="sidebar-title">Interests</div>
      <div class="sidebar-item compact">Football (Team spirit & discipline)</div>
      <div class="sidebar-item compact">Music & audio creation</div>
      <div class="sidebar-item compact">Tech monitoring, UI/UX design & Open Source</div>
    </div>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="main-content">
    <!-- HEADER -->
    <header class="header">
      <h1>Rodrigue HESSOU</h1>
      <div class="subtitle">{title_sub}</div>
      <div class="tagline">Dual Expertise: Software Engineering & Cybersecurity • Direct Pathway to Master 2</div>
    </header>

    <!-- PROFILE -->
    <section class="main-section">
      <div class="main-section-title">Professional Summary</div>
      <p class="profile-text">
        {profile_text}
      </p>
    </section>

    <!-- PROFESSIONAL EXPERIENCE -->
    <section class="main-section">
      <div class="main-section-title">Work Experience</div>

      <!-- NATAN GROUP -->
      <div class="experience-item">
        <div class="item-title">Software Engineering & QA Intern — Mobile, QA & Business Dev</div>
        <div class="item-subrow">
          <span>Nataan Group (IT Services) — Lomé, Togo</span>
          <span>Jul 2026 – Sep 2026</span>
        </div>
        <ul class="item-bullets">
          <li><strong>BoutiK Mobile Application:</strong> Co-developed a retail POS & inventory management mobile app using <strong>Flutter</strong>, connected to <strong>Firebase</strong> and integrated with <strong>FedaPay</strong> payment gateway.</li>
          <li><strong>iOS Architecture & Release:</strong> Handled iOS porting, Apple HIG compliance, OTP authentication, Apple Push Notifications (<strong>APNs</strong>), and live production release on <strong>App Store Connect</strong>.</li>
          <li><strong>Quality Assurance & Web Overhaul:</strong> Designed and conducted end-to-end functional test suites (executed <strong>103 test cases</strong>), performed UI/UX ergonomics audits, and led frontend web revamps.</li>
          <li><strong>B2B Tech Strategy & Data:</strong> Engaged with <strong>100 target SMB merchants</strong> for requirement analysis and delivered structured customer data archiving solutions.</li>
        </ul>
      </div>

      <!-- ATANYS -->
      <div class="experience-item">
        <div class="item-title">Web Development Intern</div>
        <div class="item-subrow">
          <span>ATANYS — Lomé, Togo</span>
          <span>Sep 2025 – Dec 2025</span>
        </div>
        <ul class="item-bullets">
          <li>Designed and developed a full-stack web platform for reporting, indexing, and matching lost and found items.</li>
          <li>Contributed across the entire SDLC: requirements gathering, relational database modeling (SQL), core MVC development, and user acceptance testing.</li>
        </ul>
      </div>

      <!-- DAROLLO -->
      <div class="experience-item">
        <div class="item-title">Mobile Application Development Intern</div>
        <div class="item-subrow">
          <span>Darollo Technologies Corporation — Lomé, Togo</span>
          <span>Jul 2025 – Aug 2025</span>
        </div>
        <ul class="item-bullets">
          <li>Built a bespoke <strong>Flutter</strong> mobile application for fashion artisans to streamline order management, client measurements, and delivery notifications.</li>
          <li>Engineered an <strong>offline-first local persistence architecture</strong> with automatic background data synchronization upon network recovery.</li>
        </ul>
      </div>

      <!-- ONG-CRISTO -->
      <div class="experience-item">
        <div class="item-title">Data Management Intern</div>
        <div class="item-subrow">
          <span>ONG-CRISTO — Lomé, Togo</span>
          <span>Jul 2024 – Sep 2024</span>
        </div>
        <ul class="item-bullets">
          <li>Built and automated a structured data collection pipeline for a field research consultancy.</li>
          <li>Cleaned, validated, and ensured the integrity of quantitative field survey datasets.</li>
        </ul>
      </div>
    </section>

    <!-- EDUCATION -->
    <section class="main-section">
      <div class="main-section-title">Education & Credentials</div>
      <div class="formation-list">
        <div class="formation-item">
          <div class="formation-title">Master of Science in Infrastructure & Network Systems Security (Bac+5 / 5-Year Degree)</div>
          <div class="formation-subrow">
            <span>SUPINFO Lyon — Lyon, France</span>
            <span>Since Oct 2026</span>
          </div>
        </div>

        <div class="formation-item">
          <div class="formation-title">Bachelor of Science in Software Engineering (Honors / Mention Bien)</div>
          <div class="formation-subrow">
            <span>IAI-TOGO (African Institute of Computer Science) — Lomé, Togo</span>
            <span>Nov 2022 – Dec 2025</span>
          </div>
        </div>

        <div class="formation-item">
          <div class="formation-title">French Scientific Baccalaureate (High School Diploma, Mathematics & Physics)</div>
          <div class="formation-subrow">
            <span>LPL Le Rossignol — Lomé, Togo</span>
            <span>Sep 2021 – Jun 2022</span>
          </div>
        </div>
      </div>
    </section>

    <!-- CORE COMPETENCIES KEYWORDS -->
    <section class="main-section">
      <div class="main-section-title">Core Competencies & Keywords</div>
      <div class="keywords-block">
        <div class="keyword-line">
          <strong>Infrastructure & Network Security:</strong> Linux Hardening, TCP/IP, VLAN, Wireshark, Nmap, Cryptography (TLS/AES), Passkeys (FIDO2)
        </div>
        <div class="keyword-line">
          <strong>Software Engineering & Backend:</strong> Java, Python, C/C++, PostgreSQL, MySQL, Relational SQL Modeling, RESTful APIs, Docker
        </div>
        <div class="keyword-line">
          <strong>Mobile & Cloud Computing:</strong> Flutter, Dart, iOS (App Store Connect, APNs), Android, Firebase, Offline Sync Architecture
        </div>
        <div class="keyword-line">
          <strong>QA, Security & Engineering Practices:</strong> Agile/Scrum, OWASP Security Audits, Functional QA (103 Test Cases), Git/GitHub CI
        </div>
      </div>
    </section>
  </main>

</body>
</html>
"""
    html_file = f"{filename_base}.html"
    pdf_file = f"{filename_base}.pdf"

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Wrote {html_file}")

    cmd = [
        chrome_path, "--headless", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_file}", html_file
    ]
    subprocess.run(cmd, check=True)
    print(f"Generated {pdf_file}")

    doc = fitz.open(pdf_file)
    count = len(doc)
    print(f"{pdf_file}: page count = {count}")
    assert count == 1, f"Expected 1 page, got {count} in {pdf_file}"

    # Generate preview image
    page = doc[0]
    pix = page.get_pixmap(dpi=150)
    preview_path = f"{filename_base}_preview.png"
    pix.save(preview_path)
    print(f"Saved preview: {preview_path}")

# 1. Internship (Stage Tech) EN
generate_cv(
    "CV_Rodrigue_HESSOU_Stage_Tech_EN",
    "Software Engineering, Infrastructure & Network Security — Internship (4 to 6 months)",
    "Graduate student pursuing a <strong>Master of Science in Infrastructure & Network Systems Security at SUPINFO Lyon (5-year degree)</strong> and holder of a <strong>Bachelor of Science in Software Engineering (Honors / Mention Bien)</strong> from IAI-TOGO. Seeking a <strong>4 to 6-month software engineering internship</strong> with a direct pathway to a Master 2 work-study / apprenticeship. Combining strong software engineering skills (Java, Python, Flutter, SQL) with practical network security foundations (Linux hardening, TCP/IP, cryptography, security audits), I build reliable, performant, and resilient applications designed for modern enterprise environments."
)

# 2. Apprenticeship (Alternance Tech) EN
generate_cv(
    "CV_Rodrigue_HESSOU_Alternance_Tech_EN",
    "Software Engineer & Network Systems Security — Master's Apprenticeship (Bac+5)",
    "Graduate student pursuing a <strong>Master of Science in Infrastructure & Network Systems Security at SUPINFO Lyon (5-year degree)</strong> and holder of a <strong>Bachelor of Science in Software Engineering (Honors / Mention Bien)</strong> from IAI-TOGO. Seeking a <strong>12 to 24-month work-study apprenticeship</strong> starting immediately. Combining software engineering expertise (Java, Python, Flutter, SQL) with practical network security skills (Linux hardening, TCP/IP, cryptography, security audits), I contribute proactively to building robust software and maintaining secure, scalable system architectures."
)

# 3. Master / General Tech CV EN
generate_cv(
    "CV_Rodrigue_HESSOU_EN",
    "Software Engineer & Network Systems Security (Master's Degree / Bac+5)",
    "Graduate student in <strong>Computer Science & Network Systems Security at SUPINFO Lyon (5-year degree)</strong> with a <strong>Bachelor of Science in Software Engineering (Honors)</strong>. Dual expertise spanning <strong>software engineering</strong> (Java, Python, Flutter, SQL, REST APIs) and <strong>systems & network security</strong> (Linux hardening, TCP/IP, cryptography, security audits). Proven track record delivering production-grade mobile apps (BoutiK), web platforms, and automated data pipelines. Ready to contribute with high autonomy and engineering rigor to ambitious software projects."
)

print("ALL ENGLISH CVS SUCCESSFULLY GENERATED!")
