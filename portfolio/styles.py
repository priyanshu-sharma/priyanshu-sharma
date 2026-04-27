CSS = """
:root {
  --background: #000000;
  --foreground: hsl(210 40% 98%);
  --muted: #0f1117;
  --muted-foreground: #9ea9b8;
  --card: #07090f;
  --border: #232838;
  --primary: #e8eefc;
  --primary-foreground: #0f1726;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--background); color: var(--foreground); font-family: "FiraCode Nerd Font Retina", "FiraCode Nerd Font", "Fira Code Retina", "Fira Code", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace; line-height: 1.5; }
h1, h2, h3, h4, h5, h6 { font-family: "SF Pro Text", "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
p, a, button, span, strong, div { font-family: "FiraCode Nerd Font Retina", "FiraCode Nerd Font", "Fira Code Retina", "Fira Code", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace; }
.container { max-width: 960px; margin: 0 auto; min-height: 100vh; padding: 2.5rem 1rem; }
.header { display: flex; justify-content: space-between; align-items: center; gap: 1rem; padding-bottom: 1rem; border-bottom: 1px solid var(--border); margin-bottom: 2rem; }
.profile { display: flex; align-items: center; gap: 0.75rem; }
.avatar { width: 40px; height: 40px; border-radius: 999px; border: 1px solid var(--border); background: var(--muted); }
.muted { color: var(--muted-foreground); }
.nav { display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap; }
.h1 { margin: 0; font-size: 1.1rem; font-weight: 600; }
.btn { display: inline-flex; align-items: center; justify-content: center; height: 36px; padding: 0 14px; border-radius: 6px; border: 1px solid var(--border); background: var(--card); color: var(--foreground); text-decoration: none; font-size: 0.875rem; font-weight: 500; }
.btn-primary { background: var(--primary); border-color: var(--primary); color: var(--primary-foreground); }
.card { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.02) inset; }
.section { margin-bottom: 1.5rem; }
.title { margin: 0 0 0.35rem; font-size: 1.65rem; font-weight: 700; letter-spacing: -0.01em; }
.subtitle { margin: 0; font-size: 0.95rem; }
.badge-row { margin-top: 1rem; display: flex; flex-wrap: wrap; gap: 0.45rem; }
.badge { display: inline-flex; align-items: center; border: 1px solid var(--border); border-radius: 6px; background: var(--muted); padding: 0.22rem 0.55rem; font-size: 0.74rem; font-weight: 500; }
.section-label { margin: 0 0 0.75rem; font-size: 1rem; font-weight: 600; }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 0.85rem; }
.metric-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.75rem; }
.metric { border: 1px solid var(--border); border-radius: 6px; background: var(--muted); padding: 0.75rem; }
.metric strong { font-size: 1.1rem; }
.footer { border-top: 1px solid var(--border); padding-top: 1.25rem; }
.btn-row { margin-top: 0.8rem; display: flex; flex-wrap: wrap; gap: 0.6rem; }
@media (max-width: 760px) { .grid-2, .metric-grid { grid-template-columns: 1fr; } }
"""
