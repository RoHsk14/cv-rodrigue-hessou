import re

html_content = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Rodrigue HESSOU — Software Engineer & Master 1 Informatique (Bac+5)</title>
<meta name="description" content="Portfolio de Rodrigue HESSOU. Étudiant en Master 1 Informatique à SUPINFO Lyon. Spécialité en génie logiciel, développement back-end et fullstack (Java, Python, C++, SQL, Flutter).">
<meta name="theme-color" content="#09090b">

<!-- OpenGraph / Social -->
<meta property="og:title" content="Rodrigue HESSOU — Software Engineer (Bac+5)">
<meta property="og:description" content="Étudiant Master 1 Informatique SUPINFO Lyon. Candidatures générales stage et alternance.">
<meta property="og:type" content="website">

<!-- Fonts: Plus Jakarta Sans & JetBrains Mono -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
  :root {
    --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    --font-mono: 'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace;

    /* Base Dark Theme (Default - chanhdai.com style) */
    --bg: #09090b;
    --bg-subtle: #0d0d11;
    --surface: #121216;
    --surface-elevated: #18181d;
    --surface-hover: #1f1f26;
    --border: rgba(255, 255, 255, 0.08);
    --border-subtle: rgba(255, 255, 255, 0.04);
    --border-active: rgba(255, 255, 255, 0.22);
    
    --text-primary: #f4f4f5;
    --text-secondary: #a1a1aa;
    --text-muted: #71717a;
    
    --accent: #3b82f6;
    --accent-dark: #1d4ed8;
    --accent-subtle: rgba(59, 130, 246, 0.12);
    --accent-glow: rgba(59, 130, 246, 0.25);
    
    --green: #10b981;
    --green-subtle: rgba(16, 185, 129, 0.12);
    --amber: #f59e0b;
    --amber-subtle: rgba(245, 158, 11, 0.12);
    --sky: #38bdf8;
    --sky-subtle: rgba(56, 189, 248, 0.12);
    
    --tag-bg: rgba(255, 255, 255, 0.04);
    --tag-border: rgba(255, 255, 255, 0.08);
    --tag-text: #d4d4d8;

    --card-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.5);
    --nav-blur: rgba(9, 9, 11, 0.85);
  }

  [data-theme="light"] {
    --bg: #fbfbfb;
    --bg-subtle: #f4f4f5;
    --surface: #ffffff;
    --surface-elevated: #f4f4f6;
    --surface-hover: #ebebee;
    --border: #e4e4e7;
    --border-subtle: #f0f0f2;
    --border-active: #71717a;
    
    --text-primary: #09090b;
    --text-secondary: #52525b;
    --text-muted: #71717a;
    
    --accent: #2563eb;
    --accent-dark: #1e40af;
    --accent-subtle: rgba(37, 99, 235, 0.08);
    --accent-glow: rgba(37, 99, 235, 0.15);
    
    --tag-bg: #f4f4f5;
    --tag-border: #e4e4e7;
    --tag-text: #27272a;

    --card-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.06);
    --nav-blur: rgba(251, 251, 251, 0.85);
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  html {
    scroll-behavior: smooth;
    font-size: 16px;
  }

  body {
    font-family: var(--font-sans);
    background-color: var(--bg);
    color: var(--text-primary);
    min-height: 100vh;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    transition: background-color 0.25s ease, color 0.25s ease;
    overflow-x: hidden;
  }

  /* Lined Grid Container (chanhdai.com layout) */
  .layout-wrapper {
    max-width: 980px;
    margin: 0 auto;
    border-left: 1px solid var(--border);
    border-right: 1px solid var(--border);
    background-color: var(--bg);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    position: relative;
  }

  /* TOP STICKY NAVBAR */
  .top-navbar {
    position: sticky;
    top: 0;
    z-index: 100;
    background: var(--nav-blur);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--border);
    padding: 10px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    transition: border-color 0.2s ease;
  }

  .nav-left {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
    color: inherit;
  }

  .nav-avatar-mini {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    object-fit: cover;
    border: 1px solid var(--border);
  }

  .nav-brand-text {
    display: flex;
    flex-direction: column;
  }

  .nav-brand-name {
    font-size: 13.5px;
    font-weight: 700;
    letter-spacing: -0.2px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .nav-brand-sub {
    font-family: var(--font-mono);
    font-size: 10.5px;
    color: var(--text-muted);
  }

  .status-pulse-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background-color: var(--green);
    display: inline-block;
    position: relative;
  }

  .status-pulse-dot::after {
    content: '';
    position: absolute;
    inset: -2px;
    border-radius: 50%;
    background-color: var(--green);
    opacity: 0.5;
    animation: statusPulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  }

  @keyframes statusPulse {
    0% { transform: scale(1); opacity: 0.8; }
    50% { transform: scale(2.2); opacity: 0; }
    100% { transform: scale(1); opacity: 0; }
  }

  .nav-menu {
    display: flex;
    align-items: center;
    gap: 16px;
    list-style: none;
  }

  .nav-link {
    font-size: 13px;
    font-weight: 500;
    color: var(--text-secondary);
    text-decoration: none;
    transition: color 0.15s ease;
    padding: 6px 4px;
  }

  .nav-link:hover {
    color: var(--text-primary);
  }

  .nav-right-actions {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .cmd-trigger-btn {
    font-family: var(--font-mono);
    font-size: 12px;
    color: var(--text-secondary);
    background: var(--surface-elevated);
    border: 1px solid var(--border);
    padding: 6px 10px;
    border-radius: 7px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    transition: all 0.15s ease;
  }

  .cmd-trigger-btn:hover {
    color: var(--text-primary);
    border-color: var(--border-active);
    background: var(--surface-hover);
  }

  .cmd-shortcut-badge {
    font-size: 10.5px;
    padding: 1px 5px;
    border-radius: 4px;
    background: var(--tag-bg);
    border: 1px solid var(--border);
    color: var(--text-muted);
  }

  .theme-toggle-btn, .login-nav-btn {
    background: var(--surface-elevated);
    border: 1px solid var(--border);
    color: var(--text-secondary);
    padding: 6px 10px;
    border-radius: 7px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    cursor: pointer;
    font-size: 12px;
    font-family: var(--font-mono);
    transition: all 0.15s ease;
    text-decoration: none;
  }

  .theme-toggle-btn:hover, .login-nav-btn:hover {
    color: var(--text-primary);
    border-color: var(--border-active);
    background: var(--surface-hover);
  }

  .login-nav-btn.authenticated {
    border-color: rgba(16, 185, 129, 0.4);
    color: var(--green);
    background: var(--green-subtle);
  }

  /* SVG Icons inline styling */
  .icon-svg {
    display: inline-block;
    vertical-align: middle;
    width: 14px;
    height: 14px;
    stroke: currentColor;
    fill: none;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  /* HERO SECTION */
  .hero-section {
    padding: 44px 32px 36px;
    border-bottom: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    gap: 24px;
    background: radial-gradient(circle at 10% 0%, var(--accent-subtle) 0%, transparent 60%);
  }

  .hero-top-row {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 24px;
  }

  .hero-bio-container {
    display: flex;
    flex-direction: column;
    gap: 12px;
    flex: 1;
  }

  .status-pill {
    font-family: var(--font-mono);
    font-size: 11.5px;
    font-weight: 500;
    padding: 4px 10px;
    border-radius: 999px;
    background: var(--green-subtle);
    border: 1px solid rgba(16, 185, 129, 0.25);
    color: var(--green);
    display: inline-flex;
    align-items: center;
    gap: 7px;
    width: fit-content;
  }

  .hero-name-block h1 {
    font-size: 32px;
    font-weight: 800;
    letter-spacing: -0.8px;
    color: var(--text-primary);
    line-height: 1.15;
  }

  .hero-title-role {
    font-size: 16px;
    font-weight: 600;
    color: var(--accent);
    margin-top: 3px;
  }

  .hero-lead-text {
    font-size: 14.5px;
    line-height: 1.6;
    color: var(--text-secondary);
    max-width: 620px;
  }

  .hero-lead-text strong {
    color: var(--text-primary);
    font-weight: 600;
  }

  .hero-avatar-wrapper {
    position: relative;
    flex-shrink: 0;
  }

  .hero-avatar-img {
    width: 110px;
    height: 110px;
    border-radius: 20px;
    object-fit: cover;
    border: 2px solid var(--border);
    box-shadow: 0 10px 30px -8px var(--accent-glow);
    transition: transform 0.25s ease, border-color 0.25s ease;
  }

  .hero-avatar-img:hover {
    transform: scale(1.03);
    border-color: var(--accent);
  }

  .hero-meta-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    font-family: var(--font-mono);
    font-size: 12px;
    color: var(--text-muted);
  }

  .hero-meta-item {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--tag-bg);
    border: 1px solid var(--border);
    padding: 4px 10px;
    border-radius: 6px;
  }

  .hero-actions-bar {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 10px;
    padding-top: 4px;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 600;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.15s ease;
    border: 1px solid transparent;
  }

  .btn-primary {
    background: var(--text-primary);
    color: var(--bg);
  }

  .btn-primary:hover {
    opacity: 0.9;
    transform: translateY(-1px);
  }

  .btn-secondary {
    background: var(--surface-elevated);
    border-color: var(--border);
    color: var(--text-primary);
  }

  .btn-secondary:hover {
    background: var(--surface-hover);
    border-color: var(--border-active);
    transform: translateY(-1px);
  }

  .btn-copy {
    font-family: var(--font-mono);
    font-size: 12px;
    background: var(--tag-bg);
    border: 1px solid var(--border);
    color: var(--text-secondary);
    padding: 7px 12px;
    border-radius: 8px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.15s ease;
  }

  .btn-copy:hover {
    color: var(--text-primary);
    border-color: var(--border-active);
    background: var(--surface-hover);
  }

  /* METRICS GRID */
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    background: var(--bg-subtle);
  }

  .stat-card {
    padding: 16px 20px;
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .stat-card:last-child {
    border-right: none;
  }

  .stat-num {
    font-family: var(--font-mono);
    font-size: 20px;
    font-weight: 700;
    color: var(--text-primary);
    letter-spacing: -0.5px;
  }

  .stat-label {
    font-size: 11.5px;
    color: var(--text-muted);
    font-weight: 500;
  }

  /* CONTENT SECTIONS */
  .content-section {
    padding: 36px 32px;
    border-bottom: 1px solid var(--border);
  }

  .section-header-block {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 20px;
  }

  .section-title {
    font-size: 19px;
    font-weight: 700;
    letter-spacing: -0.3px;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .section-desc {
    font-size: 12.5px;
    color: var(--text-muted);
    font-family: var(--font-mono);
  }

  /* SHOWCASE CARDS (VITRINE TECHNIQUE) */
  .showcase-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }

  .showcase-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 16px;
    transition: all 0.2s ease;
  }

  .showcase-card:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
    background: var(--surface-elevated);
    box-shadow: 0 10px 25px -8px var(--accent-glow);
  }

  .showcase-badge {
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    width: fit-content;
    margin-bottom: 6px;
    background: var(--accent-subtle);
    color: var(--accent);
    border: 1px solid rgba(59, 130, 246, 0.25);
  }

  .showcase-title {
    font-size: 18px;
    font-weight: 700;
    color: var(--text-primary);
  }

  .showcase-sub {
    font-family: var(--font-mono);
    font-size: 12px;
    color: var(--text-muted);
    margin-top: 2px;
  }

  .showcase-desc {
    font-size: 13.5px;
    color: var(--text-secondary);
    line-height: 1.5;
  }

  .tags-list {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .tech-tag {
    font-family: var(--font-mono);
    font-size: 11px;
    padding: 2px 7px;
    border-radius: 4px;
    background: var(--tag-bg);
    border: 1px solid var(--tag-border);
    color: var(--tag-text);
  }

  .showcase-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    padding-top: 10px;
    border-top: 1px dashed var(--border);
  }

  .btn-sm {
    padding: 6px 12px;
    font-size: 12px;
    border-radius: 6px;
  }

  /* TIMELINE */
  .timeline-list {
    display: flex;
    flex-direction: column;
    gap: 24px;
    position: relative;
    padding-left: 20px;
    border-left: 1px solid var(--border);
    margin-left: 8px;
  }

  .timeline-item {
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .timeline-node {
    position: absolute;
    left: -25px;
    top: 5px;
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: var(--bg);
    border: 2px solid var(--accent);
  }

  .timeline-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    flex-wrap: wrap;
    gap: 8px;
  }

  .timeline-role {
    font-size: 15px;
    font-weight: 700;
    color: var(--text-primary);
  }

  .timeline-company {
    font-size: 13.5px;
    color: var(--accent);
    font-weight: 600;
  }

  .timeline-date {
    font-family: var(--font-mono);
    font-size: 11.5px;
    color: var(--text-muted);
  }

  .timeline-desc {
    font-size: 13px;
    color: var(--text-secondary);
    line-height: 1.5;
  }

  /* PROJECTS GRID */
  .projects-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }

  .project-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 12px;
    transition: all 0.2s ease;
  }

  .project-card:hover {
    border-color: var(--border-active);
    transform: translateY(-2px);
    background: var(--surface-elevated);
  }

  .project-title {
    font-size: 15px;
    font-weight: 700;
    color: var(--text-primary);
  }

  .project-desc {
    font-size: 12.5px;
    color: var(--text-secondary);
    line-height: 1.45;
  }

  /* STACK CHIPS */
  .stack-category-block {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 18px;
  }

  .stack-category-title {
    font-family: var(--font-mono);
    font-size: 11.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--text-muted);
  }

  .stack-chips-wrap {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  .stack-chip {
    font-family: var(--font-mono);
    font-size: 12px;
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text-primary);
    padding: 5px 11px;
    border-radius: 6px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.15s ease;
  }

  .stack-chip:hover {
    border-color: var(--border-active);
    background: var(--surface-hover);
    transform: translateY(-1px);
  }

  /* PRIVATE PORTAL / AUTH CALLOUT BANNER */
  .private-access-banner {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    transition: all 0.2s ease;
  }

  .private-banner-content h3 {
    font-size: 16px;
    font-weight: 700;
    color: var(--text-primary);
  }

  .private-banner-content p {
    font-size: 13px;
    color: var(--text-secondary);
    margin-top: 4px;
    max-width: 580px;
  }

  /* PRIVATE SECTION (DISPLAYED WHEN LOGGED IN) */
  #private-dashboard {
    display: none;
    border-top: 2px solid var(--accent);
    background: var(--bg-subtle);
  }

  #private-dashboard.authenticated {
    display: block;
  }

  .private-header-bar {
    background: var(--surface-elevated);
    border-bottom: 1px solid var(--border);
    padding: 12px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .private-status-tag {
    font-family: var(--font-mono);
    font-size: 12px;
    color: var(--green);
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }

  .bento-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }

  .bento-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 16px;
    transition: all 0.2s ease;
  }

  .bento-card:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
  }

  .bento-title h4 {
    font-size: 16px;
    font-weight: 700;
    color: var(--text-primary);
  }

  .bento-title p {
    font-size: 12px;
    color: var(--text-muted);
  }

  .bento-features {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
    font-size: 12px;
    color: var(--text-secondary);
  }

  .bento-features li::before {
    content: "[*] ";
    color: var(--accent);
    font-family: var(--font-mono);
  }

  .private-docs-list {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }

  .private-doc-item {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    transition: all 0.15s ease;
  }

  .private-doc-item:hover {
    border-color: var(--border-active);
    background: var(--surface-hover);
  }

  .private-doc-title {
    font-size: 13px;
    font-weight: 600;
    color: var(--text-primary);
  }

  .private-doc-sub {
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--text-muted);
  }

  /* FOOTER */
  .site-footer {
    padding: 36px 32px;
    background: var(--bg-subtle);
    display: flex;
    flex-direction: column;
    gap: 20px;
    font-size: 12px;
    color: var(--text-muted);
  }

  .footer-top-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
  }

  .footer-links {
    display: flex;
    gap: 16px;
    list-style: none;
  }

  .footer-links a {
    color: var(--text-secondary);
    text-decoration: none;
    transition: color 0.15s ease;
  }

  .footer-links a:hover {
    color: var(--text-primary);
  }

  .footer-bottom-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    border-top: 1px solid var(--border);
    padding-top: 18px;
    font-family: var(--font-mono);
    font-size: 11.5px;
  }

  /* DIALOGS (COMMAND PALETTE & LOGIN) */
  dialog#cmd-dialog, dialog#login-modal {
    margin: 80px auto auto auto;
    border: 1px solid var(--border-active);
    border-radius: 12px;
    background: var(--surface);
    color: var(--text-primary);
    width: 90%;
    max-width: 540px;
    box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.75);
    padding: 0;
    overflow: hidden;
  }

  dialog:modal {
    overscroll-behavior: contain;
  }

  dialog::backdrop {
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    overflow: hidden;
    overscroll-behavior: contain;
  }

  .cmd-box {
    display: flex;
    flex-direction: column;
  }

  .cmd-input-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 14px 18px;
    border-bottom: 1px solid var(--border);
  }

  .cmd-search-input {
    flex: 1;
    background: transparent;
    border: none;
    font-family: var(--font-sans);
    font-size: 14px;
    color: var(--text-primary);
    outline: none;
  }

  .cmd-search-input::placeholder {
    color: var(--text-muted);
  }

  .cmd-results-list {
    max-height: 380px;
    overflow-y: auto;
    padding: 10px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    list-style: none;
  }

  .cmd-category-header {
    font-family: var(--font-mono);
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    color: var(--text-muted);
    padding: 8px 10px 4px;
  }

  .cmd-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 9px 12px;
    border-radius: 6px;
    font-size: 13px;
    color: var(--text-secondary);
    text-decoration: none;
    cursor: pointer;
    transition: all 0.1s ease;
  }

  .cmd-item:hover {
    background: var(--surface-hover);
    color: var(--text-primary);
  }

  .cmd-item-left {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .cmd-item-badge {
    font-family: var(--font-mono);
    font-size: 10.5px;
    color: var(--text-muted);
  }

  .cmd-footer-bar {
    padding: 8px 16px;
    background: var(--bg-subtle);
    border-top: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--text-muted);
  }

  /* LOGIN FORM */
  .login-card {
    padding: 24px 28px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .login-header h3 {
    font-size: 18px;
    font-weight: 700;
    color: var(--text-primary);
  }

  .login-header p {
    font-size: 12.5px;
    color: var(--text-muted);
    margin-top: 2px;
  }

  .login-form-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .login-form-group label {
    font-family: var(--font-mono);
    font-size: 11.5px;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    color: var(--text-muted);
  }

  .login-input {
    background: var(--surface-elevated);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 10px 14px;
    font-family: var(--font-mono);
    font-size: 13.5px;
    color: var(--text-primary);
    outline: none;
    transition: border-color 0.15s ease;
  }

  .login-input:focus {
    border-color: var(--accent);
  }

  .login-error-msg {
    color: #ef4444;
    font-size: 12px;
    font-family: var(--font-mono);
    display: none;
  }

  .login-actions {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 4px;
  }

  /* TOAST */
  .toast {
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: var(--surface-elevated);
    border: 1px solid var(--border-active);
    color: var(--text-primary);
    padding: 10px 16px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 500;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    transform: translateY(80px);
    opacity: 0;
    transition: all 0.25s ease;
    z-index: 1000;
  }

  .toast.show {
    transform: translateY(0);
    opacity: 1;
  }

  /* RESPONSIVE */
  @media (max-width: 768px) {
    .layout-wrapper {
      border-left: none;
      border-right: none;
    }
    .hero-top-row {
      flex-direction: column-reverse;
      align-items: center;
      text-align: center;
    }
    .hero-actions-bar, .hero-meta-row {
      justify-content: center;
    }
    .stats-grid, .showcase-grid, .bento-grid, .projects-grid, .private-docs-list {
      grid-template-columns: 1fr;
    }
    .nav-menu {
      display: none;
    }
    .content-section, .hero-section {
      padding: 24px 18px;
    }
    .private-access-banner {
      flex-direction: column;
      text-align: center;
    }
  }
</style>
</head>
<body>

  <div class="layout-wrapper">

    <!-- TOP NAVBAR -->
    <header class="top-navbar">
      <a href="#overview" class="nav-left">
        <img src="photo.jpg" alt="Rodrigue HESSOU" class="nav-avatar-mini">
        <div class="nav-brand-text">
          <div class="nav-brand-name">
            Rodrigue HESSOU
            <span class="status-pulse-dot" title="Disponible pour opportunités"></span>
          </div>
          <span class="nav-brand-sub">M1 Informatique / SUPINFO Lyon</span>
        </div>
      </a>

      <nav>
        <ul class="nav-menu">
          <li><a href="#candidatures" class="nav-link">Candidatures</a></li>
          <li><a href="#experience" class="nav-link">Expérience</a></li>
          <li><a href="#projets" class="nav-link">Projets</a></li>
          <li><a href="#competences" class="nav-link">Stack</a></li>
          <li><a href="#formation" class="nav-link">Formation</a></li>
        </ul>
      </nav>

      <div class="nav-right-actions">
        <button class="cmd-trigger-btn" onclick="openCmdPalette()" title="Ouvrir la palette de commandes (Ctrl+K)">
          <span>Recherche</span>
          <kbd class="cmd-shortcut-badge">Ctrl+K</kbd>
        </button>

        <button class="theme-toggle-btn" id="theme-btn" onclick="toggleTheme()" title="Basculer le thème clair / sombre">
          <svg class="icon-svg" id="theme-icon" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>

        <button class="login-nav-btn" id="nav-auth-btn" onclick="handleAuthNavClick()">
          <svg class="icon-svg" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          <span id="nav-auth-text">Connexion</span>
        </button>
      </div>
    </header>

    <!-- HERO PROFILE -->
    <section class="hero-section" id="overview">
      <div class="hero-top-row">
        <div class="hero-bio-container">
          <div class="status-pill">
            <span class="status-pulse-dot"></span>
            Disponible : Stage (Bac+5) & Alternance
          </div>

          <div class="hero-name-block">
            <h1>Rodrigue HESSOU</h1>
            <div class="hero-title-role">Étudiant Master 1 en Informatique (Cursus Bac+5)</div>
          </div>

          <p class="hero-lead-text">
            Passionné par le <strong>génie logiciel</strong> et l'architecture applicative. Titulaire d'une Licence en Génie Logiciel (Mention Bien) et actuellement en Master 1 à <strong>SUPINFO Lyon</strong>. Expertise concrète en développement back-end & fullstack (Java, Python, C++, SQL, Flutter, Web), tests unitaires et conduite de projets en méthodes Agiles.
          </p>

          <div class="hero-meta-row">
            <span class="hero-meta-item">Localisation : Lyon, France</span>
            <span class="hero-meta-item">Formation : SUPINFO Lyon (2026 - 2028)</span>
            <span class="hero-meta-item">Diplôme : Licence Génie Logiciel (Mention Bien)</span>
            <span class="hero-meta-item">Langues : Anglais B2</span>
          </div>

          <div class="hero-actions-bar">
            <a href="#candidatures" class="btn btn-primary">
              Consulter les Candidatures
            </a>
            <button class="btn-copy" onclick="copyContact('rodriguehessou14@gmail.com', 'Email copié dans le presse-papier')">
              rodriguehessou14@gmail.com
            </button>
            <button class="btn-copy" onclick="copyContact('+33 7 44 11 75 73', 'Téléphone copié dans le presse-papier')">
              +33 7 44 11 75 73
            </button>
          </div>
        </div>

        <div class="hero-avatar-wrapper">
          <img src="photo.jpg" alt="Photo Rodrigue HESSOU" class="hero-avatar-img">
        </div>
      </div>
    </section>

    <!-- METRICS STRIP -->
    <div class="stats-grid">
      <div class="stat-card">
        <span class="stat-num">Bac+5</span>
        <span class="stat-label">Cursus Ingénierie SUPINFO</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">2</span>
        <span class="stat-label">Dossiers Techniques Dédiés</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">100+</span>
        <span class="stat-label">Cas de Recette & QA Exécutés</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">100%</span>
        <span class="stat-label">Format A4 Strict 1 Page</span>
      </div>
    </div>

    <!-- --------------------------------------------------
         VITRINE PUBLIQUE: CANDIDATURES TECHNIQUES GENERALES
         -------------------------------------------------- -->
    <section class="content-section" id="candidatures">
      <div class="section-header-block">
        <h2 class="section-title">Candidatures Techniques (Vitrine Publique)</h2>
        <span class="section-desc">Dossiers généraux conventionnés Bac+5</span>
      </div>

      <div class="showcase-grid">

        <!-- 1. STAGE TECHNIQUE GENERAL -->
        <div class="showcase-card">
          <div>
            <span class="showcase-badge">Stage Conventionné</span>
            <h3 class="showcase-title">Développeur Logiciel — Recherche de Stage</h3>
            <div class="showcase-sub">Niveau Master 1 / Bac+5 Informatique — Lyon & Remote</div>

            <p class="showcase-desc" style="margin-top: 10px;">
              Candidature générale pour stage en développement logiciel. Conception orientée objet, développement back-end et fullstack, création d'APIs REST, intégration de bases de données relationnelles, tests unitaires approfondis et documentation technique.
            </p>

            <div class="tags-list" style="margin-top: 12px;">
              <span class="tech-tag">Java</span>
              <span class="tech-tag">Python</span>
              <span class="tech-tag">SQL</span>
              <span class="tech-tag">C++</span>
              <span class="tech-tag">Méthodes Agiles</span>
              <span class="tech-tag">Tests Unitaires</span>
              <span class="tech-tag">Cycle de Vie Applicatif</span>
            </div>
          </div>

          <div class="showcase-actions">
            <a href="CV_Rodrigue_HESSOU_Stage_Tech.pdf" target="_blank" class="btn btn-secondary btn-sm">
              <svg class="icon-svg" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              CV Stage (PDF)
            </a>
            <a href="Lettre_de_Motivation_Stage_Tech_Rodrigue_HESSOU.pdf" target="_blank" class="btn btn-secondary btn-sm">
              <svg class="icon-svg" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              Lettre Stage (PDF)
            </a>
          </div>
        </div>

        <!-- 2. ALTERNANCE TECHNIQUE GENERALE -->
        <div class="showcase-card">
          <div>
            <span class="showcase-badge">Contrat d'Alternance</span>
            <h3 class="showcase-title">Développeur Logiciel — Recherche d'Alternance</h3>
            <div class="showcase-sub">Rythme Master 1 SUPINFO Lyon (Cursus Bac+5)</div>

            <p class="showcase-desc" style="margin-top: 10px;">
              Candidature générale pour contrat d'alternance en ingénierie logicielle. Investissement sur la durée au sein de l'équipe, participation aux sprints Agiles (Scrum), développement de fonctionnalités métiers, refonte applicative et maintien de standards de code élevés.
            </p>

            <div class="tags-list" style="margin-top: 12px;">
              <span class="tech-tag">Java</span>
              <span class="tech-tag">Python</span>
              <span class="tech-tag">Web Fullstack</span>
              <span class="tech-tag">Flutter / Dart</span>
              <span class="tech-tag">MySQL / PostgreSQL</span>
              <span class="tech-tag">Docker</span>
              <span class="tech-tag">Git & CI/CD</span>
            </div>
          </div>

          <div class="showcase-actions">
            <a href="CV_Rodrigue_HESSOU_Alternance_Tech.pdf" target="_blank" class="btn btn-secondary btn-sm">
              <svg class="icon-svg" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              CV Alternance (PDF)
            </a>
            <a href="Lettre_de_Motivation_Alternance_Tech_Rodrigue_HESSOU.pdf" target="_blank" class="btn btn-secondary btn-sm">
              <svg class="icon-svg" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              Lettre Alternance (PDF)
            </a>
          </div>
        </div>

      </div>
    </section>

    <!-- --------------------------------------------------
         SECTION PARCOURS & EXPERIENCES
         -------------------------------------------------- -->
    <section class="content-section" id="experience">
      <div class="section-header-block">
        <h2 class="section-title">Parcours & Expérience</h2>
        <span class="section-desc">Historique professionnel et technique</span>
      </div>

      <div class="timeline-list">

        <!-- NATAAN GROUP -->
        <div class="timeline-item">
          <span class="timeline-node"></span>
          <div class="timeline-header">
            <div>
              <div class="timeline-role">Stagiaire — Développement Mobile, QA & Business Development</div>
              <div class="timeline-company">Nataan Group (ESN)</div>
            </div>
            <span class="timeline-date">Juil. 2026 - Sept. 2026</span>
          </div>
          <p class="timeline-desc">
            Co-développement de l'application BoutiK sous Flutter et intégration passerelle FedaPay. Portage iOS conforme aux guidelines Apple et publication App Store Connect. Recette fonctionnelle complète (103 cas de tests exécutés) et prospection B2B auprès de 100 commerçants.
          </p>
          <div class="tags-list">
            <span class="tech-tag">Flutter</span>
            <span class="tech-tag">iOS / APNs</span>
            <span class="tech-tag">QA & Recette (103 tests)</span>
            <span class="tech-tag">Firebase</span>
            <span class="tech-tag">Prospection POS</span>
          </div>
        </div>

        <!-- ATANYS -->
        <div class="timeline-item">
          <span class="timeline-node"></span>
          <div class="timeline-header">
            <div>
              <div class="timeline-role">Stagiaire en Développement Web Fullstack</div>
              <div class="timeline-company">ATANYS</div>
            </div>
            <span class="timeline-date">Sept. 2025 - Déc. 2025</span>
          </div>
          <p class="timeline-desc">
            Conception et développement d'une plateforme web complète de signalement et de gestion des objets perdus et retrouvés. Modélisation relationnelle de la base de données MySQL, développement back-end et interface utilisateur.
          </p>
          <div class="tags-list">
            <span class="tech-tag">PHP</span>
            <span class="tech-tag">JavaScript</span>
            <span class="tech-tag">MySQL</span>
            <span class="tech-tag">Architecture MVC</span>
          </div>
        </div>

        <!-- DAROLLO -->
        <div class="timeline-item">
          <span class="timeline-node"></span>
          <div class="timeline-header">
            <div>
              <div class="timeline-role">Stagiaire en Développement d'Applications Mobiles</div>
              <div class="timeline-company">Darollo Technologies Corporation</div>
            </div>
            <span class="timeline-date">Juil. 2025 - Août 2025</span>
          </div>
          <p class="timeline-desc">
            Développement d'une application mobile Flutter dédiée aux artisans tailleurs pour la gestion des commandes et mensurations. Conception d'un fonctionnement hors-ligne (offline-first) avec synchronisation automatique.
          </p>
          <div class="tags-list">
            <span class="tech-tag">Flutter / Dart</span>
            <span class="tech-tag">Architecture Offline-First</span>
            <span class="tech-tag">Synchronisation</span>
          </div>
        </div>

        <!-- LOGISTIQUE & TERRAIN -->
        <div class="timeline-item">
          <span class="timeline-node"></span>
          <div class="timeline-header">
            <div>
              <div class="timeline-role">Préparateur de Commandes & Employé Commercial</div>
              <div class="timeline-company">Plateforme Logistique & Supermarché Champion</div>
            </div>
            <span class="timeline-date">2024 - 2025</span>
          </div>
          <p class="timeline-desc">
            Rigueur de cadence en préparation de commandes, respect des consignes de sécurité. Gestion des encaissements en période de forte affluence, tenue de caisse exacte, réassort et sens du service client.
          </p>
          <div class="tags-list">
            <span class="tech-tag">Rigueur Opérationnelle</span>
            <span class="tech-tag">Tenue de Caisse</span>
            <span class="tech-tag">Gestion du Rush</span>
          </div>
        </div>

        <!-- ONG-CRISTO -->
        <div class="timeline-item">
          <span class="timeline-node"></span>
          <div class="timeline-header">
            <div>
              <div class="timeline-role">Stagiaire en Gestion & Automatisation de Données</div>
              <div class="timeline-company">ONG-CRISTO</div>
            </div>
            <span class="timeline-date">Juil. 2024 - Sept. 2024</span>
          </div>
          <p class="timeline-desc">
            Mise en place d'un système de gestion automatisée de la collecte d'informations pour un cabinet de recherche. Structuration et contrôle qualité des données terrain.
          </p>
          <div class="tags-list">
            <span class="tech-tag">Python</span>
            <span class="tech-tag">Traitement de Données</span>
            <span class="tech-tag">Automatisation</span>
          </div>
        </div>

      </div>
    </section>

    <!-- --------------------------------------------------
         SECTION PROJETS & REALISATIONS
         -------------------------------------------------- -->
    <section class="content-section" id="projets">
      <div class="section-header-block">
        <h2 class="section-title">Projets & Réalisations Techniques</h2>
        <span class="section-desc">Architecture logicielle et code</span>
      </div>

      <div class="projects-grid">

        <div class="project-card">
          <div>
            <div class="project-title">Plateforme Web Objets Perdus & Retrouvés</div>
            <p class="project-desc" style="margin-top: 6px;">
              Service web complet de dépôt d'annonces, recherche indexée et mise en relation sécurisée. Algorithme de correspondance pour les biens égarés.
            </p>
          </div>
          <div class="tags-list">
            <span class="tech-tag">PHP / JS</span>
            <span class="tech-tag">MySQL</span>
            <span class="tech-tag">Modélisation SQL</span>
          </div>
        </div>

        <div class="project-card">
          <div>
            <div class="project-title">Application Mobile Flutter pour Artisans Tailleurs</div>
            <p class="project-desc" style="margin-top: 6px;">
              Application de carnet de mesures et suivi de confection. Architecture locale avec synchronisation dès reconnexion réseau.
            </p>
          </div>
          <div class="tags-list">
            <span class="tech-tag">Flutter</span>
            <span class="tech-tag">Dart</span>
            <span class="tech-tag">Offline-First</span>
          </div>
        </div>

        <div class="project-card">
          <div>
            <div class="project-title">Pipeline Automatisé de Normalisation de Données</div>
            <p class="project-desc" style="margin-top: 6px;">
              Scripts d'ingestion et de nettoyage automatisé de données d'enquêtes terrain, détection des anomalies et export structuré.
            </p>
          </div>
          <div class="tags-list">
            <span class="tech-tag">Python</span>
            <span class="tech-tag">ETL / Data Quality</span>
          </div>
        </div>

        <div class="project-card">
          <div>
            <div class="project-title">Moteur de Génération & Impression CV A4 Exact</div>
            <p class="project-desc" style="margin-top: 6px;">
              Architecture web avec moteur CSS calibré garantissant un export PDF strict 1 page A4 et préservation totale des contrastes et fonds colorés.
            </p>
          </div>
          <div class="tags-list">
            <span class="tech-tag">HTML5 / Vanilla JS</span>
            <span class="tech-tag">Print Engine</span>
          </div>
        </div>

      </div>
    </section>

    <!-- --------------------------------------------------
         SECTION STACK TECHNIQUE
         -------------------------------------------------- -->
    <section class="content-section" id="competences">
      <div class="section-header-block">
        <h2 class="section-title">Stack Technique & Compétences</h2>
        <span class="section-desc">Technologies maîtrisées</span>
      </div>

      <div class="stack-category-block">
        <div class="stack-category-title">Langages de Programmation</div>
        <div class="stack-chips-wrap">
          <span class="stack-chip">Java</span>
          <span class="stack-chip">Python</span>
          <span class="stack-chip">C / C++</span>
          <span class="stack-chip">SQL</span>
          <span class="stack-chip">JavaScript (ES6+)</span>
          <span class="stack-chip">TypeScript</span>
          <span class="stack-chip">Dart</span>
          <span class="stack-chip">PHP</span>
        </div>
      </div>

      <div class="stack-category-block">
        <div class="stack-category-title">Frameworks & Environnements Web / Mobile</div>
        <div class="stack-chips-wrap">
          <span class="stack-chip">Flutter</span>
          <span class="stack-chip">React.js</span>
          <span class="stack-chip">Next.js</span>
          <span class="stack-chip">Node.js</span>
          <span class="stack-chip">Spring Boot (Notions)</span>
          <span class="stack-chip">Django</span>
          <span class="stack-chip">Laravel</span>
          <span class="stack-chip">Tailwind CSS</span>
        </div>
      </div>

      <div class="stack-category-block">
        <div class="stack-category-title">Bases de Données, Outils & Méthodologies</div>
        <div class="stack-chips-wrap">
          <span class="stack-chip">MySQL</span>
          <span class="stack-chip">PostgreSQL</span>
          <span class="stack-chip">Firebase Firestore</span>
          <span class="stack-chip">Git & GitHub</span>
          <span class="stack-chip">Docker</span>
          <span class="stack-chip">Linux / Shell</span>
          <span class="stack-chip">Méthodes Agiles (Scrum)</span>
          <span class="stack-chip">Tests Unitaires & QA</span>
          <span class="stack-chip">Outils EAM / PLM</span>
        </div>
      </div>
    </section>

    <!-- --------------------------------------------------
         SECTION FORMATION
         -------------------------------------------------- -->
    <section class="content-section" id="formation">
      <div class="section-header-block">
        <h2 class="section-title">Formation Académique</h2>
        <span class="section-desc">Diplômes et parcours d'études</span>
      </div>

      <div class="timeline-list">

        <div class="timeline-item">
          <span class="timeline-node"></span>
          <div class="timeline-header">
            <div>
              <div class="timeline-role">Master 1 en Informatique (Cursus Bac+5)</div>
              <div class="timeline-company">SUPINFO Lyon — Lyon, France</div>
            </div>
            <span class="timeline-date">Oct. 2026 - Présent</span>
          </div>
          <p class="timeline-desc">
            Programme d'Ingénierie Informatique : conception et modélisation logicielle, architectures distribuées, bases de données avancées et gestion de projet Agile.
          </p>
        </div>

        <div class="timeline-item">
          <span class="timeline-node"></span>
          <div class="timeline-header">
            <div>
              <div class="timeline-role">Licence Professionnelle en Génie Logiciel (Mention Bien)</div>
              <div class="timeline-company">IAI-TOGO (Institut Africain d'Informatique)</div>
            </div>
            <span class="timeline-date">2022 - 2025</span>
          </div>
          <p class="timeline-desc">
            Algorithmique fondamentale, programmation orientée objet (Java, C++), modélisation relationnelle (UML, Merise), développement web et mobile.
          </p>
        </div>

        <div class="timeline-item">
          <span class="timeline-node"></span>
          <div class="timeline-header">
            <div>
              <div class="timeline-role">Baccalauréat Scientifique (BAC 2)</div>
              <div class="timeline-company">LPL Le Rossignol</div>
            </div>
            <span class="timeline-date">2021 - 2022</span>
          </div>
          <p class="timeline-desc">
            Série scientifique : Mathématiques, Sciences Physiques et SVT.
          </p>
        </div>

      </div>
    </section>

    <!-- --------------------------------------------------
         INVITATION ESPACE PRIVE / CONNEXION
         -------------------------------------------------- -->
    <section class="content-section" id="auth-cta-section">
      <div class="private-access-banner">
        <div class="private-banner-content">
          <h3>Espace Candidat Réservé</h3>
          <p>
            Vous êtes Rodrigue HESSOU ? Connectez-vous à votre espace interne pour accéder à vos dossiers de candidatures ciblées (jobs étudiants, soutien scolaire, retail, restauration rapide) et ouvrir les éditeurs interactifs en ligne.
          </p>
        </div>
        <div>
          <button class="btn btn-secondary" onclick="openLoginModal()" id="btn-login-cta">
            <svg class="icon-svg" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
            Accéder à l'espace interne
          </button>
        </div>
      </div>
    </section>

    <!-- --------------------------------------------------
         ESPACE CACHÉ EN INTERNE (DÉBLOQUÉ APRÈS LOGIN)
         -------------------------------------------------- -->
    <div id="private-dashboard">
      <div class="private-header-bar">
        <div class="private-status-tag">
          <span class="status-pulse-dot"></span>
          Espace Interne Connecté : Rodrigue HESSOU
        </div>
        <button class="btn btn-secondary btn-sm" onclick="logout()">
          Déconnexion
        </button>
      </div>

      <!-- EDITORS BENTO -->
      <section class="content-section">
        <div class="section-header-block">
          <h2 class="section-title">Outils d'Édition en Ligne</h2>
          <span class="section-desc">Personnalisation et export instantané</span>
        </div>

        <div class="bento-grid">
          <div class="bento-card">
            <div>
              <div class="bento-title">
                <h4>Éditeur de CV Interactif</h4>
                <p>Mise en page WYSIWYG sur feuille A4 stricte</p>
              </div>
              <ul class="bento-features" style="margin-top: 12px;">
                <li>12 profils métiers pré-configurés en 1 clic</li>
                <li>Numéro de rôle d'offre personnalisable</li>
                <li>Export PDF 1 page avec couleur de colonne garantie</li>
              </ul>
            </div>
            <a href="editeur_cv.html" class="btn btn-primary btn-sm">
              Ouvrir l'Éditeur de CV
            </a>
          </div>

          <div class="bento-card">
            <div>
              <div class="bento-title">
                <h4>Éditeur de Lettre de Motivation</h4>
                <p>Génération sur-mesure pour chaque annonce</p>
              </div>
              <ul class="bento-features" style="margin-top: 12px;">
                <li>Injection automatique de l'objet et référence</li>
                <li>Modèles prêts pour tutorat, retail, tech</li>
                <li>Export PDF officiel ou copie de texte en 1 clic</li>
              </ul>
            </div>
            <a href="editeur_lettre_motivation.html" class="btn btn-primary btn-sm">
              Ouvrir l'Éditeur de Lettre
            </a>
          </div>
        </div>
      </section>

      <!-- DOSSIERS CIBLES / JOBS ETUDIANTS -->
      <section class="content-section">
        <div class="section-header-block">
          <h2 class="section-title">Candidatures Dédiées & Jobs Étudiants</h2>
          <span class="section-desc">Dossiers ciblés prêts à l'envoi</span>
        </div>

        <div class="private-docs-list">

          <!-- SOUTIEN SCOLAIRE -->
          <div class="private-doc-item">
            <div class="doc-info-col">
              <span class="private-doc-title">Soutien Scolaire & Tutorat (Maths / Sciences)</span>
              <span class="private-doc-sub">Acadomia, Complétude, familles</span>
            </div>
            <div style="display: flex; gap: 6px;">
              <a href="CV_Rodrigue_HESSOU_Soutien_Scolaire.pdf" target="_blank" class="btn btn-secondary btn-sm">CV</a>
              <a href="Lettre_de_Motivation_Soutien_Scolaire_Rodrigue_HESSOU.pdf" target="_blank" class="btn btn-secondary btn-sm">Lettre</a>
              <a href="editeur_cv.html?preset=soutien_scolaire" class="btn btn-primary btn-sm">Éditer</a>
            </div>
          </div>

          <!-- MCDONALDS -->
          <div class="private-doc-item">
            <div class="doc-info-col">
              <span class="private-doc-title">McDonald's Lyon (Équipier Polyvalent)</span>
              <span class="private-doc-sub">Caisse, bornes, Drive, rush & HACCP</span>
            </div>
            <div style="display: flex; gap: 6px;">
              <a href="CV_Rodrigue_HESSOU_Restauration_MacDo.pdf" target="_blank" class="btn btn-secondary btn-sm">CV</a>
              <a href="Lettre_de_Motivation_MacDo_Rodrigue_HESSOU.pdf" target="_blank" class="btn btn-secondary btn-sm">Lettre</a>
              <a href="editeur_cv.html?preset=macdo" class="btn btn-primary btn-sm">Éditer</a>
            </div>
          </div>

          <!-- APPLE STORE -->
          <div class="private-doc-item">
            <div class="doc-info-col">
              <span class="private-doc-title">Apple Store Lyon (Spécialiste #114438069)</span>
              <span class="private-doc-sub">Part-Dieu / Confluence · Product Zone</span>
            </div>
            <div style="display: flex; gap: 6px;">
              <a href="CV_Rodrigue_HESSOU_Apple_Retail.pdf" target="_blank" class="btn btn-secondary btn-sm">CV</a>
              <a href="Lettre_de_Motivation_Apple_Retail_Rodrigue_HESSOU.pdf" target="_blank" class="btn btn-secondary btn-sm">Lettre</a>
              <a href="editeur_cv.html?preset=apple_part_time" class="btn btn-primary btn-sm">Éditer</a>
            </div>
          </div>

          <!-- ADIDAS -->
          <div class="private-doc-item">
            <div class="doc-info-col">
              <span class="private-doc-title">adidas Lyon Part-Dieu (Vendeur CDI 35H)</span>
              <span class="private-doc-sub">Vente conseil, KPIs retail & encaissement</span>
            </div>
            <div style="display: flex; gap: 6px;">
              <a href="CV_Rodrigue_HESSOU_Retail_Polyvalent.pdf" target="_blank" class="btn btn-secondary btn-sm">CV</a>
              <a href="Lettre_de_Motivation_Adidas_Rodrigue_HESSOU.pdf" target="_blank" class="btn btn-secondary btn-sm">Lettre</a>
              <a href="editeur_cv.html?preset=adidas_part_dieu" class="btn btn-primary btn-sm">Éditer</a>
            </div>
          </div>

          <!-- RETAIL GENERAL -->
          <div class="private-doc-item">
            <div class="doc-info-col">
              <span class="private-doc-title">Retail & Vente Polyvalente Générale</span>
              <span class="private-doc-sub">Sephora, Hermès, grandes enseignes</span>
            </div>
            <div style="display: flex; gap: 6px;">
              <a href="CV_Rodrigue_HESSOU_Retail_Polyvalent.pdf" target="_blank" class="btn btn-secondary btn-sm">CV</a>
              <a href="Lettre_de_Motivation_Retail_Polyvalent.pdf" target="_blank" class="btn btn-secondary btn-sm">Lettre</a>
              <a href="editeur_cv.html?preset=retail_general" class="btn btn-primary btn-sm">Éditer</a>
            </div>
          </div>

          <!-- CAPGEMINI LYON -->
          <div class="private-doc-item">
            <div class="doc-info-col">
              <span class="private-doc-title">Capgemini France (Lyon 7e)</span>
              <span class="private-doc-sub">Offre Dév. Java / Back-End & PLM</span>
            </div>
            <div style="display: flex; gap: 6px;">
              <a href="CV_Rodrigue_HESSOU.pdf" target="_blank" class="btn btn-secondary btn-sm">CV</a>
              <a href="Lettre_de_Motivation_Rodrigue_HESSOU.pdf" target="_blank" class="btn btn-secondary btn-sm">Lettre</a>
              <a href="editeur_lettre_motivation.html?preset=capgemini_stage" class="btn btn-primary btn-sm">Éditer</a>
            </div>
          </div>

        </div>
      </section>
    </div>

    <!-- FOOTER -->
    <footer class="site-footer">
      <div class="footer-top-row">
        <div>
          <strong style="color: var(--text-primary); font-size: 13.5px;">Rodrigue HESSOU</strong>
          <p style="margin-top: 2px;">Étudiant Master 1 en Informatique / SUPINFO Lyon</p>
        </div>

        <ul class="footer-links">
          <li><a href="#overview">Accueil</a></li>
          <li><a href="#candidatures">Candidatures</a></li>
          <li><a href="#experience">Expérience</a></li>
          <li><a href="#projets">Projets</a></li>
          <li><a href="https://github.com/RoHsk14" target="_blank">GitHub</a></li>
          <li><a href="mailto:rodriguehessou14@gmail.com">Contact</a></li>
        </ul>
      </div>

      <div class="footer-bottom-row">
        <div>
          Conçu avec précision • Déployé sur Vercel
        </div>
        <div>
          Copyright 2026 Rodrigue HESSOU. Tous droits réservés.
        </div>
      </div>
    </footer>

  </div>

  <!-- COMMAND PALETTE (NATIVE <dialog> MODAL) -->
  <dialog id="cmd-dialog" closedby="any" aria-label="Palette de commandes">
    <div class="cmd-box">
      <div class="cmd-input-row">
        <svg class="icon-svg" style="color: var(--text-muted);" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="text" class="cmd-search-input" id="cmd-search" placeholder="Rechercher une section, un document ou une action..." oninput="filterCmdList(this.value)">
        <kbd class="cmd-shortcut-badge" style="cursor: pointer;" onclick="closeCmdPalette()">ESC</kbd>
      </div>

      <ul class="cmd-results-list" id="cmd-list">
        <!-- NAVIGATION -->
        <li class="cmd-category-header">Navigation Publique</li>
        <li><a class="cmd-item" href="#candidatures" onclick="closeCmdPalette()"><span class="cmd-item-left">Candidatures Techniques (Stage & Alternance)</span><span class="cmd-item-badge">Section</span></a></li>
        <li><a class="cmd-item" href="#experience" onclick="closeCmdPalette()"><span class="cmd-item-left">Parcours & Expérience</span><span class="cmd-item-badge">Timeline</span></a></li>
        <li><a class="cmd-item" href="#projets" onclick="closeCmdPalette()"><span class="cmd-item-left">Projets & Réalisations Techniques</span><span class="cmd-item-badge">Code</span></a></li>
        <li><a class="cmd-item" href="#competences" onclick="closeCmdPalette()"><span class="cmd-item-left">Stack Technique</span><span class="cmd-item-badge">Skills</span></a></li>
        <li><a class="cmd-item" href="#formation" onclick="closeCmdPalette()"><span class="cmd-item-left">Formation Académique</span><span class="cmd-item-badge">Diplômes</span></a></li>

        <!-- DOCUMENTS PUBLICS -->
        <li class="cmd-category-header">Documents Techniques Généraux</li>
        <li><a class="cmd-item" href="CV_Rodrigue_HESSOU_Stage_Tech.pdf" target="_blank"><span class="cmd-item-left">CV Développeur Logiciel (Stage Bac+5)</span><span class="cmd-item-badge">PDF</span></a></li>
        <li><a class="cmd-item" href="Lettre_de_Motivation_Stage_Tech_Rodrigue_HESSOU.pdf" target="_blank"><span class="cmd-item-left">Lettre de Motivation Développeur Logiciel (Stage)</span><span class="cmd-item-badge">PDF</span></a></li>
        <li><a class="cmd-item" href="CV_Rodrigue_HESSOU_Alternance_Tech.pdf" target="_blank"><span class="cmd-item-left">CV Développeur Logiciel (Alternance Bac+5)</span><span class="cmd-item-badge">PDF</span></a></li>
        <li><a class="cmd-item" href="Lettre_de_Motivation_Alternance_Tech_Rodrigue_HESSOU.pdf" target="_blank"><span class="cmd-item-left">Lettre de Motivation Développeur Logiciel (Alternance)</span><span class="cmd-item-badge">PDF</span></a></li>

        <!-- ACTIONS -->
        <li class="cmd-category-header">Actions Rapides</li>
        <li><div class="cmd-item" onclick="copyContact('rodriguehessou14@gmail.com', 'Email copié dans le presse-papier'); closeCmdPalette();"><span class="cmd-item-left">Copier l'Email (rodriguehessou14@gmail.com)</span><span class="cmd-item-badge">Copier</span></div></li>
        <li><div class="cmd-item" onclick="copyContact('+33 7 44 11 75 73', 'Téléphone copié dans le presse-papier'); closeCmdPalette();"><span class="cmd-item-left">Copier le Téléphone (+33 7 44 11 75 73)</span><span class="cmd-item-badge">Copier</span></div></li>
        <li><div class="cmd-item" onclick="toggleTheme(); closeCmdPalette();"><span class="cmd-item-left">Basculer le Thème (Clair / Sombre)</span><span class="cmd-item-badge">Thème</span></div></li>
        <li id="cmd-login-item"><div class="cmd-item" onclick="openLoginModal(); closeCmdPalette();"><span class="cmd-item-left">Connexion Espace Interne (Rodrigue)</span><span class="cmd-item-badge">Auth</span></div></li>
      </ul>

      <div class="cmd-footer-bar">
        <span>Navigation : Flèches haut/bas</span>
        <span>Validation : Entrée</span>
      </div>
    </div>
  </dialog>

  <!-- LOGIN MODAL DIALOG -->
  <dialog id="login-modal" closedby="any" aria-label="Connexion à l'espace interne">
    <div class="login-card">
      <div class="login-header">
        <h3>Espace Interne Réservé</h3>
        <p>Veuillez saisir votre mot de passe d'accès pour déverrouiller vos dossiers.</p>
      </div>

      <form onsubmit="handleLoginSubmit(event)">
        <div class="login-form-group">
          <label for="login-pwd">Mot de passe</label>
          <input type="password" id="login-pwd" class="login-input" placeholder="Mot de passe d'accès..." autofocus required>
          <span class="login-error-msg" id="login-error">Mot de passe incorrect. Veuillez réessayer.</span>
        </div>

        <div class="login-actions" style="margin-top: 16px;">
          <button type="button" class="btn btn-secondary btn-sm" onclick="closeLoginModal()">Annuler</button>
          <button type="submit" class="btn btn-primary btn-sm">Se connecter</button>
        </div>
      </form>
    </div>
  </dialog>

  <!-- TOAST FEEDBACK -->
  <div class="toast" id="toast">Copié dans le presse-papier</div>

  <!-- JAVASCRIPT -->
  <script>
    // THEME HANDLING
    function initTheme() {
      const saved = localStorage.getItem('theme');
      if (saved) {
        document.documentElement.setAttribute('data-theme', saved);
        updateThemeIcon(saved);
      } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
        document.documentElement.setAttribute('data-theme', 'light');
        updateThemeIcon('light');
      }
    }

    function toggleTheme() {
      const cur = document.documentElement.getAttribute('data-theme');
      const next = cur === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      updateThemeIcon(next);
      showToast(next === 'light' ? 'Mode Clair activé' : 'Mode Sombre activé');
    }

    function updateThemeIcon(theme) {
      const icon = document.getElementById('theme-icon');
      if (icon) {
        if (theme === 'light') {
          // Sun SVG
          icon.innerHTML = '<circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>';
        } else {
          // Moon SVG
          icon.innerHTML = '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>';
        }
      }
    }

    initTheme();

    // AUTHENTICATION & PRIVATE DASHBOARD
    function checkAuth() {
      const isAuth = localStorage.getItem('rodrigue_auth') === 'true';
      const dashboard = document.getElementById('private-dashboard');
      const navBtn = document.getElementById('nav-auth-btn');
      const navText = document.getElementById('nav-auth-text');
      const ctaSection = document.getElementById('auth-cta-section');
      const cmdLoginItem = document.getElementById('cmd-login-item');

      if (isAuth) {
        dashboard.classList.add('authenticated');
        navBtn.classList.add('authenticated');
        navText.innerText = 'Espace Connecté';
        ctaSection.style.display = 'none';
        if (cmdLoginItem) {
          cmdLoginItem.innerHTML = '<div class="cmd-item" onclick="logout(); closeCmdPalette();"><span class="cmd-item-left">Déconnexion de l\'Espace Interne</span><span class="cmd-item-badge">Auth</span></div>';
        }
      } else {
        dashboard.classList.remove('authenticated');
        navBtn.classList.remove('authenticated');
        navText.innerText = 'Connexion';
        ctaSection.style.display = 'block';
        if (cmdLoginItem) {
          cmdLoginItem.innerHTML = '<div class="cmd-item" onclick="openLoginModal(); closeCmdPalette();"><span class="cmd-item-left">Connexion Espace Interne (Rodrigue)</span><span class="cmd-item-badge">Auth</span></div>';
        }
      }
    }

    function handleAuthNavClick() {
      const isAuth = localStorage.getItem('rodrigue_auth') === 'true';
      if (isAuth) {
        document.getElementById('private-dashboard').scrollIntoView({ behavior: 'smooth' });
      } else {
        openLoginModal();
      }
    }

    function openLoginModal() {
      const m = document.getElementById('login-modal');
      const err = document.getElementById('login-error');
      const pwd = document.getElementById('login-pwd');
      err.style.display = 'none';
      pwd.value = '';
      if (m.showModal) {
        m.showModal();
        setTimeout(() => pwd.focus(), 50);
      }
    }

    function closeLoginModal() {
      document.getElementById('login-modal').close();
    }

    function handleLoginSubmit(e) {
      e.preventDefault();
      const pwd = document.getElementById('login-pwd').value.trim();
      const err = document.getElementById('login-error');

      // Valid passwords
      if (pwd === 'rodrigue' || pwd === 'rodrigue2026' || pwd === 'admin') {
        localStorage.setItem('rodrigue_auth', 'true');
        checkAuth();
        closeLoginModal();
        showToast('Connexion réussie : Espace interne déverrouillé');
        setTimeout(() => {
          document.getElementById('private-dashboard').scrollIntoView({ behavior: 'smooth' });
        }, 150);
      } else {
        err.style.display = 'block';
      }
    }

    function logout() {
      localStorage.removeItem('rodrigue_auth');
      checkAuth();
      showToast('Déconnexion effectuée');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    checkAuth();

    // COPY TO CLIPBOARD
    function copyContact(text, msg) {
      navigator.clipboard.writeText(text).then(() => {
        showToast(msg || 'Copié dans le presse-papier');
      }).catch(() => {
        showToast('Erreur de copie');
      });
    }

    function showToast(msg) {
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2600);
    }

    // COMMAND PALETTE
    const cmdDialog = document.getElementById('cmd-dialog');
    const cmdSearch = document.getElementById('cmd-search');

    function openCmdPalette() {
      if (cmdDialog.showModal) {
        cmdDialog.showModal();
        cmdSearch.value = '';
        filterCmdList('');
        setTimeout(() => cmdSearch.focus(), 50);
      }
    }

    function closeCmdPalette() {
      cmdDialog.close();
    }

    window.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        if (cmdDialog.open) {
          closeCmdPalette();
        } else {
          openCmdPalette();
        }
      }
    });

    function filterCmdList(query) {
      const q = query.toLowerCase().trim();
      const items = document.querySelectorAll('.cmd-results-list li');
      items.forEach(li => {
        if (li.classList.contains('cmd-category-header')) {
          li.style.display = q === '' ? 'block' : 'none';
          return;
        }
        const text = li.innerText.toLowerCase();
        if (q === '' || text.includes(q)) {
          li.style.display = 'block';
        } else {
          li.style.display = 'none';
        }
      });
    }

    // LIGHT DISMISS FALLBACK FOR SAFARI
    if (!('closedBy' in HTMLDialogElement.prototype)) {
      const outside = (e, dialog) => {
        const r = dialog.getBoundingClientRect();
        return e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom;
      };
      let pressedOutside = false;
      cmdDialog.addEventListener('pointerdown', (e) => { pressedOutside = outside(e, cmdDialog); });
      cmdDialog.addEventListener('pointerup', (e) => { if (pressedOutside && outside(e, cmdDialog)) cmdDialog.close(); });

      const loginModal = document.getElementById('login-modal');
      let loginPressedOutside = false;
      loginModal.addEventListener('pointerdown', (e) => { loginPressedOutside = outside(e, loginModal); });
      loginModal.addEventListener('pointerup', (e) => { if (loginPressedOutside && outside(e, loginModal)) loginModal.close(); });
    }
  </script>

</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html successfully.")
