from django import forms
from main.models import Recipe

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