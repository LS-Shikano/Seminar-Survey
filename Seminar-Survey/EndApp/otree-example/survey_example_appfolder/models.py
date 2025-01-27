from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

#this is where we would import andy extra functions or packages we need from python
import random 

author = 'Richard Neureuther, Julia Schleißheimer, Mariia Pyvovar'
doc = '''These are the demographics for the Candidates Pictures group of the 
"Designing and implementing online survey experiments" seminar.'''

class Constants(BaseConstants):
    name_in_url = 'survey-example'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass
        
class Group(BaseGroup):
   pass


class Player(BasePlayer):
    #this is the most important feature of this file. We can collect all the variables used on the html pages here

    #Gender
    gender = models.IntegerField(initial=-999, blank=False)

    #Age
    age_question = models.IntegerField(
        label="<b>Wann sind Sie geboren? </b> <br> Bitte geben Sie Ihr Geburtsjahr an.",
        min=1900, 
        max=2007
    )

    #Academic
    academic_level = models.IntegerField(initial=-999, blank=False)

    #State of residence 
    state = models.IntegerField(initial=-999, blank=False)

    #Political self-placement 
    political = models.IntegerField(
    label="<b>Wo würden Sie sich selbst einordnen?</b>",
    choices=[(1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
    ],
    widget=widgets.RadioSelectHorizontal,
    initial=1, 
    )

