from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ManufacturerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description')
    country = StringField('Country')
    certificates = StringField('Certificates')
    submit = SubmitField('Add Manufacturer')
