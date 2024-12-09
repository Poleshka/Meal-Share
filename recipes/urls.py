from .views import AddRecipe, Recipes, DeleteRecipe, EditRecipe, recipe_detail
from django.urls import path

urlpatterns = [
    path('add/', AddRecipe.as_view(), name="add_recipe"),
    path('', Recipes.as_view(), name="recipes"),
    path('recipes/<int:pk>/', recipe_detail, name="recipe_detail"),
    path('delete/<slug:pk>/', DeleteRecipe.as_view(), name="delete_recipe"),
    path('recipes/edit/<slug:pk>/', EditRecipe.as_view(), name="edit_recipe"),
]