from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateField()

    def __str__(self):
        return self.title

class Playthroughs(models.Model):
    name = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)

    class Meta:
        unique_together = ("name", "game", "user")
    
    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    maxlvl = models.IntegerField()
    image = models.ImageField(upload_to="tracker/")

    def __str__(self):
        return self.name

class Spells(models.Model):
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    maxlvl = models.IntegerField()
    image = models.ImageField(upload_to="tracker/")

    def __str__(self):
        return self.name

class Quests(models.Model):
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
