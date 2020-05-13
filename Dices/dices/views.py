from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Roll
from .forms import Game1ChoiceForm
import random

# Create your views here.
class Start(TemplateView):

    template_name = 'start.html'


class Game1(View):

    def get(self, request):
        form = Game1ChoiceForm()
        numbers = [random.randrange(1,7) for x in range(5)]
        roll = Roll.objects.create(dice_1=numbers[0], dice_2=numbers[1], dice_3=numbers[2], dice_4=numbers[3], dice_5=numbers[4])
        return render(request, "game_1_start.html", {"roll": roll, "form": form, "numbers": numbers})

    def post(self, request):
        """Obliczanie wyniku na podstawie wyboru z formularza i przekierowanie do strony, gdzie gracz wybiera, czy rzuca dalej"""
        form = Game1ChoiceForm(request.POST)
        return HttpResponseRedirect('/start/')
