# Project Structure Visualization

```
Welcome to Bhopal Website
│
├── 📄 app.py                                    [PYTHON/FLASK BACKEND]
│   ├── Flask application initialization
│   ├── Route handlers
│   ├── API endpoints
│   └── Error handling
│
├── 📄 requirements.txt                         [DEPENDENCIES]
│   └── Python package requirements
│
├── 📄 README.md                                [DOCUMENTATION]
│   └── Project guide and setup instructions
│
├── 📄 index.html                               [OLD - ORIGINAL]
│   └── Original single-file version
│
├── 📁 templates/                               [HTML TEMPLATES]
│   └── 📄 index.html                          [JINJA2 TEMPLATE]
│       ├── Navigation with IGV Instagram link
│       ├── Hero section
│       ├── Explore & Resources
│       ├── AIESEC Opportunities
│       ├── City Life
│       ├── Chronicles
│       ├── Testimonials
│       ├── FAQ
│       └── Footer
│
└── 📁 static/                                  [STATIC FILES]
    ├── 📁 css/                                 [STYLESHEETS]
    │   └── 📄 styles.css                      [COMPLETE CSS]
    │       ├── CSS Variables & Theme
    │       ├── Navigation styles
    │       ├── Hero animations
    │       ├── Card components
    │       ├── Grid layouts (bento, explore, city)
    │       ├── Testimonials & FAQ
    │       ├── Responsive design
    │       └── Mobile optimization
    │
    └── 📁 js/                                  [JAVASCRIPT]
        └── 📄 script.js                       [FUNCTIONALITY]
            ├── Progress bar
            ├── Mobile menu toggle
            ├── Navigation effects
            ├── Scroll animations
            ├── FAQ accordion
            ├── Search tool
            └── Smooth scrolling
```

## File Types & Purposes

| File Type | Location | Purpose |
|-----------|----------|---------|
| Python/Flask | `app.py` | Backend server & API |
| HTML | `templates/index.html` | Page structure & layout |
| CSS | `static/css/styles.css` | Visual styling & animations |
| JavaScript | `static/js/script.js` | Interactive features |
| Config | `requirements.txt` | Dependencies |
| Docs | `README.md` | Documentation |

## Key Features by File

### HTML (`templates/index.html`)
- ✅ Updated Instagram link: https://www.instagram.com/igv.bhopal
- ✅ Fully structured semantic markup
- ✅ Jinja2 template syntax for static file references
- ✅ All 10 major sections

### CSS (`static/css/styles.css`)
- ✅ 40+ CSS classes for styling
- ✅ Dark theme with colorful gradients
- ✅ Mobile-first responsive design
- ✅ Smooth animations & transitions
- ✅ CSS Variables for easy theming

### JavaScript (`static/js/script.js`)
- ✅ Scroll-triggered reveal animations
- ✅ Mobile hamburger menu
- ✅ FAQ accordion functionality
- ✅ Search tool integration
- ✅ Smooth anchor scrolling

### Flask Backend (`app.py`)
- ✅ 6+ API endpoints
- ✅ Health check monitoring
- ✅ Error handling (404, 500)
- ✅ JSON response formatting
- ✅ Contact form placeholder

## Instagram Integration

**Primary Link Added:**
- URL: https://www.instagram.com/igv.bhopal?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==
- Locations in HTML:
  - Navigation bar CTA button
  - Mobile menu
  - Footer social links
  - CTA banner section

## How to Run

```bash
# 1. Navigate to project folder
cd Webpage

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Flask app
python app.py

# 4. Open browser
# http://localhost:5000
```

---

**Total Files**: 7  
**Total Lines of Code**: 1500+  
**Organized into**: 3 categories (Python/HTML/CSS-JS)
