class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    gas = BooleanField ('Check the types of gas you have', validators=[Required()])
    submit = SubmitField('Submit')