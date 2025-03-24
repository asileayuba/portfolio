 // Function to handle navigation and update URL without reloading
 function navigate(event) {
    event.preventDefault(); // Prevent the default link behavior
    
    const target = event.target;
    const href = target.getAttribute('href'); // Get the URL from the href attribute
    const sectionId = href.substring(1); // Get the section id (remove the slash)
    
    // Scroll to the relevant section
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }

    // Update the browser's URL
    window.history.pushState(null, null, href);
}

// Attach the navigate function to all links with data-link attribute
document.querySelectorAll('a[data-link]').forEach(link => {
    link.addEventListener('click', navigate);
});

// Handle the back button and forward button
window.addEventListener('popstate', () => {
    const sectionId = window.location.pathname.substring(1);
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
});

// Function to handle smooth scroll to top
function scrollToTop(event) {
    event.preventDefault(); // Prevent the default link behavior
    window.scrollTo({
        top: 0,
        behavior: 'smooth' // Smooth scroll to the top
    });

    // Update the browser's URL to "/"
    window.history.pushState(null, null, '/');
}

// Attach the scrollToTop function to the "Back to Top" button
document.getElementById('back-to-top').addEventListener('click', scrollToTop);

/*==================== toggle icon navbar ====================*/
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
};

/*==================== scroll sections active link ====================*/
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
            });
        };
    });
    /*==================== sticky navbar ====================*/
    let header = document.querySelector('header');

    header.classList.toggle('sticker', window.scrollY > 100);

    /*==================== remove toggle icon and navbar when click navbar link (scroll) ====================*/
    menuIcon.classList.remove('bx-x');
    navbar.classList.remove('active');
};


/*==================== scroll reveal ====================*/
ScrollReveal({ 
    // reset: true,
    distance: '80px',
    duration: 2000,
    delay: 200
 });

 ScrollReveal().reveal('.home-content, .heading', { origin:  'top' });
 ScrollReveal().reveal('.home-img, .services-container, .portfolio-box, .contact form', { origin:  'bottom' });
 ScrollReveal().reveal('.home-content h1, .about-img', { origin:  'left' });
 ScrollReveal().reveal('.home-content p, .about-content', { origin:  'right' });


 /*==================== typed js ====================*/
var typed = new Typed('#multiple-text', {
    strings: ['a Web Developer', 'an Aerospace Engineering Student', 'an Aspiring AI Engineer'],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
});




document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();
  
    // Get form data
    const fullName = document.querySelector('input[name="fullName"]').value;
    const emailAddress = document.querySelector('input[name="emailAddress"]').value;
    const mobileNumber = document.querySelector('input[name="mobileNumber"]').value;
    const emailSubject = document.querySelector('input[name="emailSubject"]').value;
    const message = document.querySelector('textarea[name="message"]').value;
  
    // Create a payload object
    const payload = {
      fullName,
      emailAddress,
      mobileNumber,
      emailSubject,
      message,
    };
  
    // Send POST request to backend
    fetch('http://localhost:5001/contact', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    })
      .then(response => {
        if (response.ok) {
          alert('Message sent successfully!');
        } else {
          alert('Error sending message');
        }
      })
      .catch(error => {
        console.error('Error:', error);
        alert('Error sending message');
      });
  });
  
