from flask_wtf import FlaskForm
from wtforms.validators import Required,Email, DataRequired
from wtforms import SubmitField,TextAreaField,SelectMultipleField



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    gas = SelectMultipleField ('Check the types of gas you have', choices =[('TotalGaz6KG','TotalGaz6KG'),('TotalGaz13Kg','TotalGaz13KG'),('TotalGaz22kg','TotalGaz22KG'),('TotalGaz50Kg','TotalGaz50Kg'),('ShellAfrigas6KG','ShellAfrigas6KG'),('ShellAfrigas13KG','ShellAfrigas13KG'),('ShellAfrigas22KG','ShellAfrigas22KG'),('ShellAfrigas45KG','ShellAfrigas45KG'),('k-Gas6Kg','k-Gas6Kg'),('k-Gas13Kg','k-Gas13Kg'),('k-Gas22Kg','k-Gas22Kg'),('k-Gas50Kg','k-Gas50Kg')])
    submit = SubmitField('Submit')
    
class LocationForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Submit')
