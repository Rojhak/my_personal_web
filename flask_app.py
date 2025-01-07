from flask import Flask, render_template, request, redirect, url_for
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
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/<lang>/')
@app.route('/', defaults={'lang': 'en'})
def index(lang):
    if lang not in ['en', 'de']:
        return redirect(url_for('index', lang='en'))
    translations = load_translations()
    portfolio = load_portfolio_data()
    
    # Combine data from both sources
    data = translations[lang]
    data['profile_image'] = 'fehmi.jpg'
    data['social_links'] = portfolio['social_links']
    return render_template('index.html', data=data, lang=lang)

@app.route('/<lang>/about')
@app.route('/about', defaults={'lang': 'en'})
def about(lang):
    if lang not in ['en', 'de']:
        return redirect(url_for('about', lang='en'))
    translations = load_translations()
    data = translations[lang]
    data['profile_image'] = 'profile.png'
    return render_template('about.html', data=data, lang=lang)

@app.route('/<lang>/projects')
@app.route('/projects', defaults={'lang': 'en'})
def projects(lang):
    if lang not in ['en', 'de']:
        return redirect(url_for('projects', lang='en'))
    translations = load_translations()
    return render_template('projects.html', data=translations[lang], lang=lang)

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