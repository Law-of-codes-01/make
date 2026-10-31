import os

import secrets
from flask import url_for,current_app
from __init__ import mail
from flask_mail import Message
import cloudinary
import cloudinary.uploader



cloudinary.config(
    cloud_name=os.environ.get("cloud_id"),
    api_key=os.environ.get("cloud_Api_Key"),
    api_secret=os.environ.get("cloud_Api_secret"),
    secure=True
)

def save_pic(s_pic):
    result = cloudinary.uploader.upload(
        s_pic,
        public_id=secrets.token_hex(8),
        folder="profile_pics",
        resource_type="auto",
    )
    return result["secure_url"]

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
