from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class Addform(FlaskForm):
    name = StringField('Name of Puppy: ')
    submit = SubmitField('Submit')

class Delform(FlaskForm):
    id = IntegerField('ID number of Puppy to remove: ')
    submit = SubmitField('Submit')

class Owneraddform(FlaskForm):  
    name = StringField('Enter name of the Owner: ')  
    pup_id = IntegerField('Enter ID of Puppy: ')
    submit = SubmitField('Submit')
