from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
# vai crir um arquivo.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# secrets, você pode pegar o secrets.token_hex(16)
app.config['SECRET_KEY'] = 'random-caracteres'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
lg = LoginManager(app)
lg.login_view = 'login'
lg.login_message_category = 'info'


# importação de rotas.
from app import routes
