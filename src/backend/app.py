"""
Flask Application for Welcome to Bhopal Website
This is the main backend application serving the HTML frontend.
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

# Determine paths
backend_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(backend_dir)
frontend_dir = os.path.join(src_dir, 'frontend')
templates_dir = os.path.join(frontend_dir, 'templates')
static_dir = os.path.join(frontend_dir, 'static')

# Initialize Flask app
app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)

# Configuration
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    """
    Render the main landing page
    """
    return render_template('index.html')


@app.route('/api/page-info', methods=['GET'])
def get_page_info():
    """
    API endpoint to get page information
    Returns metadata about the page including last updated time
    """
    page_info = {
        'title': 'Welcome to Bhopal — Digital City Gateway',
        'description': 'Your digital gateway to the heart of India',
        'city': 'Bhopal',
        'state': 'Madhya Pradesh',
        'country': 'India',
        'last_updated': datetime.now().isoformat(),
        'version': '1.0.0'
    }
    return jsonify(page_info)


@app.route('/api/city-stats', methods=['GET'])
def get_city_stats():
    """
    API endpoint to get city statistics
    """
    stats = {
        'population': '1.9M+',
        'unesco_sites': 4,
        'lakes': '30+',
        'founding_year': 1707,
        'notable_features': [
            'UNESCO World Heritage Sites',
            'City of Lakes',
            'Educational Hub',
            'Cultural Center',
            'Nature Lover Haven'
        ]
    }
    return jsonify(stats)


@app.route('/api/opportunities-count', methods=['GET'])
def get_opportunities_count():
    """
    API endpoint to get current opportunities count
    """
    opportunities = {
        'job_descriptions': '50+',
        'project_booklets': '10+',
        'ep_packages_available': True,
        'exchange_cycle': '26.27',
        'updated_at': datetime.now().isoformat()
    }
    return jsonify(opportunities)


@app.route('/api/social-links', methods=['GET'])
def get_social_links():
    """
    API endpoint to get social media links
    """
    links = {
        'instagram': {
            'igv_bhopal': 'https://www.instagram.com/igv.bhopal',
            'welcome_to_bhopal': 'https://www.instagram.com/welcometobhopal',
            'chronicles_2026': 'https://www.instagram.com/_chronicles_2026_'
        },
        'resources': {
            'search_tool': 'https://docs.google.com/spreadsheets/d/1NjDweAu9sN0Ul72VR58KPVCHZpWi8VmAEhuRsIxtgpo',
            'job_descriptions': 'https://drive.google.com/drive/folders/1ltNlwLcGaJNhs9JLMILOxgFo4krVev3g',
            'project_booklets': 'https://drive.google.com/drive/folders/1GVfHC7Ie1samd3vS9bCqtI0KXxXKGj6A',
            'ep_packages': 'https://drive.google.com/drive/folders/1EBqVO8-3Wv6zmnk9yRNLcXaOGJTEdTCV',
            'testimonials': 'https://drive.google.com/drive/folders/1-qoi7-t1ZczULPFevLGhZzaFvim4LtUk'
        }
    }
    return jsonify(links)


@app.route('/api/contact', methods=['POST'])
def contact():
    """
    Handle contact form submissions (placeholder)
    """
    try:
        data = request.get_json()
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        
        # Validation
        if not all([name, email, message]):
            return jsonify({'error': 'All fields are required'}), 400
        
        # Here you would typically save to database or send email
        # For now, we'll just return success
        response = {
            'status': 'success',
            'message': f'Thank you {name}, we received your message!',
            'timestamp': datetime.now().isoformat()
        }
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Welcome to Bhopal API'
    }), 200


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors
    """
    return jsonify({
        'error': 'Resource not found',
        'status_code': 404,
        'message': 'The requested resource does not exist'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors
    """
    return jsonify({
        'error': 'Internal server error',
        'status_code': 500,
        'message': 'An unexpected error occurred'
    }), 500


if __name__ == '__main__':
    # Create necessary directories if they don't exist
    os.makedirs(templates_dir, exist_ok=True)
    os.makedirs(os.path.join(static_dir, 'css'), exist_ok=True)
    os.makedirs(os.path.join(static_dir, 'js'), exist_ok=True)
    
    # Run the Flask application
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=True
    )
