from flask_wtf import FlaskForm
from wtforms import StringField,FileField,EmailField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flask_wtf.file import FileAllowed


class MySignup_form(FlaskForm):
    firstname=StringField("Firstname",validators=[DataRequired()])
    lastname=StringField("Lastname",validators=[DataRequired()])
    username=StringField("Username",validators=[DataRequired(),Length(min=3,max=8)])
    useremail=EmailField("Email address",validators=[Email(),DataRequired()])
    userphone=StringField("Phone ",validators=[Length(min=11,max=11)])
    userpass=PasswordField("Password",validators=[DataRequired(),Length(min=6,max=50)])
    usergender=StringField("Gender",validators=[DataRequired()])
    userc_pass=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo('userpass')])
    usercountry=StringField("Nationality",validators=[DataRequired(),Length(min=3,max=16)])
    submit=SubmitField('Create Account')

    def validate_username(self,username):
        from db_structure import User
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("username is taken , use a different one")

    def validate_useremail(self,useremail):
        from db_structure import User
        user=User.query.filter_by(email=useremail.data).first()
        if user:
            raise ValidationError("Email is taken , use a different one")

    def validate_userphone(self,userphone):
        from db_structure import User
        user=User.query.filter_by(phone=userphone.data).first()
        if user:
            raise ValidationError("Phone Number is taken , use a different one")



class MySignin_form(FlaskForm):
    useremail=EmailField("Email address",validators=[Email(),DataRequired()])
    userpass=PasswordField("Password",validators=[DataRequired(),Length(min=6,max=50)])
    remember=BooleanField("Remember Me")
    submit=SubmitField('Log in')

    def validate_useremail(self,useremail):
        from db_structure import User
        from __init__ import hsh
        user=User.query.filter_by(email=useremail.data).first()
        
        if user:
            user=User.query.filter_by(email=useremail.data).first()
            hash_pass=hsh.check_password_hash(user.password,self.userpass.data)
            if hash_pass ==False:
                raise ValidationError("Incorrect password")
        else:
            raise ValidationError("User do not exit ,check email or password")



class EditProfile(FlaskForm):

    pic=FileField("Update Profile Picture",
                             validators=[FileAllowed(['jpg','png'])])
    username=StringField("Update Username",
                         validators=[DataRequired(),Length(min=4,max=20)])
    email=StringField("Update Email",
                      validators=[DataRequired(),Email(),Length(min=4,max=20)])

    country=StringField("Change Nationality",
                            validators=[Length(min=4,max=20)])    

    bio=StringField("Edit Bio",
                                validators=[Length(min=10)])

    phone=StringField("Edit Phone ",validators=[Length(min=11,max=11)])

    
    submit=SubmitField("Update")


class MyReq_form(FlaskForm):
    email=StringField("Update Email",
                      validators=[DataRequired(),Email(),Length(min=4,max=20)])
    submit=SubmitField('Get Code')


class MyReset_form(FlaskForm):
    userpass=PasswordField("Password",validators=[DataRequired(),Length(min=6,max=50)])
    userc_pass=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo('userpass')])

    submit=SubmitField('Update Password')