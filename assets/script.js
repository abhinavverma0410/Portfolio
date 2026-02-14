document.addEventListener('DOMContentLoaded', function() {
    const sectionIds = ['hero-section', 'experience-section', 'skills-section', 'projects-section', 'contact-section'];
    
    let isClickScrolling = false;

    document.addEventListener('click', function(e) {
        
        const hamburgerWrapper = document.querySelector('.fixed-hamburger-wrapper');
        const collapseMenu = document.getElementById('hamburger-collapse');
        const hamburgerBtn = document.getElementById('hamburger-btn');

        if (hamburgerWrapper && !hamburgerWrapper.contains(e.target)) {
            if (collapseMenu && collapseMenu.classList.contains('show')) {
                if (hamburgerBtn) {
                    hamburgerBtn.click();
                }
            }
        }

        const targetLink = e.target.closest('.custom-nav-link');
        if (targetLink) {
            isClickScrolling = true;
            setTimeout(() => { isClickScrolling = false; }, 800);
        }
    });

    const observerOptions = {
        root: null,
        rootMargin: '-50% 0px -50% 0px', 
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        if (isClickScrolling) return;

        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const currentSectionId = `#${entry.target.id}`;
                
                if (window.location.hash !== currentSectionId) {
                    history.replaceState(null, null, currentSectionId);
                    window.dispatchEvent(new Event('popstate'));
                }
            }
        });
    }, observerOptions);

    const initInterval = setInterval(() => {
        const sections = sectionIds.map(id => document.getElementById(id)).filter(Boolean);
        
        if (sections.length === sectionIds.length) {
            sections.forEach(section => observer.observe(section));
            clearInterval(initInterval);
            console.log("Scroll tracking and click-away initialized successfully.");
        }
    }, 250); 
});
