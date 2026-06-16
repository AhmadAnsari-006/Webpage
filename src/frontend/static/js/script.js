// Progress bar
window.addEventListener('scroll', () => {
  const h = document.documentElement;
  const pct = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
  document.getElementById('progress-bar').style.width = pct + '%';
});

// Mobile menu
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobile-menu');

if (hamburger) {
  hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
  });
}

function closeMobile() {
  mobileMenu.classList.remove('open');
}

// Nav scroll style
const nav = document.getElementById('main-nav');
window.addEventListener('scroll', () => {
  if (window.scrollY > 80) {
    nav.style.background = 'rgba(5,8,17,0.92)';
  } else {
    nav.style.background = 'rgba(5,8,17,0.7)';
  }
});

// Reveal on scroll
const reveals = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

reveals.forEach(el => observer.observe(el));

// FAQ toggle
function toggleFaq(item) {
  const isOpen = item.classList.contains('open');
  document.querySelectorAll('.faq-item').forEach(f => f.classList.remove('open'));
  if (!isOpen) item.classList.add('open');
}

// Search tool open
function openSearch() {
  const q = document.getElementById('search-query').value.trim();
  if (q) {
    window.open('https://docs.google.com/spreadsheets/d/1NjDweAu9sN0Ul72VR58KPVCHZpWi8VmAEhuRsIxtgpo', '_blank');
  } else {
    window.open('https://docs.google.com/spreadsheets/d/1NjDweAu9sN0Ul72VR58KPVCHZpWi8VmAEhuRsIxtgpo', '_blank');
  }
}

// Enter key search
const searchInput = document.getElementById('search-query');
if (searchInput) {
  searchInput.addEventListener('keydown', e => {
    if (e.key === 'Enter') openSearch();
  });
}

// Smooth anchor scrolling
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
      closeMobile();
    }
  });
});
