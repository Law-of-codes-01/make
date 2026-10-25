

import os

class Lawconfig:
    SECRET_KEY = os.environ.get("Describeit_secrete")
    _uri = os.environ.get("lawdb", "sqlite:///site.db")
    if _uri.startswith("postgres://"):
        _uri = _uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = _uri

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("Describeit_email")
    MAIL_PASSWORD = os.environ.get("Describeit_pass")
    MAIL_DEFAULT_SENDER = os.environ.get("Describeit_email")
