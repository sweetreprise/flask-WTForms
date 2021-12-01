from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, NumberRange, Optional

class PetForm(FlaskForm):
    """form for adding pets"""

    name = StringField("Name", validators=[InputRequired('Please enter a name')])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo", validators=[URL('Please enter a valid URL'), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message='Please enter an age between 0 and 30'), Optional()])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """form for editing pets"""

    photo_url = StringField("Photo", validators=[URL('Please enter a valid URL'), Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available?")
