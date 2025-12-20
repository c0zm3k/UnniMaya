// Main JS - Futuristic Effects

document.addEventListener('DOMContentLoaded', () => {
    console.log('System Initialized...');

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
