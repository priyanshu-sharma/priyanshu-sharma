CSS = """
:root {
  --background: #09090b;
  --foreground: #fafafa;
  --muted: #18181b;
  --muted-foreground: #a1a1aa;
  --card: #09090b;
  --card-foreground: #fafafa;
  --border: #27272a;
  --primary: #ffffff;
  --primary-foreground: #09090b;
  --accent: #27272a;
  --accent-foreground: #fafafa;
  --radius: 0.5rem;
}

/* Light Mode Variables */
body.light-mode {
    --background: #ffffff;
    --foreground: #09090b;
    --muted: #f4f4f5;
    --muted-foreground: #71717a;
    --card: #ffffff;
    --border: #e4e4e7;
    --primary: #09090b;
    --primary-foreground: #ffffff;
    --accent: #f4f4f5;
    --accent-foreground: #09090b;
}

* { box-sizing: border-box; }

body { 
    margin: 0; 
    background: var(--background); 
    color: var(--foreground); 
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.6; 
    -webkit-font-smoothing: antialiased;
    transition: background-color 0.3s ease, color 0.3s ease;
}

h1, h2, h3, h4, h5, h6 { 
    font-family: "Inter", sans-serif; 
    font-weight: 600;
    letter-spacing: -0.02em;
    color: var(--foreground);
    transition: color 0.3s ease;
}

.container { 
    max-width: 700px; 
    margin: 0 auto; 
    padding: 4rem 1.5rem; 
}

.header { 
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3.5rem; 
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
    background: transparent; 
    border: 1px solid var(--border); 
    border-radius: var(--radius); 
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer; 
    color: var(--foreground);
    transition: all 0.2s ease;
}

.theme-toggle:hover {
    background: var(--accent);
    transform: translateY(-2px);
}

.header-nav { 
    margin-bottom: 4rem; 
}

.nav { 
    display: flex; 
    gap: 0.5rem; 
    flex-wrap: wrap; 
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
    color: var(--foreground);
    border: 1px solid transparent;
}

.btn:hover {
    background: var(--muted);
    border-color: var(--muted-foreground);
    color: var(--foreground);
    transform: translateY(-1px);
}

.btn-primary { 
    background: var(--primary); 
    color: var(--primary-foreground); 
    box-shadow: 0 1px 2px rgba(0,0,0,0.1);
}

.btn-primary:hover {
    background: var(--foreground);
    color: var(--background);
    opacity: 1;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.card { 
    background: var(--card); 
    border: 1px solid var(--border); 
    border-radius: var(--radius); 
    padding: 1.5rem; 
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.card:hover { 
    border-color: var(--muted-foreground); 
    transform: translateY(-4px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.section { 
    margin-bottom: 3.5rem; 
    animation: fadeIn 0.5s ease-out forwards;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
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
    background: var(--muted);
}

.metric:hover {
    border-color: var(--muted-foreground);
    background: var(--card);
}

.metric strong { 
    display: block;
    font-size: 1.5rem; 
    font-weight: 700;
    margin-bottom: 0.25rem;
}

.footer { 
    margin-top: 5rem;
    border-top: 1px solid var(--border); 
    padding: 3rem 0; 
}

@media (max-width: 640px) { 
    .metric-grid { grid-template-columns: 1fr; } 
    .header { flex-direction: column; align-items: flex-start; gap: 1.5rem; }
    .header-right { align-self: flex-end; }
}
"""
