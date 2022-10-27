from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.TextField()

class Recipes(models.Model):
    name = models.TextField()
    photo = models.TextField()
    preparation_guide = models.TextField()
    difficulty = models.TextField()
    ideal_for = models.TextField()
    preparation_time = models.TextField()
