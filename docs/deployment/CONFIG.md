# Configuration Guide

## Project Configuration

### Flask Configuration (`app.py`)

```python
# Current Settings:
app.config['DEBUG'] = True              # Auto-reload on changes
app.config['JSON_SORT_KEYS'] = False    # Preserve JSON key order

# Server Settings:
host='0.0.0.0'                          # Listen on all interfaces
port=5000                               # Port number
debug=True                              # Debug mode enabled
use_reloader=True                       # Auto-reload on code changes
```

### To change settings:

#### Change Port
```python
# In app.py, find this line:
app.run(port=5000)

# Change to:
app.run(port=8000)  # or any other port
```

#### Disable Debug Mode (Production)
```python
# In app.py:
app.config['DEBUG'] = False
app.run(debug=False)
```

---

## Directory Configuration

### Static Files
All static files are served from the `static/` directory:
```
static/
├── css/
│   └── styles.css        # Main stylesheet
└── js/
    └── script.js         # Main script file
```

### Templates
HTML templates are served from the `templates/` directory:
```
templates/
└── index.html            # Main page template
```

### To add new static files:
1. Place CSS in `static/css/`
2. Place JavaScript in `static/js/`
3. Reference in HTML using: `{{ url_for('static', filename='path/file.ext') }}`

---

## Instagram Integration

### Primary Instagram Account
**IGV Bhopal** (Main Account)
```
URL: https://www.instagram.com/igv.bhopal
UTM Parameter: ?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==
Full URL: https://www.instagram.com/igv.bhopal?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==
```

### Other Instagram Accounts
```
Welcome to Bhopal: https://www.instagram.com/welcometobhopal
Chronicles 2026: https://www.instagram.com/_chronicles_2026_
```

### Where Instagram Link Appears
1. **Navigation** - "Follow IGV ↗" button (top right)
2. **Mobile Menu** - "Follow IGV ↗" link
3. **Footer** - Social media button (📷 icon)
4. **CTA Banner** - "Follow on Instagram" button

---

## Environment Variables (Optional)

To use environment variables, add to `app.py`:

```python
import os

# Example:
DEBUG_MODE = os.getenv('DEBUG', 'True').lower() == 'true'
FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))

app.config['DEBUG'] = DEBUG_MODE
```

Then set in terminal:
```bash
# On Windows:
set DEBUG=False
set FLASK_PORT=8000

# On Mac/Linux:
export DEBUG=False
export FLASK_PORT=8000

# Then run:
python app.py
```

---

## Database Configuration (Future)

To add database support:

```python
# Install SQLAlchemy:
# pip install flask-sqlalchemy

from flask_sqlalchemy import SQLAlchemy

# Add to app.py:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bhopal.db'
db = SQLAlchemy(app)

# Create models for contact submissions, etc.
```

---

## CORS Configuration (If Needed)

To enable CORS (for external API calls):

```python
# Install flask-cors:
# pip install flask-cors

from flask_cors import CORS

# Add to app.py:
CORS(app)
```

---

## Email Configuration (For Contact Form)

To enable email sending:

```python
# Install flask-mail:
# pip install flask-mail

from flask_mail import Mail, Message

# Add to app.py:
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)
```

---

## Logging Configuration

Add logging to `app.py`:

```python
import logging
from logging.handlers import RotatingFileHandler

# Create logs directory
if not os.path.exists('logs'):
    os.mkdir('logs')

# Configure logger
file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

app.logger.info('Welcome to Bhopal app startup')
```

---

## Production Deployment Configuration

### Using Gunicorn (Recommended)

1. **Install Gunicorn:**
```bash
pip install gunicorn
```

2. **Create `wsgi.py`:**
```python
from app import app

if __name__ == "__main__":
    app.run()
```

3. **Run with Gunicorn:**
```bash
gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:app
```

4. **Update `requirements.txt`:**
```
Flask==2.3.3
Gunicorn==21.2.0
```

---

## SSL/HTTPS Configuration

For production with HTTPS:

```python
# Using PyOpenSSL:
# pip install pyopenssl

# In app.py:
if __name__ == '__main__':
    app.run(
        ssl_context='adhoc'  # Requires pyopenssl
    )
```

Or use nginx/Apache reverse proxy for SSL.

---

## Cache Configuration

Add caching to `app.py`:

```python
# Install flask-caching:
# pip install flask-caching

from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Cache a route:
@app.route('/api/city-stats')
@cache.cached(timeout=3600)  # Cache for 1 hour
def get_city_stats():
    # ...
```

---

## Development vs Production Settings

### Development (`app.py` - default)
```python
app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['JSON_SORT_KEYS'] = False
```

### Production
```python
app.config['DEBUG'] = False
app.config['TESTING'] = False
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
```

---

## Testing Configuration

Add testing support:

```python
# Install pytest:
# pip install pytest flask-testing

# Create test file: test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```

Run tests:
```bash
pytest test_app.py
```

---

## Performance Optimization

### Enable Compression
```python
# Install flask-compress:
# pip install flask-compress

from flask_compress import Compress

Compress(app)
```

### Minify Static Files
- Already optimized in production
- Use tools like `cssmin` and `jsmin` for minification

### CDN Integration
Reference external CDN for fonts:
```html
<!-- Already included in index.html -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display..." rel="stylesheet" />
```

---

## Monitoring & Analytics

### Add Google Analytics (Optional)
Add to `templates/index.html` before `</body>`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID');
</script>
```

---

## Backup & Recovery

### Backup Important Files
```bash
# Windows:
xcopy "c:\Users\ahmad\Desktop\AIESEC\Webpage\*" "backup\Webpage" /E /I

# Mac/Linux:
cp -r Webpage Webpage_backup
```

---

## Troubleshooting Configuration Issues

| Issue | Solution |
|-------|----------|
| Port already in use | Change port in `app.run(port=8000)` |
| Static files not loading | Check `static/` folder exists |
| Templates not found | Check `templates/` folder path |
| CORS errors | Install and enable `flask-cors` |
| No email sent | Check mail configuration and credentials |

---

## Configuration Checklist

- [ ] Python 3.7+ installed
- [ ] `requirements.txt` dependencies installed
- [ ] `templates/` folder exists with `index.html`
- [ ] `static/css/` folder has `styles.css`
- [ ] `static/js/` folder has `script.js`
- [ ] Port 5000 is available
- [ ] Instagram links are correct
- [ ] API endpoints tested
- [ ] CORS configured if needed
- [ ] Logging enabled
- [ ] Backups created

---

For more advanced configurations, refer to:
- [Flask Documentation](https://flask.palletsprojects.com)
- [Jinja2 Template Engine](https://jinja.palletsprojects.com)
- [Gunicorn Documentation](https://gunicorn.org)

**Last Updated**: 2026
