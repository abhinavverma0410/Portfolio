document.addEventListener('DOMContentLoaded', function() {
    
    let isScrollingManual = false;
    let scrollTimeout = null;

    function updateActiveState() {
        if (isScrollingManual) return;

        const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
        const sections = document.querySelectorAll('[id$="-section"]');
        const scrollPosition = window.scrollY + 150;

        let currentSectionId = '';

        if (window.scrollY < 50) {
            currentSectionId = '#hero-section';
        } 
        else if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 5) {
            currentSectionId = '#contact-section';
        } 
        else {
            sections.forEach(section => {
                const sectionTop = section.offsetTop - 150;
                const sectionBottom = sectionTop + section.offsetHeight;
                
                if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                    currentSectionId = `#${section.id}`;
                }
            });
        }

        if (currentSectionId) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === currentSectionId) {
                    link.classList.add('active');
                }
            });

            if (history.replaceState && window.location.hash !== currentSectionId) {
                history.replaceState(null, null, currentSectionId);
            }
        }
    }

    document.addEventListener('click', function(e) {
        const targetLink = e.target.closest('a[href^="#"]');
        
        if (targetLink) {
            e.preventDefault();
            isScrollingManual = true;

            const targetId = targetLink.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                if(history.pushState) {
                    history.pushState(null, null, targetId);
                }

                const navbarHeight = 70; 
                const elementPosition = targetSection.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - navbarHeight;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });

                document.querySelectorAll('.navbar-nav .nav-link').forEach(l => l.classList.remove('active'));
                targetLink.classList.add('active');

                setTimeout(() => {
                    isScrollingManual = false;
                }, 800);
            }
        }
    });

    const initInterval = setInterval(() => {
        const nav = document.querySelector('.navbar-nav');
        if (nav) {
            console.log("Navbar detected. Initializing URL-updater script...");
            window.addEventListener('scroll', () => {
                if (scrollTimeout) clearTimeout(scrollTimeout);
                scrollTimeout = setTimeout(updateActiveState, 50);
            });
            updateActiveState();
            clearInterval(initInterval);
        }
    }, 100);
});
