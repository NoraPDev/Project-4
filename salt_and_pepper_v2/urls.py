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
    path('recipe-details/<int:id>/', Views.recipe_details),
    path('delete-recipe/<int:id>/', Views.delete_recipe),
    path('update-recipe/<int:id>/', Views.update_recipe),
    path('edit-recipe/', Views.edit_recipe),
    path('recipe-list/', Views.recipe_list),
    path('stored-recipe/', Views.new_recipe),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', Views.home)
]
