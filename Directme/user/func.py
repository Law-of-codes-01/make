import os

import secrets
from flask import url_for,current_app
from __init__ import mail
from flask_mail import Message

def save_pic(s_pic):
    rnd_hex=secrets.token_hex(8)
    _,pth=os.path.splitext(s_pic.filename)
    pic_nm=rnd_hex + pth
    pic_path=os.path.join(current_app.root_path,'static/images',pic_nm)
    s_pic.save(pic_path)
    return pic_nm

def send_mail(user):
    msg = Message(
        subject=f"Welcome  to Describeit {user.useremail.data}",
        recipients=[user.useremail.data],
        body=f" {user.username.data}Make a perfect description for perfect reward")
    mail.send(msg)
    return "Email sent!"

def send_email(user):
    token=user.get_token()
    msg = Message(
        subject=f"Hello {user.email}",
        recipients=user.email,
        body=f"click {url_for('user.reset',token=token,_external=True)} to access your password reset page")
    mail.send(msg)
    return "Email sent!"