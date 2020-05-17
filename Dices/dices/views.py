from django.http import HttpResponseRedirect
from django.shortcuts import render #get_object_or_404
from django.views import View
#from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from .models import Roll, Scores
from .forms import Game1ChoiceForm
import random

# Create your views here.
class Start_Game(View):

    def get(self, request):
        Scores.objects.all().delete()
        Scores.objects.create(total=0, player_no=1)
        return HttpResponseRedirect('/start/')


class Start(View):

    def get(self, request):
        numbers = [random.randrange(1,7) for x in range(5)]
        Roll.objects.all().delete()
        Roll.objects.create(dice_1=numbers[0], dice_2=numbers[1], dice_3=numbers[2], dice_4=numbers[3], dice_5=numbers[4], game_no=1)
        scores = Scores.objects.get(player_no=1)
        return render(request, "start.html", {"scores": scores})


class Game1(View):

    def get(self, request):
        form = Game1ChoiceForm()
        roll = Roll.objects.get(game_no=1)
        #zdefiniować zupę (if roll.dice_1 != roll.dice_2 itd.); jeśli zupa, wyświetlić zupa.html
        return render(request, "game_1_start.html", {"form": form, "roll": roll})

    def post(self, request):
        """Obliczanie wyniku na podstawie wyboru z formularza i przekierowanie do strony, gdzie gracz wybiera, czy rzuca dalej"""
        form = Game1ChoiceForm(request.POST)
        roll = Roll.objects.get(game_no=1)
        #zdefiniować błędy w formularzu, tj. niedopuszczalne wybory (odwołując się dp chosen_numbers)
        if form.is_valid():
            put_aside = form.cleaned_data['put_aside']
            chosen_numbers = []
            result = 0
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
            """Count the result"""
            if len(chosen_numbers) == 5:
                if len(set(chosen_numbers)) == 1:
                    if 1 in chosen_numbers:
                        result += 400
                    elif 5 in chosen_numbers:
                        result += 200
                    else:
                        result += 120
                elif len(set(chosen_numbers)) == 2:
                    if chosen_numbers.count(1) == 4 and 5 in chosen_numbers:
                        result += 205
                    elif chosen_numbers.count(1) == 3 and 5 in chosen_numbers:
                        result += 110
                    elif chosen_numbers.count(1) == 2 and 5 in chosen_numbers:
                        result += 70
                    elif chosen_numbers.count(1) == 1 and 5 in chosen_numbers:
                        result += 110
                    elif chosen_numbers.count(1) == 2 and 5 not in chosen_numbers:
                        result += 50
                    elif chosen_numbers.count(5) == 2 and 1 not in chosen_numbers:
                        result += 40
                    elif chosen_numbers.count(1) == 1 and 1 not in chosen_numbers:
                        result += 70
                    elif chosen_numbers.count(5) == 1 and 5 not in chosen_numbers:
                        result += 65
                    else:
                        return HttpResponseRedirect('/game_1/')#komunikat o błędzie w formularzu - jak wyświetlić???
                elif len(set(chosen_numbers)) == 3:
                        if 1 in chosen_numbers and 5 in chosen_numbers:
                            result += 45
                        else:
                            return HttpResponseRedirect('/game_1/')  #komunikat o błędzie w formularzu
                elif len(set(chosen_numbers)) == 4:
                    return HttpResponseRedirect('/game_1/') #komunikat o błędzie w formularzu
                elif len(set(chosen_numbers)) == 5:
                    return HttpResponseRedirect('/game_1/') #komunikat o błędzie w formularzu
            elif len(chosen_numbers) == 4:
                if len(set(chosen_numbers)) == 1:
                    if 1 in chosen_numbers:
                        result += 200
                    elif 5 in chosen_numbers:
                        result += 100
                    else:
                        result += 60
                elif len(set(chosen_numbers)) == 2:
                    if chosen_numbers.count(1) == 3 and 5 in chosen_numbers:
                        result += 105
                    elif chosen_numbers.count(1) == 2 and 5 in chosen_numbers:
                        result += 30
                    elif chosen_numbers.count(5) == 3 and 1 in chosen_numbers:
                        result += 60
                    elif chosen_numbers.count(5) == 4:
                        result += 100
                    elif 1 in chosen_numbers and 5 not in chosen_numbers:
                        result += 40
                    elif 5 in chosen_numbers and 1 not in chosen_numbers:
                        result += 35
                    else:
                        return HttpResponseRedirect('/game_1/') #komunikat o błędzie w formularzu
                elif len(set(chosen_numbers)) == 3:
                    return HttpResponseRedirect('/game_1/')#komunikat o błędzie w formularzu
                elif len(set(chosen_numbers)) == 4:
                    return HttpResponseRedirect('/game_1/')#komunikat o błędzie w formularzu
            elif len(chosen_numbers) == 3:
                if len(set(chosen_numbers)) == 1:
                    if 1 in chosen_numbers:
                        result += 100
                    elif 5 in chosen_numbers:
                        result += 50
                    else:
                        result += 30
                elif len(set(chosen_numbers)) == 2:
                    if chosen_numbers.count(1) == 2 and 5 in chosen_numbers:
                        result += 25
                    elif chosen_numbers.count(5) == 2 and 1 in chosen_numbers:
                        result += 20
                    else:
                        return HttpResponseRedirect('/game_1/') #komunikat o błędzie w formularzu
                elif len(set(chosen_numbers)) == 3:
                    return HttpResponseRedirect('/game_1/')#komunikat o błędzie w formularzu
            elif len(chosen_numbers) == 2:
                if len(set(chosen_numbers)) == 1:
                    if 1 in chosen_numbers:
                        result += 20
                    elif 5 in chosen_numbers:
                        result += 10
                    else:
                        return HttpResponseRedirect('/game_1/')#komunikat o błędzie w formularzu
                elif len(set(chosen_numbers)) == 2:
                    if 1 in chosen_numbers and 5 in chosen_numbers:
                        result += 15
                    else:
                        return HttpResponseRedirect('/game_1/')#komunikat o błędzie w formularzu
            elif len(chosen_numbers) == 1:
                if 1 in chosen_numbers:
                    result += 10
                elif 5 in chosen_numbers:
                    result += 5
                else:
                    #komunikat o błędzie w formularzu
                    return HttpResponseRedirect('/game_1/')
            scores = Scores.objects.get(player_no=1)
            print("Total: {}".format(scores.total))
            print("Chosen numbers: {}".format(chosen_numbers))
            print("Result: {}".format(result))
            scores.total += result
            scores.save()
            print("New total: {}".format(scores.total))
            return HttpResponseRedirect('/start/')
        else: #if form is not is_valid
            return HttpResponseRedirect('/game_1/') #komunikat o błędzie w formularzu/ przez form.add_error??


class Total(View):

    def get(self, request):
        return render(request, "total.html")
