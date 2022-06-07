from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class emailForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(max=50)])
    email = StringField('email', validators=[DataRequired(), Length(max=50)])
    message = TextAreaField('message', validators=[DataRequired()])

