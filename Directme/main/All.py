
from flask_login import current_user,login_required
from flask import render_template,redirect,url_for,Blueprint
from Directme.main.form import MyLocate_form

main=Blueprint('main',__name__)


@main.route('/homepage',methods=["GET","POST"])
@login_required
def home():
    if current_user.is_authenticated:
        return render_template("home.html")
    return render_template("index.html")

@main.route('/',methods=["GET","POST"])
def index():
    return render_template("index.html")


@main.route('/locate',methods=["GET","POST"])
def locate():
    form=MyLocate_form()
    if form.validate_on_submit():
        return redirect(url_for('main.home'))
    return render_template("locate.html",title="Mywebsite",form=form)
    
