document.addEventListener('DOMContentLoaded', function() {
    // The exact IDs of your portfolio layout sections
    const sectionIds = ['hero-section', 'experience-section', 'skills-section', 'projects-section', 'contact-section'];
    
    // Flag to pause observer during click-based smooth scrolling
    let isClickScrolling = false;

    // 1. Global Click Listener (Handles Outside Clicks & Link Tracking)
    document.addEventListener('click', function(e) {
        
        // --- NEW: Click-Away Logic ---
        const hamburgerWrapper = document.querySelector('.fixed-hamburger-wrapper');
        const collapseMenu = document.getElementById('hamburger-collapse');
        const hamburgerBtn = document.getElementById('hamburger-btn');

        // Check if the click happened outside the menu wrapper entirely
        if (hamburgerWrapper && !hamburgerWrapper.contains(e.target)) {
            // Check if the menu is currently expanded/open
            if (collapseMenu && collapseMenu.classList.contains('show')) {
                // Programmatically click the toggle button to let Dash safely close it
                if (hamburgerBtn) {
                    hamburgerBtn.click();
                }
            }
        }
        // -----------------------------

        // --- EXISTING: Dropdown link click tracking ---
        const targetLink = e.target.closest('.custom-nav-link');
        if (targetLink) {
            isClickScrolling = true;
            setTimeout(() => { isClickScrolling = false; }, 800); // Re-enable tracking after scroll
        }
    });

    // 2. Setup Intersection Observer
    const observerOptions = {
        root: null,
        rootMargin: '-50% 0px -50% 0px', 
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        if (isClickScrolling) return; // Ignore intersections if clicking a link

        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const currentSectionId = `#${entry.target.id}`;
                
                // Only act if the hash is actually changing
                if (window.location.hash !== currentSectionId) {
                    history.replaceState(null, null, currentSectionId);
                    // Fire a popstate event to trigger Dash's dcc.Location callback
                    window.dispatchEvent(new Event('popstate'));
                }
            }
        });
    }, observerOptions);

    // 3. Wait for Dash to load the DOM, then attach the observer
    const initInterval = setInterval(() => {
        const sections = sectionIds.map(id => document.getElementById(id)).filter(Boolean);
        
        if (sections.length === sectionIds.length) {
            sections.forEach(section => observer.observe(section));
            clearInterval(initInterval);
            console.log("Scroll tracking and click-away initialized successfully.");
        }
    }, 250); 
});
