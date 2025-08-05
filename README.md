# Quiz Application Using Flask

## 📌 Introduction

This is a simple yet interactive **Quiz Application** built with the Flask web framework in Python. It allows users to attempt multiple-choice questions on Python and general knowledge, track their progress, and view their final score. The application uses a clean Bootstrap interface along with Flask's backend capabilities to provide a seamless quiz experience.

---

## 🚀 Features

* Dynamic quiz system powered by a database
* Multiple-choice questions with radio options
* Displays one question per page
* Tracks user answers using session
* Calculates and displays final score
* Option to retake the quiz
* Designed with responsive Bootstrap UI

---

## ⚙️ Workflow Overview

1. **Home Page**
   → Welcome screen with a "Start Quiz" button

2. **Quiz Flow**
   → User sees questions one by one
   → Selects an option and submits
   → Answer is stored in session
   → Proceeds to next question

3. **Result Page**
   → Marks the quiz based on correct answers
   → Shows user score out of total
   → "Try Again" button to restart the quiz

---

## 📁 Project Structure

```
app/
│
├── __init__.py          → App factory & configuration
├── models/
│   └── models.py        → SQLAlchemy models (Question class)
├── routes/
│   └── quiz_routes.py   → All quiz-related routes & logic
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── quiz.html
│   └── result.html
└── static/
    └── style.css        → Custom CSS styling
```

---

## 📚 Libraries & Technologies Used

| Library / Tool       | Purpose                                 |
| -------------------- | --------------------------------------- |
| **Flask**            | Web framework                           |
| **Flask-WTF**        | Form handling & CSRF protection         |
| **Flask-SQLAlchemy** | ORM to manage database models           |
| **WTForms**          | Creating quiz forms                     |
| **SQLite**           | Lightweight database to store questions |
| **Bootstrap 5**      | Frontend styling and layout             |

---

## ✅ How It Works Internally

* The application follows the **Flask App Factory pattern**
* Questions are stored in an SQLite database via SQLAlchemy
* User progress is stored using Flask sessions
* Each time a question is answered, the app fetches the next one from the database
* At the end of the quiz, the score is calculated by comparing user answers against correct options

---
