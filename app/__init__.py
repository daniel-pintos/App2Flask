from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
lg = LoginManager()
lg.login_view = 'users.login'
lg.login_message_category = 'info'
mail = Mail()


def create_app(config_Class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    lg.init_app(app)
    mail.init_app(app)

    # importação de rotas.
    from app.main.routes import main
    from app.posts.routes import posts
    from app.users.routes import users
    from app.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
