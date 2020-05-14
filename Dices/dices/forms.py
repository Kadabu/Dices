from django import forms
from django.contrib.auth.models import User
#from .models import Roll


DICES_SIDES = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    )


class Game1ChoiceForm(forms.Form):
    put_aside = forms.MultipleChoiceField(choices=DICES_SIDES, widget=forms.CheckboxSelectMultiple)
