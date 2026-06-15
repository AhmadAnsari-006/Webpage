# Welcome to Bhopal - Website Project

A modern, responsive digital gateway to the City of Lakes - Bhopal, India. Built with Flask backend and a beautiful, interactive frontend.

## 📁 Project Structure

```
Webpage/
├── app.py                          # Flask application (Python backend)
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── templates/
│   └── index.html                 # Main HTML template (uses Jinja2)
│
└── static/
    ├── css/
    │   └── styles.css             # All CSS styles
    └── js/
        └── script.js              # JavaScript functionality
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd Webpage
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   - Navigate to `http://localhost:5000`
   - The website will be fully loaded and interactive

## 📝 File Descriptions

### Backend (Python/Flask)

**`app.py`**
- Main Flask application
- Routes and API endpoints
- Health check and utility endpoints
- Static file serving configuration

**API Endpoints:**
- `GET /` - Render main page
- `GET /api/page-info` - Get page metadata
- `GET /api/city-stats` - Get Bhopal city statistics
- `GET /api/opportunities-count` - Get current opportunities
- `GET /api/social-links` - Get all social media and resource links
- `GET /api/health` - Health check endpoint
- `POST /api/contact` - Contact form submission (placeholder)

**`requirements.txt`**
- Lists all Python package dependencies
- Flask, Werkzeug, Jinja2, and supporting libraries

### Frontend (HTML/CSS/JavaScript)

**`templates/index.html`**
- Complete HTML structure using Jinja2 templating
- Semantic HTML5 markup
- Updated Instagram link: https://www.instagram.com/igv.bhopal?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==
- Sections include:
  - Navigation bar
  - Hero section
  - Explore section
  - AIESEC opportunities search
  - City life showcase
  - Chronicles
  - Testimonials
  - FAQ
  - Footer

**`static/css/styles.css`**
- Complete styling for all components
- CSS Variables for theme colors
- Responsive design with media queries
- Animations and transitions
- Dark mode with gradient accents
- Mobile-optimized layouts

**`static/js/script.js`**
- Interactive functionality
- Progress bar tracking
- Mobile menu toggle
- Smooth scrolling
- Scroll-triggered animations (reveal)
- FAQ accordion toggle
- Search functionality
- Navigation highlighting

## 🎨 Design Features

- **Modern Design**: Dark theme with gradient accents (blue, purple, gold, teal, pink)
- **Responsive**: Works seamlessly on desktop, tablet, and mobile
- **Interactive**: Smooth animations, hover effects, and dynamic interactions
- **Accessible**: Semantic HTML, proper ARIA labels, keyboard navigation
- **Performance**: Optimized CSS and JavaScript, lazy loading animations

## 🔗 Key Links Integrated

- **Instagram**: https://www.instagram.com/igv.bhopal?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==
- **Welcome to Bhopal**: https://www.instagram.com/welcometobhopal
- **Chronicles 2026**: https://www.instagram.com/_chronicles_2026_
- **AIESEC Search Tool**: Google Sheets with opportunities
- **Resources**: Google Drive folders with guides, booklets, and packages

## 🎯 Sections Overview

1. **Navigation** - Fixed header with logo, links, and CTA
2. **Hero** - Landing section with main headline and call-to-action
3. **Explore** - Featured resources and guides about Bhopal
4. **Opportunities** - AIESEC search tool and available opportunities
5. **City Life** - Showcase of Bhopal's attractions and culture
6. **Chronicles** - Community stories and experiences
7. **Testimonials** - Reviews from exchange participants
8. **FAQ** - Common questions and answers
9. **CTA Banner** - Final call-to-action before footer
10. **Footer** - Links, social media, and copyright

## 🛠️ Development

### Running in Development Mode
The Flask app runs with `debug=True` by default, which enables:
- Auto-reloading on code changes
- Interactive debugger
- Detailed error pages

### Adding New Features
1. Add HTML elements in `templates/index.html`
2. Add styles in `static/css/styles.css`
3. Add functionality in `static/js/script.js`
4. Add API endpoints in `app.py` as needed

### Building for Production
1. Set `DEBUG = False` in `app.py`
2. Use a production WSGI server (e.g., Gunicorn)
3. Configure proper environment variables
4. Set up CDN for static files if needed

## 📱 Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📧 Contact & Support

- Instagram: @igv.bhopal
- Search Tool: [AIESEC Opportunities](https://docs.google.com/spreadsheets/d/1NjDweAu9sN0Ul72VR58KPVCHZpWi8VmAEhuRsIxtgpo)

## 📄 License

© 2026 Welcome to Bhopal · AIESEC in Bhopal · Made with 💙 for the City of Lakes

---

**Version**: 1.0.0  
**Last Updated**: 2026
