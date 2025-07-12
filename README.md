# Goal Breakdown Planner (AI-Powered)

This is a AI-powered dynamic website that helps users break down their personal goals into actionable steps based on their available time.

## 🎯 Features
- Accepts goal description and time availability
- Uses NLP (SpaCy) to understand the goal category
- Uses Optuna to optimize and suggest a personalized daily plan
- Clean and simple web UI built with Flask

## 🚀 How to Run Locally
1. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Run the app**
   ```
   python app.py
   ```

3. Open browser and visit:
   ```
   http://localhost:5000
   ```

## 🌐 Deploy on Render
1. Push code to GitHub
2. Go to [https://render.com](https://render.com)
3. Create new Web Service
4. Set:
   - **Environment**: Python
   - **Start Command**: `gunicorn app:app`
5. Connect GitHub repo and deploy!

## 🧠 Tech Stack
- Python
- Flask
- SpaCy (NLP)
- Optuna (Hyperparameter optimization)
- HTML, CSS (Frontend)

---

Created for Project
