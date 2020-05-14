from django.http import HttpResponseRedirect
from django.shortcuts import render #get_object_or_404
from django.views import View
#from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from .models import Roll
from .forms import Game1ChoiceForm
import random

# Create your views here.
class Start(View):

    def get(self, request):
        numbers = [random.randrange(1,7) for x in range(5)]
        Roll.objects.all().delete()
        Roll.objects.create(dice_1=numbers[0], dice_2=numbers[1], dice_3=numbers[2], dice_4=numbers[3], dice_5=numbers[4], game_no=1)
        return render(request, "start.html")


class Game1(View):

    def get(self, request):
        form = Game1ChoiceForm()
        roll = Roll.objects.get(game_no=1)
        return render(request, "game_1_start.html", {"form": form, "roll": roll})

    def post(self, request):
        """Obliczanie wyniku na podstawie wyboru z formularza i przekierowanie do strony, gdzie gracz wybiera, czy rzuca dalej"""
        form = Game1ChoiceForm(request.POST)
        roll = Roll.objects.get(game_no=1)
        #zdefiniować błędy w formularzu, tj. niedopuszczalne wybory
        if form.is_valid():
            put_aside = form.cleaned_data['put_aside']
            chosen_numbers = []
            if "1" in put_aside:
                chosen_numbers.append(roll.dice_1)
            if "2" in put_aside:
                chosen_numbers.append(roll.dice_2)
            if "3" in put_aside:
                chosen_numbers.append(roll.dice_3)
            if "4" in put_aside:
                chosen_numbers.append(roll.dice_4)
            if "5" in put_aside:
                chosen_numbers.append(roll.dice_5)
            print(chosen_numbers)
            #obliczenia
            return HttpResponseRedirect('/start/')
        else:
            return HttpResponseRedirect('/start/')#???
