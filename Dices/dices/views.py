from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
#from .models import
from .forms import Game1Form
import random

# Create your views here.

class Game1(View):

    def get(self, request):
        form = Game1Form()
        return render(request, "game_1_start.html")

    def post(self, request):
        numbers = [random.randrange(1,6) for x in range(6)]
        result = 0
        return render(request, "game_1_result.html", {"result": result, "numbers": numbers})
