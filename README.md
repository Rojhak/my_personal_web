 README.md
# Personal Portfolio Website

A modern, responsive portfolio website built with Flask, featuring a bilingual interface (English/German), interactive project showcases, and a dynamic dashboard.

## 🌟 Features

- **Bilingual Support**: Full English and German language support
- **Responsive Design**: Optimized for all device sizes
- **Interactive Sections**:
  - 📊 Project Portfolio with live demos
  - 📑 PDF Presentation Viewer
  - 📈 Interactive Tableau Dashboard
  - 📝 About Section with Timeline
  - 🗣️ Multi-language Support

## 🛠️ Tech Stack

- **Backend**: Python/Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Database Integration**: PostgreSQL
- **Visualization**: Tableau
- **Deployment**: Heroku
- **Version Control**: Git

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Virtual Environment (recommended)

### Installation

1. Clone the repository:
\`\`\`bash
git clone https://github.com/Rojhak/my_personal_web.git
cd my_personal_web
\`\`\`

2. Create and activate virtual environment:
\`\`\`bash
python -m venv web_app_env
source web_app_env/bin/activate  # On Windows: web_app_env\Scripts\activate
\`\`\`

3. Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. Set up environment variables:
\`\`\`bash
cp .env.example .env
# Edit .env with your configurations
\`\`\`

5. Run the application:
\`\`\`bash
python personal_app.py
\`\`\`

The application will be available at \`http://localhost:5001\`

## 📁 Project Structure

\`\`\`
my_personal_web/
├── static/
│   ├── images/         # Image assets
│   │   ├── skillup.png
│   │   ├── yekmal.png
│   │   └── tablaeu.png
│   ├── js/
│   │   └── dashboard.js
│   └── style.css
├── templates/
│   ├── dashboard/
│   │   └── index.html
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   ├── slides.html
│   ├── schedule.html
│   └── contact.html
├── project_slides/
│   └── wine_quality.pdf
├── personal_app.py
├── requirements.txt
├── Procfile
├── translations.json
└── .env (not committed)
\`\`\`

## 🌐 Deployment

The website is configured for Heroku deployment:

1. Create a Heroku app
2. Set environment variables
3. Deploy using Git

\`\`\`bash
heroku create your-app-name
heroku config:set SECRET_KEY=your_secret_key
git push heroku main
\`\`\`

## 🔧 Configuration

Key configuration options are managed through environment variables:
- \`SECRET_KEY\`: Application security key
- \`FLASK_ENV\`: Development/Production environment
- \`PORT\`: Application port (default: 5001)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Fehmi Katar
- LinkedIn: [Fehmi Katar](https://www.linkedin.com/in/fehmi-dataanalyst)
- GitHub: [Rojhak](https://github.com/Rojhak)

## 🙏 Acknowledgments

- Open source community for various tools and libraries
