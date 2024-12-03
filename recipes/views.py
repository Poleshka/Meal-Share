from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Recipe

# Create your views here.

class Recipes(ListView):
    """View all recipies"""
    template_name = 'recipes/recipes'
    model = Recipe
    context_object_name = 'recipes'

class AddRecipe(CreateView):
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    success_url = '/recipes/'

    def form_valid(self, form):
        form.instances.user = self.user
        return super(AddRecipe, self).form_valid(form)
