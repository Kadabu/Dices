from django import forms
from django.contrib.auth.models import User
from .models import Roll



class Game1ChoiceForm(forms.ModelForm):
    class Meta:
        model = Roll
        fields = '__all__'
