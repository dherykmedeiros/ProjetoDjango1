from django.contrib import admin
from django.urls import path
from recipes.views import home, recipe, category, search, RecipeCreateView

urlpatterns = [
        path('', home, name='recipes-home'), #Home
        path('recipes/<int:id>/', recipe, name='recipes-recipe'), #Recipes
        path('recipes/category/<int:category_id>/', category, name='recipes-category'), #Categories
        path('recipes/search/', search, name='search'), #Search
        path('recipes/new/', RecipeCreateView.as_view(), name='recipe_create'),
]