

```markdown
# Personal Portfolio Website

A modern, responsive portfolio website built with Flask, featuring bilingual functionality (English/German), interactive project showcases, and a dynamic dashboard.

---

## 🌟 Features

- **Bilingual Support**: Full English and German language options
- **Responsive Design**: Optimized for all devices, from desktops to mobile
- **Interactive Sections**:
  - 📊 Project Portfolio with live demos
  - 📑 PDF Presentation Viewer
  - 📈 Interactive Tableau Dashboard
  - 📝 About Section with Timeline
  - 🗣️ Multi-language Support

---

## 🛠️ Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: PostgreSQL
- **Visualization**: Tableau
- **Deployment**: Heroku
- **Version Control**: Git

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Virtual Environment (recommended)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rojhak/my_personal_web.git
   cd my_personal_web
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv web_app_env
   source web_app_env/bin/activate  # On Windows: web_app_env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit the .env file with your configurations
   ```

5. **Run the application**:
   ```bash
   python personal_app.py
   ```

   The application will be available at `http://localhost:5001`.

---

## 📁 Project Structure

```plaintext
my_personal_web/
├── static/
│   ├── images/         # Image assets
│   ├── js/             # JavaScript files
│   └── style.css       # CSS file
├── templates/          # HTML templates
│   ├── dashboard/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   ├── slides.html
│   ├── schedule.html
│   └── contact.html
├── project_slides/     # PDF presentations
│   └── wine_quality.pdf
├── personal_app.py     # Main application script
├── requirements.txt    # Python dependencies
├── Procfile            # Heroku configuration
├── translations.json   # Bilingual support
└── .env (not committed) # Environment variables
```

---

## 🌐 Deployment

The website is configured for deployment on Heroku:

1. **Create a Heroku app**:
   ```bash
   heroku create your-app-name
   ```

2. **Set environment variables**:
   ```bash
   heroku config:set SECRET_KEY=your_secret_key
   ```

3. **Deploy the app**:
   ```bash
   git push heroku main
   ```

---

## 🔧 Configuration

Key configuration options are managed through environment variables:

- `SECRET_KEY`: Application security key
- `FLASK_ENV`: Development/Production environment
- `PORT`: Application port (default: 5001)

---

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 👤 Author

**Fehmi Katar**

- LinkedIn: [Fehmi Katar](https://www.linkedin.com/in/fehmi-dataanalyst)
- GitHub: [Rojhak](https://github.com/Rojhak)

---

## 🙏 Acknowledgments

Thanks to the open-source community for providing incredible tools and libraries.

---

Feel free to suggest further enhancements or share feedback!
```
