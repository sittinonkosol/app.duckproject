(() => {
    const words = [...document.querySelectorAll('[data-typewriter-word]')];
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    if (words.length !== 2 || motion.matches) return;
    const labels = words.map(word => word.textContent);
    const cursors = words.map(word => word.nextElementSibling);
    let timer;
    const finish = () => {
        clearTimeout(timer);
        words.forEach((word, index) => { word.textContent = labels[index]; });
        cursors.forEach((cursor, index) => { cursor.hidden = index !== words.length - 1; });
    };
    motion.addEventListener('change', event => { if (event.matches) finish(); });
    words.forEach(word => { word.textContent = ''; });
    cursors.forEach((cursor, index) => { cursor.hidden = index !== 0; });
    let line = 0;
    let character = 0;
    const type = () => {
        if (motion.matches) { finish(); return; }
        words[line].textContent = labels[line].slice(0, ++character);
        if (character < labels[line].length) {
            timer = setTimeout(type, 120);
        } else if (line < words.length - 1) {
            timer = setTimeout(() => {
                cursors[line].hidden = true;
                line += 1;
                character = 0;
                cursors[line].hidden = false;
                type();
            }, 260);
        }
    };
    timer = setTimeout(type, 250);
})();
