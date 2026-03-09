from flask import Flask, render_template, request, redirect, session, url_for
from questions import QUESTIONS

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-this"


MAX_QUESTIONS = 5
ABILITY_STEP = 0.4


def get_question_by_id(question_id: int):
    for question in QUESTIONS:
        if question["id"] == question_id:
            return question
    return None


def choose_next_question(answered_ids, ability):
    remaining = [q for q in QUESTIONS if q["id"] not in answered_ids]
    if not remaining:
        return None

    # Simplified CAT rule:
    # choose the unanswered question whose difficulty is closest to current ability
    remaining.sort(key=lambda q: abs(q["difficulty"] - ability))
    return remaining[0]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/start", methods=["POST"])
def start():
    session["ability"] = 0.0
    session["history"] = []
    session["answered_ids"] = []
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    ability = session.get("ability", 0.0)
    history = session.get("history", [])
    answered_ids = session.get("answered_ids", [])

    if request.method == "POST":
        question_id = int(request.form["question_id"])
        selected = request.form.get("answer")

        question = get_question_by_id(question_id)
        if question is None:
            return redirect(url_for("quiz"))

        is_correct = (selected == question["answer"])

        difficulty = question["difficulty"]

        if is_correct:
            ability += ABILITY_STEP * (1 + difficulty)
        else:
            ability -= ABILITY_STEP * (1 - difficulty)

        ability = max(-2, min(2, ability))

        history.append({
            "question_text": question["text"],
            "selected": selected,
            "correct_answer": question["answer"],
            "is_correct": is_correct,
            "difficulty": question["difficulty"],
        })
        answered_ids.append(question_id)

        session["ability"] = round(ability, 2)
        session["history"] = history
        session["answered_ids"] = answered_ids

        if len(history) >= MAX_QUESTIONS:
            return redirect(url_for("result"))

    ability = session.get("ability", 0.0)
    answered_ids = session.get("answered_ids", [])

    next_question = choose_next_question(answered_ids, ability)
    if next_question is None:
        return redirect(url_for("result"))

    return render_template(
        "quiz.html",
        question=next_question,
        question_number=len(answered_ids) + 1,
        max_questions=MAX_QUESTIONS,
        ability=ability,
    )


@app.route("/result")
def result():
    ability = session.get("ability", 0.0)
    history = session.get("history", [])

    if ability < -0.5:
        level = "beginner"
    elif ability < 0.8:
        level = "intermediate"
    else:
        level = "advanced"

    return render_template(
        "result.html",
        ability=ability,
        level=level,
        history=history,
    )


if __name__ == "__main__":
    app.run(debug=True)