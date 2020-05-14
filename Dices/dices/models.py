from django.db import models

# Create your models here.
class Roll(models.Model):

    dice_1 = models.IntegerField()
    dice_2 = models.IntegerField()
    dice_3 = models.IntegerField()
    dice_4 = models.IntegerField()
    dice_5 = models.IntegerField()
    game_no = models.IntegerField(unique=True)
