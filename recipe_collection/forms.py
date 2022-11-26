from django import forms
from recipe_collection.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
          'name',
          'photo_cloudinary',
          'short_description',
          'preparation_guide',
          'difficulty',
          'ideal_for',
          'preparation_time',
          'ingredients',
          'created_by',
        ]
        widgets = {
          'name': forms.TextInput(attrs={'class': 'form-control w-50'}),
          'short_description': forms.Textarea(attrs={'class': 'form-control w-50'}),
          'preparation_guide': forms.Textarea(attrs={'class': 'form-control w-50'}),
          'difficulty': forms.TextInput(attrs={'class': 'form-control w-50'}),
          'ideal_for': forms.TextInput(attrs={'class': 'form-control w-50'}),
          'preparation_time': forms.TextInput(attrs={'class': 'form-control w-50'}),
          'ingredients': forms.TextInput(attrs={'class': 'form-control w-50'}),
          'created_by': forms.HiddenInput()
        }
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['created_by'].required = False
        self.fields['photo_cloudinary'].required = False