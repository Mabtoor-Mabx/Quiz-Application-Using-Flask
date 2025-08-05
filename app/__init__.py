# App Factory

# Required Libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

# Initialize Database and CSRF(Security)

db = SQLAlchemy()
csrf = CSRFProtect()

# Initalize Flask App, Databases and Keys

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Mabtoor-Mabx"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)
    csrf.init_app(app)


    from .routes.quiz_routes import quiz_bp
    app.register_blueprint(quiz_bp)

    with app.app_context():
        db.create_all()
    
    return app




