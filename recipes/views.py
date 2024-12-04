from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Recipe
from .forms import RecipeForm 


# Create your views here.

class Recipes(ListView):
    """View all recipies"""
    template_name = 'recipes/recipes.html'
    model = Recipe
    context_object_name = 'recipes'


class RecipeDetail(DetailView):
    template_name = 'recipes/recipe_detail.html'
    model = Recipe
    context_object_name = 'recipe'

class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    form_class =RecipeForm
    #fields = ['title', 'ingredients', 'description']  replace these with the fields form your model. 
    success_url = reverse_lazy('recipes')
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe,self).form_valid(form)

    
