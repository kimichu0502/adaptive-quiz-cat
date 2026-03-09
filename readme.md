# MiniCAT

MiniCAT is a small prototype of a **Computerized Adaptive Testing (CAT)** quiz built using Python and Flask.  
The system adapts the difficulty of questions based on the user's estimated ability, simulating a simplified adaptive testing environment.

## Features

- Adaptive question selection based on user performance
- The ability update is weighted by question difficulty to better approximate adaptive testing behavior.
- Multiple-choice quiz interface
- Question history and results summary
- Simple and clean web interface

## How It Works

MiniCAT demonstrates the basic idea behind computerized adaptive testing:

1. The quiz starts with an initial ability estimate.
2. The system selects a question whose difficulty is closest to the user's current ability.
3. If the user answers correctly, the ability estimate increases.
4. If the user answers incorrectly, the ability estimate decreases.
5. The next question is selected based on the updated ability estimate.

This mimics how adaptive testing systems adjust question difficulty to better estimate a user's knowledge level.

## Tech Stack

- Python
- Flask
- HTML
- CSS
- Jinja templates

## Project Structure

```
MiniCAT/
│
├── app.py
├── questions.py
│
├── templates/
│   ├── home.html
│   ├── quiz.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── README.md
```

## Running the Project

1. Clone the repository

```
git clone https://github.com/kimichu0502/minicat.git
cd minicat
```

2. Install dependencies

```
pip install flask
```

3. Run the application

```
python app.py
```

4. Open the app in your browser

```
http://127.0.0.1:5000
```

## Future Improvements

Possible extensions include:

- Implementing a more realistic Item Response Theory (IRT) ability update
- Adding explanations for answers
- Expanding the question bank
- Adding question categories or topics
- Improving the user interface and visual feedback

---

This project was built as a small experiment to explore how **adaptive testing systems select questions based on estimated ability**.