from django.db import models


class Recipe(models.Model):
    name = models.TextField()
    photo = models.TextField()
    short_description = models.TextField(default="")
    preparation_guide = models.TextField()
    difficulty = models.TextField()
    ideal_for = models.TextField()
    preparation_time = models.TextField()
    ingredients = models.TextField()

    def __str__(self):
        return self.name
