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

document.addEventListener('DOMContentLoaded', () => {
    const nav = document.querySelector('.nav');
    const indicator = document.querySelector('.nav-indicator');
    const activeLink = nav.querySelector('.btn-primary');

    if (indicator && activeLink) {
        function moveIndicator(el) {
            indicator.style.width = `${el.offsetWidth}px`;
            indicator.style.left = `${el.offsetLeft}px`;
        }
        
        moveIndicator(activeLink);

        nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('mouseenter', () => moveIndicator(link));
            link.addEventListener('mouseleave', () => moveIndicator(activeLink));
        });
    }
});
