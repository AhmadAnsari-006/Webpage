# 🚀 Quick Start Guide

## ⚡ 5-Minute Setup

### Step 1: Install Python Dependencies
```bash
cd c:\Users\ahmad\Desktop\AIESEC\Webpage
pip install -r requirements.txt
```

### Step 2: Run the Flask Application
```bash
python app.py
```

### Step 3: Open in Browser
- Go to: `http://localhost:5000`
- You should see the beautiful Bhopal website!

---

## 📊 Project Organization

Your website has been organized into a professional structure:

```
Webpage/
│
├── Python Backend
│   ├── app.py (Flask server)
│   └── requirements.txt (dependencies)
│
├── HTML Templates
│   └── templates/index.html (Page structure)
│
├── CSS Styling
│   └── static/css/styles.css (All styles)
│
└── JavaScript
    └── static/js/script.js (Interactive features)
```

---

## 🔗 Key Updates Made

✅ **Instagram Link Added:**
- URL: https://www.instagram.com/igv.bhopal?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==
- Added in 4 locations:
  1. Navigation "Follow IGV" button
  2. Mobile menu
  3. Footer social links
  4. CTA banner section

✅ **Code Separated Into:**
- **HTML** - Clean structure in `templates/index.html`
- **CSS** - All styling in `static/css/styles.css`
- **JavaScript** - Interactivity in `static/js/script.js`
- **Python/Flask** - Backend in `app.py`

---

## 📁 File Breakdown

| File | Purpose | Lines |
|------|---------|-------|
| `app.py` | Flask backend with API endpoints | ~150 |
| `templates/index.html` | HTML template | ~850 |
| `static/css/styles.css` | All CSS styling | ~850 |
| `static/js/script.js` | JavaScript functionality | ~100 |

---

## 🎯 What's Included

### Backend (Flask) Features:
- ✅ 6 API endpoints
- ✅ Health checks
- ✅ Social link management
- ✅ City statistics endpoint
- ✅ Opportunity counts
- ✅ Contact form placeholder

### Frontend Features:
- ✅ Responsive design (mobile, tablet, desktop)
- ✅ Dark theme with gradients
- ✅ Smooth animations
- ✅ Interactive FAQ
- ✅ Mobile hamburger menu
- ✅ Progress bar
- ✅ Reveal on scroll effects

---

## 🔧 API Endpoints Available

Once the server is running, you can access:

```
GET  http://localhost:5000/                    # Main page
GET  http://localhost:5000/api/page-info       # Page metadata
GET  http://localhost:5000/api/city-stats      # Bhopal stats
GET  http://localhost:5000/api/opportunities   # Open opportunities
GET  http://localhost:5000/api/social-links    # All social links
GET  http://localhost:5000/api/health          # Health check
POST http://localhost:5000/api/contact         # Contact form
```

---

## 📝 Making Changes

### To update the website:

1. **Modify HTML** → Edit `templates/index.html`
2. **Change styles** → Edit `static/css/styles.css`
3. **Add functionality** → Edit `static/js/script.js`
4. **Update backend** → Edit `app.py`

Changes will auto-reload if you have debug mode enabled!

---

## 📱 Testing on Different Devices

The site is fully responsive! Test on:
- Desktop (1920px+)
- Tablet (768px - 1024px)
- Mobile (320px - 767px)

All layouts are optimized for each breakpoint.

---

## 🎨 Color Theme

The site uses these main colors:
- **Primary**: Blue (`#4f7cff`)
- **Secondary**: Purple (`#7c5cff`)
- **Accent**: Gold (`#f0b429`)
- **Highlight**: Teal (`#00d4aa`)
- **Accent**: Pink (`#ff5fa0`)
- **Background**: Dark (`#050811`)

All colors are CSS variables - easy to customize!

---

## ✨ Next Steps

1. **Customize Content** - Edit text in `templates/index.html`
2. **Update Colors** - Modify CSS variables in `static/css/styles.css`
3. **Add More Pages** - Create new routes in `app.py`
4. **Database Integration** - Connect database for contact forms
5. **Deploy** - Use platforms like:
   - Heroku
   - AWS
   - Azure
   - DigitalOcean
   - Render

---

## 💡 Tips

- **Instagram Link**: Use the UTM parameters for tracking analytics
- **Search Tool**: Links to Google Sheets for opportunity searches
- **Mobile First**: Test on mobile before desktop
- **SEO Ready**: HTML is semantic and SEO-optimized
- **Performance**: Static files are optimized and cached

---

## ❓ Troubleshooting

### Port 5000 already in use?
```bash
# Use a different port
python app.py
# Then modify the port in app.py to a free one
```

### CSS not loading?
- Make sure `static/css/styles.css` exists
- Check browser console for 404 errors

### JavaScript not working?
- Ensure `static/js/script.js` is present
- Check browser console for errors

---

## 📞 Support Resources

- **Flask Documentation**: https://flask.palletsprojects.com
- **Instagram**: https://www.instagram.com/igv.bhopal
- **AIESEC Search**: https://docs.google.com/spreadsheets/d/1NjDweAu9sN0Ul72VR58KPVCHZpWi8VmAEhuRsIxtgpo

---

**Enjoy your new structured website!** 🎉

Made with 💙 for the City of Lakes
