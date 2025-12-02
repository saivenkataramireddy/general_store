document.addEventListener("DOMContentLoaded", () => {
    const splash = document.querySelector(".splash");
    const splashText = document.getElementById("splash-text");
    const splashLogo = document.getElementById("splash-logo");

    const text = "WELCOME TO SJMS STORES";
    let index = 0;

    function typeEffect() {
        if (index < text.length) {
            splashText.innerHTML += text[index];
            index++;
            setTimeout(typeEffect, 100); // typing speed
        } else {
            // Show Logo after text completes
            setTimeout(() => {
                splashLogo.style.opacity = "1";
            }, 500);

            // Fade splash and hide completely
            setTimeout(() => {
                splash.style.opacity = "0";
                splash.style.transition = "1s ease-in-out";
                setTimeout(() => splash.style.display = "none", 1000);
            }, 2500);
        }
    }

    typeEffect();
});

// Hamburger Menu Toggle
const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("navLinks");

hamburger.addEventListener("click", () => {
    navLinks.classList.toggle("active");
});
