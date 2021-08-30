from flask_wtf import FlaskForm
from wtforms.fields.html5 import DecimalRangeField
from wtforms import SubmitField, SelectField

ptypes = ['Grass', 'Fire', 'Water', 'Bug', 'Normal', 'Poison', 'Electric', 'Ground', 'Fairy', 'Fighting', 
'Psychic', 'Rock', 'Ghost', 'Ice', 'Dragon', 'Dark', 'Steel', 'Flying']

stypes = ['Poison', 'No Secondary Type', 'Flying', 'Dragon', 'Ground', 'Fairy', 'Grass', 'Fighting', 'Psychic',
 'Steel', 'Ice', 'Rock', 'Dark', 'Water', 'Electric', 'Fire', 'Ghost', 'Bug', 'Normal']

class PokeForm(FlaskForm):
    ptype = SelectField("Primary Type:",choices = ptypes)
    stype = SelectField("Secondary Type:",choices = stypes)
    attack = DecimalRangeField('Attack:')
    speed = DecimalRangeField('Speed:')
    defense = DecimalRangeField('Defense:')
    submit = SubmitField("Get Pokemon")