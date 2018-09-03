import os


class Config(object):
    # vai crir um arquivo.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # secrets, você pode pegar o secrets.token_hex(16)
    SECRET_KEY = 'random-caracteres'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_USERNAME = "danielmachadopintos@gmail.com"
    MAIL_PASSWORD = "1234"