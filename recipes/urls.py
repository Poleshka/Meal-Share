from .views import AddRecipe, Recipes, RecipeDetail
from django.urls import path

urlpatterns = [
    path('add', AddRecipe.as_view(), name="add_recipe"),
    path('', Recipes.as_view(), name="recipes"),
    path('<slug:pk>/', RecipeDetail.as_view(), name="recipe_detail"),
]