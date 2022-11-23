from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    photo_cloudinary = CloudinaryField('image')
    short_description = models.TextField(default="")
    preparation_guide = models.TextField()
    difficulty = models.CharField(max_length=255)
    ideal_for = models.CharField(max_length=255)
    preparation_time = models.IntegerField(verbose_name="Preparation time (in minutes)")
    ingredients = models.TextField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
