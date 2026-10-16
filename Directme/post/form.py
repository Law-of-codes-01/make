from flask_wtf import FlaskForm,Form
from wtforms import StringField,FileField,TextAreaField,SubmitField
from wtforms.validators import DataRequired



class MyPost_form(FlaskForm):
    title=StringField("Title",validators=[DataRequired()])
    media=FileField("Video/photos",validators=[DataRequired()])
    content=TextAreaField("What is on your mind",validators=[DataRequired()])

    submit=SubmitField('Post')

class Updatepost_form(FlaskForm):
    title=StringField("Title",validators=[DataRequired()])
    content=TextAreaField("What is on your mind",validators=[DataRequired()])
    submit=SubmitField('Update')