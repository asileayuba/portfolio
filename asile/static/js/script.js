document.addEventListener("DOMContentLoaded", function () {
    // Initialize Typed.js for animated text
    if (document.getElementById('multiple-text')) {
        new Typed('#multiple-text', {
            strings: ['a Web Developer', 'an Aerospace Engineering Student', 'an Aspiring AI Engineer'],
            typeSpeed: 100,
            backSpeed: 100,
            backDelay: 1000,
            loop: true
        });
    }

    // Typewriter Effect for Dynamic Text
    function sleep(ms) {
        return new Promise((resolve) => setTimeout(resolve, ms));
    }

    const phrases = ["a Web Developer", "an Aerospace Engineering Student"];
    const el = document.getElementById("typewriter");

    if (el) {
        let sleepTime = 100;
        let curPhraseIndex = 0;

        const writeLoop = async () => {
            while (true) {
                let curWord = phrases[curPhraseIndex];

                // Typing effect
                for (let i = 0; i <= curWord.length; i++) {
                    el.innerText = curWord.substring(0, i);
                    await sleep(sleepTime);
                }

                await sleep(sleepTime * 10);

                // Backspacing effect
                for (let i = curWord.length; i >= 0; i--) {
                    el.innerText = curWord.substring(0, i);
                    await sleep(sleepTime);
                }

                await sleep(sleepTime * 5);

                // Move to the next phrase
                curPhraseIndex = (curPhraseIndex + 1) % phrases.length;
            }
        };

        writeLoop();
    }

    // JavaScript for typing effect
    const typedTextElement = document.getElementById("typed-text");
    const textArray = ["Passionate Web Developer", "AI Enthusiast", "Aerospace Engineer"];
    let textIndex = 0;
    let charIndex = 0;

    function typeText() {
        if (charIndex < textArray[textIndex].length) {
            typedTextElement.textContent += textArray[textIndex].charAt(charIndex);
            charIndex++;
            setTimeout(typeText, 100);  // Adjust typing speed (100ms per character)
        } else {
            setTimeout(() => {
                charIndex = 0;
                textIndex++;
                if (textIndex >= textArray.length) {
                    textIndex = 0;  // Loop through the array again
                }
                typedTextElement.textContent = "";  // Clear the text
                typeText();  // Start typing the next text
            }, 1000);  // Delay before typing the next phrase (1 second)
        }
    }

    if (typedTextElement) {
        typeText();  // Start typing effect
    }

    // JavaScript for progress bar colors
    const progressBars = document.querySelectorAll('.progress-bar');
    progressBars.forEach((bar) => {
        let percentage = bar.getAttribute('aria-valuenow');
        bar.style.width = `${percentage}%`;

        // Change color based on the percentage value
        if (percentage <= 20) {
            bar.style.backgroundColor = 'red';  // 0-20% (red)
        } else if (percentage <= 50) {
            bar.style.backgroundColor = 'blue';  // 20-50% (blue)
        } else {
            bar.style.backgroundColor = 'green';  // 50-100% (green)
        }
    });
});

// Back to Top Button
const backToTopButton = document.getElementById("backToTop");

// Show or hide the button based on scroll position
window.onscroll = function () {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        backToTopButton.style.display = "block";
    } else {
        backToTopButton.style.display = "none";
    }
};

// Scroll to the top when the button is clicked
backToTopButton.onclick = function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
};
