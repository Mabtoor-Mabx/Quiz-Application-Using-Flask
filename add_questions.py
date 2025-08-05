from app import create_app, db
from app.models.models import Question

app = create_app()
with app.app_context():

    db.create_all()

    if Question.query.count() == 0:
        sample_questions = [
            Question(question_text="What is the output of print(2 ** 3)?",
                     option_a="5", option_b="6", option_c="8", option_d="9", correct_option="C"),
            Question(question_text="Who invented Python programming?",
                     option_a="Dennis Ritchie", option_b="Guido van Rossum", option_c="James Gosling", option_d="Mark Zuckerberg", correct_option="B"),
            Question(question_text="Which keyword is used for function in Python?",
                     option_a="function", option_b="def", option_c="fun", option_d="define", correct_option="B"),
            Question(question_text="Which planet is known as the Red Planet?",
                     option_a="Earth", option_b="Venus", option_c="Mars", option_d="Jupiter", correct_option="C"),
            Question(question_text="What is the capital of France?",
                     option_a="Rome", option_b="Madrid", option_c="Berlin", option_d="Paris", correct_option="D"),
            Question(question_text="Which data type is immutable in Python?",
                     option_a="List", option_b="Dictionary", option_c="Set", option_d="Tuple", correct_option="D"),
            Question(question_text="What is the largest ocean on Earth?",
                     option_a="Indian Ocean", option_b="Pacific Ocean", option_c="Atlantic Ocean", option_d="Arctic Ocean", correct_option="B"),
            Question(question_text="Which language is used for web apps?",
                     option_a="PHP", option_b="Python", option_c="JavaScript", option_d="All of the above", correct_option="D"),
            Question(question_text="What is 7 * 6?",
                     option_a="36", option_b="42", option_c="48", option_d="56", correct_option="B"),
            Question(question_text="Which command is used to install packages in Python?",
                     option_a="install", option_b="get", option_c="pip", option_d="fetch", correct_option="C"),
        ]

        db.session.bulk_save_objects(sample_questions)
        db.session.commit()
        print("Questions added successfully!")
    else:
        print("Questions already exist in the database.")
