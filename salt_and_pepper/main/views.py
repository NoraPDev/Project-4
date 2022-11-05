from django.shortcuts import render
from main.models import Recipe

# Create your views here.
def home(request):
    context = {
        'recipes': Recipe.objects.order_by('-id')[0:3]
    }
    return render(request, "home.html", context)

def recipe_details(request, id):
    context = {
        'recipe': Recipe.objects.get(id=id)
    }
    return render(request, "recipe-details.html", context)