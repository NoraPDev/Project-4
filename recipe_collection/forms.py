from django import forms
from recipe_collection.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
          'name',
          'photo',
          'short_description',
          'preparation_guide',
          'difficulty',
          'ideal_for',
          'preparation_time',
          'ingredients'
        ]
        widgets = {
          'name': forms.TextInput(attrs={'class': 'form-control w-50'}),
          'photo': forms.TextInput(attrs={'class': 'form-control w-50'}),
          'short_description': forms.TextInput(attrs={'class': 'form-control w-50'}),
          'preparation_guide': forms.TextInput(attrs={'class': 'form-control w-50'}),
          'difficulty': forms.TextInput(attrs={'class': 'form-control w-50'}),
          'ideal_for': forms.TextInput(attrs={'class': 'form-control w-50'}),
          'preparation_time': forms.TextInput(attrs={'class': 'form-control w-50'}),
          'ingredients': forms.TextInput(attrs={'class': 'form-control w-50'})
        }