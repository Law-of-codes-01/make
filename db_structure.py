import os
from __init__ import db,login_manager
from flask import current_app
from flask_login import UserMixin
from datetime import datetime
from itsdangerous import URLSafeTimedSerializer as srz
from itsdangerous import BadSignature, SignatureExpired


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), unique=False, nullable=False)
    lastname = db.Column(db.String(100), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone= db.Column(db.String(15), unique=True, nullable=True)
    password = db.Column(db.String(300), nullable=False)
    country = db.Column(db.String(200), nullable=False)
    gender=db.Column(db.String(10), nullable=True)
    bio=db.Column(db.String(200), nullable=True)
    whatsapp=db.Column(db.String(15), unique=True, nullable=True)
    whatsappnum=db.Column(db.String(15), unique=True, nullable=True)
    user_img = db.Column(db.String(3000), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_token(self):
        s = srz(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_token(token, expire_sec=1800):
        s = srz(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token, max_age=expire_sec)
            user_id = data['user_id']   
        except (BadSignature, SignatureExpired):
            return None
        return db.session.get(User, user_id)

    def __repr__(self):
        return f'User("{self.username}","{self.id}","{self.phone}","{self.email}","{self.user_img}","{self.country}","{self.password}")'


class Post(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    media_type = db.Column(db.String(300), nullable=False)   # 'text' | 'image' | 'video' | 'voice'
    title = db.Column(db.String(100), nullable=True)
    content = db.Column(db.Text, nullable=True)              # for text posts / captions
    media_path = db.Column(db.String(1000), nullable=True)   # filename for image/video/voice
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Post("{self.media_type}","{self.id}","{self.date_posted}")'