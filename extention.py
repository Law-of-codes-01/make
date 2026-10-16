from flask import Flask,url_for,redirect,render_template
from flask_sqlalchemy import SQLAlchemy,model
from flask_bcrypt import Bcrypt
from flask_login import UserMixin