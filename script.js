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

// --- Contact Form Logic (Formspree) ---
document.getElementById("contact-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const form = e.target;
  const statusEl = document.getElementById("form-status");
  statusEl.textContent = "Sending...";

  try {
    const res = await fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { "Accept": "application/json" }
    });

    if (res.ok) {
      form.reset();
      statusEl.textContent = "Thanks! Your message was sent.";
    } else {
      statusEl.textContent =
        "Something went wrong. You can also email us at mini.cassia.chiropractic@gmail.com.";
    }
  } catch (err) {
    statusEl.textContent =
      "Network error. Please try again or email us at mini.cassia.chiropractic@gmail.com.";
  }
});

