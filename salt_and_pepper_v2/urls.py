"""salt_and_pepper_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import recipe_collection.views as Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', Views.recipes, name="recipes"),
    path('recipe-details/<int:id>/', Views.recipe_details, name="recipe_details"),
    path('delete-recipe/<int:id>/', Views.delete_recipe, name="delete_recipe"),
    path('update-recipe/<int:id>/', Views.update_recipe, name="update_recipe_form"),
    path('new-recipe/', Views.new_recipe_form, name="new_recipe_form"),
    path('edit-recipe/', Views.edit_recipe, name="edit_recipe_process"),
    path('stored-recipe/', Views.new_recipe, name="new_recipe_process"),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', Views.recipe_list, name="profile_page"),
    path('', Views.home, name="home")
]
