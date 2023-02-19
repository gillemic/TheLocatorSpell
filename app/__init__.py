from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman

# db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)

# db.init_app(app)

bootstrap = Bootstrap(app)

from app import routes, errors