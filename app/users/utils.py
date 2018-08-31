import os
import secrets

from PIL import Image
from flask import url_for
from flask_mail import Message

from app import app, mail


# save this picture and rendimension
def save_picture(form_picture):
    # vamos randomizar o nome da função
    random_hex = secrets.token_bytes(8)
    # vamos salvar com a mesma extensao
    _, f_ext = os.path.splitext(form_picture.filename)
    # vamos concatenar
    picture_fn = random_hex + f_ext
    # vamos salvar no static folders
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    # vamos redimensionar para compactar
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    # form_picture.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='danielmachadopintos@gmail.com',
                  recipients=[user.email])
    msg.body = f"""
         To reset your password, visit the following link:
         {url_for('reset_token', token=token, _external=True)}

         If you did not make this request then simply ignore this email
    """
    mail.send(msg)
