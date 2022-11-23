from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from recipe_collection.models import Recipe
from recipe_collection.forms import RecipeForm
from cloudinary.forms import cl_init_js_callbacks


# Create your views here.
def home(request):
    context = {
        'recipes': Recipe.objects.order_by('-id')[0:3]
    }
    return render(request, "home.html", context)


def contact_us(request):
    return render(request, "contact-us.html", {})

def recipes(request):
    context = {
        'recipes': Recipe.objects.all().order_by('-id')
    }
    return render(request, "all-recipes.html", context)


def recipe_details(request, id):
    context = {
        'recipe': Recipe.objects.get(id=id)
    }
    return render(request, "recipe-details.html", context)


@login_required
def recipe_list(request):
    context = {
        "recipes": Recipe.objects.filter(created_by=request.user.id),
        "form": RecipeForm()
    }
    return render(request, "recipe-list.html", context)

@login_required
def new_recipe_form(request):
    context = {
        "form": RecipeForm()
    }
    return render(request, "new-recipe-form.html", context)

@login_required
def new_recipe(request):
    recipe_form = RecipeForm(request.POST, request.FILES)

    form_valid = recipe_form.is_valid()

    if form_valid:
        recipe_form = recipe_form.save(commit=False)
        recipe_form.created_by = request.user
        recipe_form.save()

    context = {
        "form_valid": form_valid
    }

    return render(request, "new-recipe.html", context)

@login_required
def delete_recipe(request, id):
    Recipe.objects.filter(id=id).delete()
    context = {
        "recipes": Recipe.objects.filter(created_by=request.user.id),
        "form": RecipeForm()
    }
    return render(request, "recipe-list.html", context)

@login_required
def update_recipe(request, id):
    recipe = Recipe.objects.filter(id=id)

    context = {
        "recipes": Recipe.objects.all(),
        "form": RecipeForm(instance=recipe[0]),
        "recipe_id": recipe[0].id
    }
    return render(request, "update-recipe.html", context)

@login_required
def edit_recipe(request):
    recipe_form = RecipeForm(request.POST, request.FILES)
    Recipe.objects.filter(id=request.POST["id"]).delete()

    form_valid = recipe_form.is_valid()

    if form_valid:
        # recipe= Recipe.objects.get(id=request.POST["id"])
        # recipe.name = request.POST["name"]
        # recipe.photo = request.POST["photo"]
        # recipe.short_description = request.POST["short_description"]
        # recipe.preparation_guide = request.POST["preparation_guide"]
        # recipe.difficulty = request.POST["difficulty"]
        # recipe.ideal_for = request.POST["ideal_for"]
        # recipe.preparation_time = request.POST["preparation_time"]
        # recipe.ingredients = request.POST["ingredients"]
        recipe_form.save()

    return render(request, "edit-recipe.html", { "form_valid": form_valid })
