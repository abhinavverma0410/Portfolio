document.addEventListener('DOMContentLoaded', function() {
    
    let isScrollingManual = false;
    let scrollTimeout = null;

    // 1. SCROLL SPY + URL UPDATER
    function updateActiveState() {
        if (isScrollingManual) return; // Don't fight the click scroll

        const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
        const sections = document.querySelectorAll('[id$="-section"]');
        const scrollPosition = window.scrollY + 150; // Offset for navbar

        let currentSectionId = '';

        // -- Special Case: Top of Page --
        if (window.scrollY < 50) {
            currentSectionId = '#hero-section';
        } 
        // -- Special Case: Bottom of Page (Strict Check) --
        // Only trigger contact if we are literally at the very bottom pixel
        else if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 5) {
            currentSectionId = '#contact-section';
        } 
        // -- Standard Section Tracking --
        else {
            sections.forEach(section => {
                const sectionTop = section.offsetTop - 150;
                const sectionBottom = sectionTop + section.offsetHeight;
                
                if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                    currentSectionId = `#${section.id}`;
                }
            });
        }

        // Apply Changes
        if (currentSectionId) {
            // A. visual highlight
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === currentSectionId) {
                    link.classList.add('active');
                }
            });

            // B. Update Browser URL (Throttle this to avoid lag)
            if (history.replaceState && window.location.hash !== currentSectionId) {
                // replaceState updates URL without adding to back-button history
                history.replaceState(null, null, currentSectionId);
            }
        }
    }

    // 2. CLICK HANDLER (Smooth Scroll + URL Update)
    document.addEventListener('click', function(e) {
        const targetLink = e.target.closest('a[href^="#"]');
        
        if (targetLink) {
            e.preventDefault(); // Stop default jump
            isScrollingManual = true; // Lock scroll spy temporarily

            const targetId = targetLink.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                // 1. Update URL immediately
                if(history.pushState) {
                    history.pushState(null, null, targetId);
                }

                // 2. Smooth Scroll
                const navbarHeight = 70; 
                const elementPosition = targetSection.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - navbarHeight;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });

                // 3. Set Active Class
                document.querySelectorAll('.navbar-nav .nav-link').forEach(l => l.classList.remove('active'));
                targetLink.classList.add('active');

                // 4. Unlock Scroll Spy after animation (approx 800ms)
                setTimeout(() => {
                    isScrollingManual = false;
                }, 800);
            }
        }
    });

    // 3. INITIALIZATION
    const initInterval = setInterval(() => {
        const nav = document.querySelector('.navbar-nav');
        if (nav) {
            console.log("Navbar detected. Initializing URL-updater script...");
            window.addEventListener('scroll', () => {
                // Simple throttle for performance
                if (scrollTimeout) clearTimeout(scrollTimeout);
                scrollTimeout = setTimeout(updateActiveState, 50);
            });
            updateActiveState();
            clearInterval(initInterval);
        }
    }, 100);
});