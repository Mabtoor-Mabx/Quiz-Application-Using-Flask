from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models.models import Question
from app import db
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

quiz_bp = Blueprint('quiz', __name__)

class QuizForm(FlaskForm):
    choices = RadioField('Option', choices=[], validators=[DataRequired()])
    submit = SubmitField('Next')

@quiz_bp.route('/')
def home():
    session.clear()
    return render_template('home.html')

@quiz_bp.route('/quiz', methods=['GET', 'POST'])
def quiz():
    form = QuizForm()

    # If user is just starting, find the first question in the DB
    question_id = session.get('current_question')
    if not question_id:
        first_question = Question.query.order_by(Question.id.asc()).first()
        if not first_question:
            return redirect(url_for('quiz.result'))  # No questions in DB
        question_id = first_question.id
        session['current_question'] = question_id

    question = Question.query.get(question_id)

    # Set choices
    form.choices.choices = [
        ('A', question.option_a),
        ('B', question.option_b),
        ('C', question.option_c),
        ('D', question.option_d),
    ]

    if form.validate_on_submit():
        answers = session.get('answers', {})
        answers[str(question.id)] = form.choices.data
        session['answers'] = answers

        # Move to next question based on actual DB ordering
        next_question = Question.query.filter(Question.id > question.id).order_by(Question.id.asc()).first()
        if next_question:
            session['current_question'] = next_question.id
            return redirect(url_for('quiz.quiz'))
        else:
            return redirect(url_for('quiz.result'))

    return render_template('quiz.html', form=form, question=question)

@quiz_bp.route('/result')
def result():
    answers = session.get('answers', {})
    score = 0
    total = Question.query.count()

    for q_id, user_answer in answers.items():
        q = Question.query.get(int(q_id))
        if q and q.correct_option == user_answer:
            score += 1

    return render_template('result.html', score=score, total=total)
