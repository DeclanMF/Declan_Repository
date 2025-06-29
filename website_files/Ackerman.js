document.querySelector('.nav-links').addEventListener('mouseenter', () => {
        navButton.textContent = 'Explore';
    });

document.querySelector('#nav-button').addEventListener('mouseleave', () => {
        navButton.textContent  = 'Navigate';
    });
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (scroll) {
        scroll.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});