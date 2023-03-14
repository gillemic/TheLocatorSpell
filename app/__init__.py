from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman

# import SQLAlchemy so we can use it later
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    bootstrap = Bootstrap(app)

    from . import models

    Talisman(app, content_security_policy=None)

    with app.app_context():
        db.create_all()

    return app