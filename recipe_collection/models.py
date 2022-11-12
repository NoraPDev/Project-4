from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    short_description = models.TextField(default="")
    preparation_guide = models.TextField()
    difficulty = models.CharField(max_length=255)
    ideal_for = models.CharField(max_length=255)
    preparation_time = models.IntegerField(verbose_name="Preparation time (in minutes)")
    ingredients = models.TextField(max_length=255)

    def __str__(self):
        return self.name
