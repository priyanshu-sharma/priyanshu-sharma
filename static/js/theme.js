function applyTheme(isDark) {
    document.body.classList.toggle('light-mode', !isDark);
    const themeToggle = document.querySelector('.theme-toggle');
    if (themeToggle) themeToggle.innerText = isDark ? '🌙' : '☀️';
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
}

function toggleTheme() {
    const isCurrentlyDark = !document.body.classList.contains('light-mode');
    applyTheme(!isCurrentlyDark);
}

const savedTheme = localStorage.getItem('theme') || 'dark';
applyTheme(savedTheme === 'dark');
