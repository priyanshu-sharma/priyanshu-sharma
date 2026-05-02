CSS = """
:root {
  --background: #09090b;
  --foreground: #fafafa;
  --muted: rgba(24, 24, 27, 0.5);
  --muted-foreground: #a1a1aa;
  --card: rgba(15, 15, 18, 0.6);
  --card-foreground: #fafafa;
  --border: rgba(255, 255, 255, 0.08);
  --primary: #ffffff;
  --primary-foreground: #09090b;
  --accent: rgba(39, 39, 42, 0.5);
  --accent-foreground: #fafafa;
  --radius: 0.75rem;
  --glass-blur: 12px;
  
  --accent-yellow: #F3B841;
  --accent-purple: #6D20E5;
  --accent-green: #60B77E;
  --accent-blue: #58BEE1;
  --accent-orange: #C56D40;
}

/* Light Mode Variables */
body.light-mode {
    --background: #f8fafc;
    --foreground: #0f172a;
    --muted: rgba(241, 245, 249, 0.6);
    --muted-foreground: #64748b;
    --card: rgba(255, 255, 255, 0.7);
    --border: rgba(0, 0, 0, 0.06);
    --primary: #0f172a;
    --primary-foreground: #ffffff;
    --accent: rgba(241, 245, 249, 0.8);
    --accent-foreground: #0f172a;
}

* { box-sizing: border-box; }

body { 
    margin: 0; 
    background: var(--background); 
    color: var(--foreground); 
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 1rem;
    line-height: 1.7;
    -webkit-font-smoothing: antialiased;
    transition: background-color 0.3s ease, color 0.3s ease;
    min-height: 100vh;
    overflow-x: hidden;
}

/* Grain Texture */
body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0.03;
    z-index: 1000;
    pointer-events: none;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3%3Ffilter id='noiseFilter'%3E%3FfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3F/filter%3E%3Frect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3F/svg%3E");
}

body.light-mode::before {
    opacity: 0.02;
}

/* Background Decorative Elements */
.bg-blobs {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: -1;
    overflow: hidden;
    pointer-events: none;
}

.blob {
    position: absolute;
    width: 500px;
    height: 500px;
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(45, 212, 191, 0.15) 100%);
    filter: blur(80px);
    border-radius: 50%;
    animation: float 20s infinite alternate;
}

.blob-1 { top: -100px; right: -100px; }
.blob-2 { bottom: -100px; left: -100px; animation-delay: -10s; }

@keyframes float {
    from { transform: translate(0, 0) scale(1); }
    to { transform: translate(100px, 50px) scale(1.1); }
}

h1, h2, h3, h4, h5, h6 { 
    font-family: "Inter", sans-serif; 
    font-weight: 600;
    letter-spacing: -0.02em;
    color: var(--foreground);
    transition: color 0.3s ease;
    text-wrap: balance;
}

/* Focus States for Accessibility */
:focus-visible {
    outline: 2px solid var(--primary);
    outline-offset: 2px;
    border-radius: var(--radius);
}

/* Animated Links */
a:not(.btn) {
    color: var(--foreground);
    text-decoration: none;
    position: relative;
    background-image: linear-gradient(currentColor, currentColor);
    background-position: 0% 100%;
    background-repeat: no-repeat;
    background-size: 0% 1px;
    transition: background-size 0.3s;
}

a:not(.btn):hover {
    background-size: 100% 1px;
}

.container { 
    max-width: 700px; 
    margin: 0 auto; 
    padding: 4rem 1.5rem; 
    position: relative;
}

.header { 
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3.5rem; 
    background: transparent !important;
    border: none !important;
}

.avatar { 
    width: 48px; 
    height: 48px; 
    border-radius: 50%; 
    background: linear-gradient(135deg, #3b82f6 0%, #2dd4bf 100%);
    border: 2px solid var(--border);
    transition: transform 0.3s ease, border-color 0.3s ease;
}

.avatar:hover {
    transform: scale(1.05) rotate(5deg);
}

.theme-toggle { 
    background: var(--card); 
    backdrop-filter: blur(var(--glass-blur));
    -webkit-backdrop-filter: blur(var(--glass-blur));
    border: 1px solid var(--border); 
    border-radius: var(--radius); 
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer; 
    color: var(--foreground);
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.theme-toggle:hover {
    background: var(--accent);
    transform: rotate(20deg) scale(1.1);
}

.header-nav { 
    margin-bottom: 4rem; 
}

.nav { 
    display: flex; 
    gap: 0.5rem; 
    flex-wrap: wrap;
    background: var(--card);
    padding: 0.4rem;
    border-radius: calc(var(--radius) + 0.25rem);
    border: 1px solid var(--border);
    backdrop-filter: blur(var(--glass-blur));
    -webkit-backdrop-filter: blur(var(--glass-blur));
    width: max-content;
    position: relative;
}

.nav-indicator {
    position: absolute;
    bottom: -2px;
    height: 2px;
    background: var(--primary);
    transition: all 0.3s ease;
}

.btn { 
    display: inline-flex; 
    align-items: center; 
    justify-content: center; 
    height: 2.25rem; 
    padding: 0 1rem; 
    border-radius: var(--radius); 
    font-size: 0.875rem; 
    font-weight: 500; 
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    text-decoration: none;
    background: transparent;
    color: var(--muted-foreground);
    border: 1px solid transparent;
    cursor: pointer;
}

.btn:active {
    transform: scale(0.98);
}

.btn:hover {
    background: var(--accent);
    color: var(--foreground);
}

.btn-primary { 
    background: var(--accent); 
    color: var(--foreground); 
    border-color: var(--border);
    box-shadow: 0 1px 2px rgba(0,0,0,0.1);
}

.btn-primary:hover {
    background: var(--primary);
    color: var(--primary-foreground);
    opacity: 1;
}

.card { 
    background: var(--card); 
    backdrop-filter: blur(var(--glass-blur)) saturate(180%);
    -webkit-backdrop-filter: blur(var(--glass-blur)) saturate(180%);
    border: 1px solid var(--border); 
    border-radius: 20px; 
    padding: 2rem; 
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.card:hover { 
    border-color: rgba(255, 255, 255, 0.2); 
    transform: translateY(-4px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.bento-card h3 {
    margin: 0;
    font-size: 0.85rem;
    color: var(--muted-foreground);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 700;
}

.experience-card h3 {
    font-size: 0.75rem;
}

.card h3 {
    margin: 0;
    font-size: 0.95rem;
    color: var(--muted-foreground);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 700;
}


.card h4 {
    margin: 0;
    font-size: 1.35rem;
    font-weight: 600;
    color: var(--foreground);
}

.card p {
    margin: 0;
    font-size: 1rem;
    line-height: 1.5;
    color: var(--foreground);
}

body.light-mode .card:hover {
    border-color: rgba(0, 0, 0, 0.1);
}

/* Enhanced Bento Grid System */
.top-row {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
}

.top-row > .bento-card {
    flex: 1;
}

.bento-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
}

.bento-card {
    background: var(--card);
    backdrop-filter: blur(var(--glass-blur));
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.bento-card:hover { 
    border-color: rgba(255, 255, 255, 0.2); 
    transform: translateY(-4px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.bento-card h3 {
    margin: 0;
    font-size: 1.1rem;
    color: var(--muted-foreground);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.bento-card p {
    margin: 0;
    font-size: 1.2rem;
    line-height: 1.4;
    font-weight: 500;
}

.bento-card.span-2 { grid-column: span 2; }
.bento-card.row-span-2 { grid-row: span 2; }

.section { 
    margin-bottom: 3.5rem; 
    animation: fadeIn 0.5s ease-out forwards;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

Main {
    animation: fadeIn 0.4s ease-out forwards;
}

.title { 
    margin: 0 0 0.75rem; 
    font-size: 2.25rem; 
    line-height: 1.1;
    font-weight: 700;
}

.subtitle { 
    margin: 0; 
    font-size: 1.125rem; 
    color: var(--muted-foreground); 
}

.muted { color: var(--muted-foreground); }

.btn-row { 
    margin-top: 1.5rem; 
    display: flex; 
    flex-wrap: wrap; 
    gap: 1rem; 
}

.badge-row {
    margin-top: 1.5rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
}

.badge { 
    display: inline-flex;
    align-items: center; 
    border-radius: 9999px;
    background: var(--muted); 
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    padding: 0.25rem 0.75rem; 
    font-size: 0.75rem; 
    font-weight: 500; 
    color: var(--foreground);
    border: 1px solid var(--border);
    transition: all 0.2s ease;
}

.badge:hover {
    background: var(--accent);
    border-color: var(--muted-foreground);
}

.section-label { 
    margin: 0 0 1.25rem; 
    font-size: 0.75rem; 
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 700;
    color: var(--muted-foreground);
}

.grid-2 { 
    display: grid; 
    grid-template-columns: 1fr 1fr; 
    gap: 1.5rem; 
}

@media (max-width: 640px) {
    .grid-2 { grid-template-columns: 1fr; }
    .bento-card.span-2 { grid-column: span 1; }
}

.metric-grid { 
    display: grid; 
    grid-template-columns: repeat(3, 1fr); 
    gap: 1rem; 
}

.metric { 
    border: 1px solid var(--border); 
    border-radius: var(--radius); 
    padding: 1.25rem; 
    text-align: center;
    transition: all 0.3s ease;
    background: var(--card);
    backdrop-filter: blur(var(--glass-blur));
    -webkit-backdrop-filter: blur(var(--glass-blur));
}

.metric:hover {
    border-color: rgba(255, 255, 255, 0.2);
    transform: translateY(-2px);
}

.metric strong { 
    display: block;
    font-size: 1.5rem; 
    font-weight: 700;
    margin-bottom: 0.25rem;
}

.copy-btn {
    cursor: pointer;
    background: var(--muted);
    border: 1px solid var(--border);
    font-size: 0.75rem;
    color: var(--foreground);
    padding: 0.25rem 0.6rem;
    border-radius: 6px;
    transition: all 0.2s ease;
    font-weight: 500;
}

.copy-btn:hover {
    background: var(--accent);
}

.footer { 
    margin-top: 5rem;
    padding: 2rem; 
    border-radius: var(--radius);
    background: var(--card);
    backdrop-filter: blur(var(--glass-blur));
    -webkit-backdrop-filter: blur(var(--glass-blur));
    border: 1px solid var(--border);
}

/* Skeleton loader */
.skeleton {
    background: linear-gradient(90deg, var(--muted) 25%, var(--accent) 50%, var(--muted) 75%);
    background-size: 200% 100%;
    animation: loading 1.5s infinite;
}

@keyframes loading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

@media (max-width: 640px) { 
    .metric-grid { grid-template-columns: 1fr; } 
    .header { flex-direction: column; align-items: flex-start; gap: 1.5rem; }
    .header-right { align-self: flex-end; }
}
"""
