// --- Page Navigation Logic ---
function showPage(pageId, navElement) {
    // Hide all page content
    document.querySelectorAll('.page-content').forEach(page => {
        page.classList.remove('active');
    });

    // Show the selected page
    const activePage = document.getElementById(pageId);
    if (activePage) {
        activePage.classList.add('active');
    }

    // Update active state on nav links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
    });
    
    // Add active class to the correct nav link(s)
    const mainNavLink = document.getElementById(`nav-${pageId}`);
    if(mainNavLink) mainNavLink.classList.add('active');
    
    // Also handle the main 'Home' and 'About' links directly
    if (navElement && (pageId === 'home' || pageId === 'about' || pageId === 'location' || pageId === 'contact')) {
         navElement.classList.add('active');
    }

    // Scroll to the top of the page on navigation
    window.scrollTo(0, 0);
    event.preventDefault(); // Prevent default anchor link behavior
}

// --- Mobile Menu Logic ---
const mobileMenuButton = document.getElementById('mobile-menu-button');
const mobileMenu = document.getElementById('mobile-menu');

mobileMenuButton.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

function closeMenu() {
    if(!mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.add('hidden');
    }
}

// --- Contact Form Logic ---
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const inquiry = document.getElementById('inquiry').value;
    
    const subject = `New Inquiry from ${name}`;
    const body = `Name: ${name}%0D%0AEmail: ${email}%0D%0APhone: ${phone}%0D%0A%0D%0AMessage:%0D%0A${inquiry}`;
    
    window.location.href = `mailto:mini.cassia.chiropractic@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
});
