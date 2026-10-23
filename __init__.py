
from extention import Flask,SQLAlchemy,Bcrypt
from flask_login import LoginManager
from flask_mail import Mail 
from Directme.lawconfig import Lawconfig


db=SQLAlchemy()
hsh=Bcrypt()
mail=Mail()
login_manager=LoginManager()
login_manager.login_view="user.login"



def create_app(law_class=Lawconfig):
    LAW=Flask(__name__,template_folder="mytemp")

    LAW.config.from_object(law_class)
    db.init_app(LAW)
    hsh.init_app(LAW)
    mail.init_app(LAW)
    login_manager.init_app(LAW)

    from Directme.user.All import user
    from Directme.post.All import posts
    from Directme.main.All import main
    LAW.register_blueprint(user)
    LAW.register_blueprint(posts)
    LAW.register_blueprint(main)


    return LAW

def create_db():
    law=create_app()
    with law.app_context():
        db.create_all()



        
