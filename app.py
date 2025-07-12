from flask import Flask, render_template, request
from datetime import datetime
import spacy
import optuna

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

category_units = {
    "education": 20,
    "fitness": 15,
    "project": 25,
    "exam": 30,
    "reading": 10,
    "language": 30,
    "writing": 18,
    "skill": 22
}

def categorize_goal(goal_text):
    doc = nlp(goal_text.lower())
    for token in doc:
        if token.lemma_ in category_units:
            return token.lemma_, category_units[token.lemma_]
    return "general", 20

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    goal = request.form['goal']
    start = datetime.strptime(request.form['start_date'], "%Y-%m-%d")
    end = datetime.strptime(request.form['end_date'], "%Y-%m-%d")
    total_hours = int(request.form['total_hours'])
    busy_hours = int(request.form['busy_hours'])
    free_hours = total_hours - busy_hours
    total_days = (end - start).days

    category, units = categorize_goal(goal)

    if free_hours <= 0 or total_days <= 0:
        plan = "Insufficient time to plan this goal."
    else:
        def objective(trial):
            daily_unit = trial.suggest_float("daily_unit", 0.1, units)
            required_days = units / daily_unit
            if required_days > total_days:
                return float("inf")
            return abs((free_hours * total_days) - (daily_unit * total_days))

        study = optuna.create_study(direction="minimize")
        study.optimize(objective, n_trials=50)
        best_unit = round(study.best_params["daily_unit"], 2)

        plan = (f"To achieve your goal: '{goal}' (Category: {category}), the system has determined you need to complete approximately {best_unit} units daily over {total_days} days.\n"
                f"This fits within your free time of {free_hours} hours/day.")

    return render_template('result.html', goal=goal, plan=plan)

if __name__ == '__main__':
    app.run(debug=True)
