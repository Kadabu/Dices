from django.db import models

# Create your models here.
class Roll(models.Model):

    dice_1 = models.IntegerField()
    dice_2 = models.IntegerField()
    dice_3 = models.IntegerField()
    dice_4 = models.IntegerField()
    dice_5 = models.IntegerField()
    game_no = models.IntegerField(unique=True)


class Scores(models.Model):

    total = models.IntegerField()
    dices_amount = models.IntegerField()
    player_no = models.IntegerField(unique=True)
