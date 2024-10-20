from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BrandForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    logo = StringField('Logo URL', validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Add Brand')
