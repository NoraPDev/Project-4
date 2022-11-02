from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.TextField()
    photo = models.TextField()
    short_description = models.TextField(default="")
    preparation_guide = models.TextField()
    difficulty = models.TextField()
    ideal_for = models.TextField()
    preparation_time = models.TextField()
    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    def __str__(self):
        return self.ingredient_id.name + " - " + self.recipe_id.name
