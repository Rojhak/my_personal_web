from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import json
import os
import socket
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')

def find_free_port(start_port=5001):
    """Find a free port starting from start_port."""
    port = start_port
    while port < start_port + 100:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('127.0.0.1', port))
            sock.close()
            return port
        except OSError:
            port += 1
    raise RuntimeError('No free ports found')

def load_translations():
    """Load translations (English + German) from translations.json."""
    with open('translations.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
@app.route('/<lang>/')
def index(lang='en'):
    """Home page; default to English if invalid language."""
    if lang not in ['en', 'de']:
        return redirect(url_for('index', lang='en'))
    translations = load_translations()
    data = translations[lang]
    return render_template('index.html', data=data, lang=lang)

@app.route('/<lang>/about')
@app.route('/about', defaults={'lang': 'en'})
def about(lang='en'):
    """About page."""
    if lang not in ['en', 'de']:
        return redirect(url_for('about', lang='en'))
    translations = load_translations()
    data = translations[lang]
    return render_template('about.html', data=data, lang=lang)

@app.route('/<lang>/projects')
@app.route('/projects', defaults={'lang': 'en'})
def projects(lang='en'):
    """Projects page."""
    if lang not in ['en', 'de']:
        return redirect(url_for('projects', lang='en'))
    translations = load_translations()
    data = translations[lang]
    return render_template('projects.html', data=data, lang=lang)

@app.route('/<lang>/slides')
@app.route('/slides', defaults={'lang': 'en'})
def slides(lang='en'):
    """Slides page with PDF files from project_slides/."""
    if lang not in ['en', 'de']:
        return redirect(url_for('slides', lang='en'))
    translations = load_translations()
    data = translations[lang]
    slides_dir = 'project_slides'
    pdf_files = []

    if os.path.exists(slides_dir):
        pdf_files = [f for f in os.listdir(slides_dir) if f.endswith('.pdf')]
        pdf_files.sort()

    slides_data = []
    for pdf in pdf_files:
        name = pdf.replace('.pdf', '').replace('_', ' ').title()
        slides_data.append({
            'name': name,
            'file': pdf,
            'url': url_for('serve_slides', filename=pdf)
        })

    return render_template('slides.html', slides=slides_data, data=data, lang=lang)

@app.route('/project_slides/<path:filename>')
def serve_slides(filename):
    """Serve PDF files from the project_slides folder."""
    try:
        slides_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'project_slides')
        return send_from_directory(slides_dir, filename)
    except Exception as e:
        return f"Error serving file: {str(e)}", 500

# If you have a schedule page:
@app.route('/<lang>/schedule')
@app.route('/schedule', defaults={'lang': 'en'})
def schedule(lang='en'):
    """Schedule page with Calendly embed."""
    if lang not in ['en', 'de']:
        return redirect(url_for('schedule', lang='en'))
    translations = load_translations()
    data = translations[lang]
    return render_template('schedule.html', data=data, lang=lang)

# If you have a "dashboard" page:
@app.route('/<lang>/dashboard')
def dashboard(lang='en'):
    """Dashboard page example."""
    if lang not in ['en', 'de']:
        return redirect(url_for('dashboard', lang='en'))
    translations = load_translations()
    data = translations[lang]
    total_sales = 733000  # example
    return render_template('dashboard/index.html', data=data, lang=lang, total_sales=total_sales)

if __name__ == '__main__':
    debug_mode = True
    try:
        port = find_free_port()
        print(f"\nStarting Flask app at http://127.0.0.1:{port}/{'en' or 'de'}")
        app.run(debug=debug_mode, port=port)
    except Exception as e:
        print(f"Error: {e}")
