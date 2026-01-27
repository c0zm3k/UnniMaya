// Main JS - Futuristic Effects

document.addEventListener('DOMContentLoaded', () => {
    console.log('System Initialized...');

    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
            const icon = mobileMenuBtn.querySelector('i');
            if (icon.classList.contains('bi-list')) {
                icon.classList.remove('bi-list');
                icon.classList.add('bi-x');
            } else {
                icon.classList.remove('bi-x');
                icon.classList.add('bi-list');
            }
        });
    }

    // Add glitch effect or other interactions here if needed
    const inputs = document.querySelectorAll('.form-control');

    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            playHoverSound();
        });
    });
});

function playHoverSound() {
    // Placeholder for UI sounds
    // const audio = new Audio('/static/sounds/hover.mp3');
    // audio.play().catch(e => console.log('Audio require interaction'));
}
