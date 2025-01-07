# Project Workflow & Changes

## 2024

### January

- **03/01/2024**: Separated Flask and Streamlit applications to resolve threading conflicts and created combined version as alternative solution.
- **03/01/2024**: Created new lightweight environment 'web_app_env' for Heroku deployment.
- **03/01/2024**: Successfully implemented auto-port finding and verified Flask app functionality.

## Environment Setup
### Development Environment (Original)
- Python Environment: tensorflow_env (Anaconda)
- Python Path: /Users/fehmikatar/anaconda3/envs/tensorflow_env

### New Lightweight Environment
- Created using venv instead of conda for simplicity
- Setup commands:
  ```bash
  python -m venv web_app_env
  source web_app_env/bin/activate
  pip install flask streamlit gunicorn
  ```
- Key Dependencies:
  - Flask==3.0.0
  - Streamlit==1.29.0
  - gunicorn==21.2.0

## Future Plans
- Implement user authentication
- Add database integration
- Create API endpoints
- Improve UI/UX design

## Deployment Options

### Streamlit Cloud
- Free Tier:
  - 1 app per account
  - Public GitHub repository required
  - 1GB RAM
  - Shared CPU
  - No custom domain
  - Community support

### Heroku
- Free Tier discontinued as of Nov 28, 2022
- Starts at $5/month (Eco dyno)
- Includes:
  - 1 dyno
  - Custom domains
  - 512MB RAM
  - Automatic SSL

## Notes
- Flask runs on port 5001
- Streamlit runs on port 8501 (default)
- Combined version uses threading (development only)
- For Heroku deployment, use requirements.txt and Procfile 
- Consider Streamlit Cloud for free deployment if your code can be public
- Heroku requires paid subscription but offers more flexibility 

## Pre-Deployment Checklist
### Current Status
### Working Features
- [x] Basic Flask app setup
- [x] Auto port selection
- [x] Multi-language support (EN/DE)
- [x] Template rendering
- [x] JSON data loading
- [x] Multiple routes (home, about, projects)
- [x] Error handling

### Required Features
- [ ] Complete UI design
- [ ] Add all content
- [ ] Mobile responsiveness
- [ ] Loading states

### Testing
- [ ] Local testing
- [ ] Cross-browser testing
- [ ] Performance testing
- [ ] Security checks

## Next Steps
1. Set up the Streamlit app
2. Add your actual content and routes
3. Design the UI layout
4. Implement remaining features from the checklist 