from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import json
import os
import socket

app = Flask(__name__)

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
    with open('translations.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def load_portfolio_data():
    print("Loading portfolio data...")  # Add debug print
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(f"Found {len(data['projects'])} projects")  # Debug print
        return data

@app.route('/<lang>/')
@app.route('/', defaults={'lang': 'en'})
def index(lang):
    if lang not in ['en', 'de']:
        return redirect(url_for('index', lang='en'))
    translations = load_translations()
    portfolio = load_portfolio_data()
    
    # Combine data from both sources
    data = translations[lang]
    data['profile_image'] = 'fehmi.jpg'  # Use fehmi.jpg for home page
    data['social_links'] = portfolio['social_links']
    data['logo'] = 'your-logo.png'  # Add your logo file name here
    return render_template('index.html', data=data, lang=lang)

@app.route('/<lang>/slides')
@app.route('/slides', defaults={'lang': 'en'})
def slides(lang):
    if lang not in ['en', 'de']:
        return redirect(url_for('slides', lang='en'))
    translations = load_translations()
    data = translations[lang]
    
    # Get all PDF files from the project_slides directory
    slides_dir = 'project_slides'
    pdf_files = [f for f in os.listdir(slides_dir) if f.endswith('.pdf')]
    pdf_files.sort()  # Sort alphabetically
    
    slides_data = []
    for pdf in pdf_files:
        name = pdf.replace('.pdf', '').replace('_', ' ').title()
        slides_data.append({
            'name': name,
            'file': pdf,
            'url': url_for('serve_slides', filename=pdf)
        })
    
    return render_template('slides.html', slides=slides_data, data=data, lang=lang)

@app.route('/<lang>/about')
@app.route('/about', defaults={'lang': 'en'})
def about(lang):
    if lang not in ['en', 'de']:
        return redirect(url_for('about', lang='en'))
    translations = load_translations()
    data = translations[lang]
    data['profile_image'] = 'profile.png'
    
    # Debug prints
    print("\nLanguages type:", type(data['about']['languages']))
    print("Languages data:", data['about']['languages'])
    
    print("\nInterests type:", type(data['about']['interests']))
    print("Interests data:", data['about']['interests'])
    
    # Convert languages and interests to lists if they're not already
    if isinstance(data['about']['languages'], dict) and 'items' in data['about']['languages']:
        data['about']['languages'] = data['about']['languages']['items']
    
    if isinstance(data['about']['interests'], dict) and 'items' in data['about']['interests']:
        data['about']['interests'] = data['about']['interests']['items']
    
    return render_template('about.html', data=data, lang=lang)

@app.route('/<lang>/projects')
@app.route('/projects', defaults={'lang': 'en'})
def projects(lang):
    if lang not in ['en', 'de']:
        return redirect(url_for('projects', lang='en'))
    translations = load_translations()
    data = translations[lang]
    
    # Add slides data to the slides project
    slides_dir = 'project_slides'
    if os.path.exists(slides_dir):
        pdf_files = [f for f in os.listdir(slides_dir) if f.endswith('.pdf')]
        pdf_files.sort()
        
        # Find and update the slides project in the translated projects
        for project in data['projects']:
            if project.get('type') == 'slides':
                project['slides'] = [
                    {
                        'name': pdf.replace('.pdf', '').replace('_', ' ').title(),
                        'url': url_for('serve_slides', filename=pdf)
                    }
                    for pdf in pdf_files
                ]
    
    # Debug print to verify the data
    print(f"\nProjects data for {lang}:")
    print(json.dumps(data.get('projects', []), indent=2))
    
    return render_template('projects.html', data=data, lang=lang)

@app.route('/project_slides/<path:filename>')
def serve_slides(filename):
    print(f"Attempting to serve file: {filename}")
    try:
        # Get the absolute path to the project_slides directory
        slides_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'project_slides')
        print(f"Slides directory: {slides_dir}")
        
        # Check if file exists
        file_path = os.path.join(slides_dir, filename)
        if os.path.exists(file_path):
            print(f"File found at: {file_path}")
        else:
            print(f"File not found at: {file_path}")
        
        return send_from_directory(slides_dir, filename)
    except Exception as e:
        print(f"Error serving file: {e}")
        return f"Error: {str(e)}", 500

@app.route('/project_slides')
def project_slides():
    # Get all PDF files from the project_slides directory
    slides_dir = 'project_slides'
    pdf_files = [f for f in os.listdir(slides_dir) if f.endswith('.pdf')]
    pdf_files.sort()  # Sort alphabetically
    
    slides_data = []
    for pdf in pdf_files:
        name = pdf.replace('.pdf', '').replace('_', ' ').title()
        slides_data.append({
            'name': name,
            'file': pdf,
            'url': url_for('serve_slides', filename=pdf)
        })
    
    return render_template('slides.html', slides=slides_data)

if __name__ == '__main__':
    debug_mode = True
    try:
        port = find_free_port()
        print(f"\nStarting Flask app on http://127.0.0.1:{port}")
        print(f"Debug mode: {debug_mode}")
        print("Available routes:")
        print(f"- http://127.0.0.1:{port}/ (home)")
        print(f"- http://127.0.0.1:{port}/about (about)")
        print(f"- http://127.0.0.1:{port}/projects (projects)")
        print("Language options: /en/ or /de/")
        print("\nPress CTRL+C to quit\n")
        
        app.run(debug=debug_mode, port=port)
    except Exception as e:
        print(f"Error: {e}")