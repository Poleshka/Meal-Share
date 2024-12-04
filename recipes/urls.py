from .views import AddRecipe, Recipes
from django.urls import path

urlpatterns = [
    path('', AddRecipe.as_view(), name="add_recipe"),
    path('recipes/', Recipes.as_view(), name="recipes"),

]