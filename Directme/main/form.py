
from flask_wtf import FlaskForm,Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class MyLocate_form(FlaskForm):
    country=StringField("Country",validators=[DataRequired()])
    state=StringField("State",validators=[DataRequired()])
    submit=SubmitField('Search')

class MySearch_form(FlaskForm):
    search=StringField("Search",validators=[DataRequired()])
    submit=SubmitField('Search')