from django.db import models

# Create your models here.
from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    # match = models.CharField(max_length=50)
    # score = models.IntegerField()
    def __str__(self):
        return self.name


class Score(models.Model):
    score =models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.IntegerField()
    def __str__(self):
        return self.player.name + " score: " +  str(self.score)
