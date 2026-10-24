
from flask_login import current_user,login_required,logout_user,login_user
from __init__ import hsh
from flask import render_template,redirect,url_for,flash,abort,Blueprint
from Directme.user.form import MySignin_form,MySignup_form,EditProfile,MyReq_form,MyReset_form,MyContact_form
from db_structure import db,User,Post
from Directme.user.func import send_email,send_mail,save_pic
from flask_login import login_required

user=Blueprint('user',__name__)

@user.route('/signup',methods=["GET","POST"])
def create():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form=MySignup_form()
    if form.validate_on_submit():
        # send_mail(form)
        hash_pass=hsh.generate_password_hash(form.userpass.data).decode("utf-8")
        user=User(firstname=form.firstname.data,lastname=form.lastname.data,
                  gender=form.usergender.data,username=form.username.data,
                  phone=form.userphone.data,email=form.useremail.data,
                  country=form.usercountry.data,
                  password=hash_pass)
        db.session.add(user)
        db.session.commit()
        print(user)
        return redirect(url_for('user.login'))
    print(form.errors)
    
    return render_template("signup.html",title="Mywebsite",form=form)

@user.route('/signin',methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form=MySignin_form()
    if form.validate_on_submit():
        user_em=User.query.filter_by(email=form.useremail.data).first()
        if user_em:
            user_p=hsh.check_password_hash(user_em.password,form.userpass.data)
            if user_em and user_p:
                login_user(user_em,remember=form.remember.data)
                flash("Login succesfully")
                return redirect(url_for('main.home'))
        return redirect(url_for("user.login"))
    return render_template("signin.html",title="Mywebsite",form=form)

@user.route('/logout')
def logout():
        logout_user()
        return redirect(url_for("user.login"))




@user.route('/profile/<string:username>',methods=["GET","POST"])
@login_required
def profile(username):
    cont=MyContact_form()
    user = User.query.filter_by(username=username).first_or_404()
    image_file = https://res.cloudinary.com/gy6px9jz/image/upload/f_auto/q_auto/profile_pics/+ user.user_img
    if user:
        # if user.whatsappnum==None or user.whatsapp==None:
        #     return redirect(url_for('user.contact',username=username))
        whatsappnum=user.whatsappnum
        whatsapp=user.whatsapp
        post= (Post.query
                .filter_by(user_id=user.id)
                .order_by(Post.date_posted.desc())
                .all())

        return render_template("profile.html", user=user, img_f=image_file, posts=post,cont=cont,phone=whatsappnum,whatsapp=whatsapp)
    return render_template("profile.html", user=user, img_f=image_file, posts=post,cont=cont,phone=whatsappnum,whatsapp=whatsapp)


@user.route('/editprofile',methods=["GET","POST"])
def editprofile():

    if current_user.is_authenticated:
        form=EditProfile()
        if form.validate_on_submit():
            if form.pic.data:
                pcs=save_pic(form.pic.data)
                db.session.commit()
                current_user.user_img=pcs
            current_user.username=form.username.data
            current_user.email=form.email.data
            current_user.bio=form.bio.data
            current_user.country=form.country.data
            current_user.phone=form.phone.data

            db.session.commit()
            return redirect(url_for('user.profile',username=current_user.username))
        form.username.data=current_user.username
        form.email.data=current_user.email
        form.bio.data=current_user.bio
        form.country.data=current_user.country
        form.phone.data=current_user.phone
        image_file=url_for("static",filename="images/"+current_user.user_img)
        print(form.errors)
        return render_template("edtprofile.html",form=form,img_f=image_file)

@user.route('/passwordreset',methods=["GET","POST"])
def token_req():
    if current_user.is_authenticated:
        return redirect(url_for("user.logout"))
    form=MyReq_form()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user:
            send_email(user)
            return redirect(url_for("user.login"))
        flash("Invalid or expired token")
    return render_template("req.html",form=form,title="Email Verification")


@user.route('/verifytoken/reset/<token>', methods=["GET", "POST"])
def reset(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    user = User.verify_token(token)
    if user is None:
        flash("Invalid or expired token")
        return redirect(url_for("user.token_req"))

    form = MyReset_form()
    if form.validate_on_submit():
        user.password = hsh.generate_password_hash(form.userpass.data)
        form.userc_pass=user.password
        db.session.commit()
        flash("Password updated. Please log in.")
        return redirect(url_for("user.login"))

    return render_template("reset.html", form=form)


@user.route('/contact/<string:username>',methods=["GET","POST"])
def contact(username):
    form=MyContact_form() 
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first_or_404()
        if user:
            user.whatsappnum=form.phone.data
            user.whatsapp=form.whatsapp.data
            db.session.commit()
        return redirect(url_for('main.home'))
    print(form.errors)

    return render_template("contact.html",form=form)


@user.route('/editcontact',methods=["GET","POST"])
def editcontact():

    if current_user.is_authenticated:
        form=MyContact_form()
        if form.validate_on_submit():
            current_user.whatsappnum=form.phone.data
            current_user.whatsapp=form.whatsapp.data

            db.session.commit()
            return redirect(url_for('user.profile',username=current_user.username))
        form.phone.data=current_user.whatsappnum

        form.whatsapp.data=current_user.whatsapp
        print(form.errors)
        return render_template("editcontact.html",form=form)
