from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Recipe

# Create your views here.

class Recipes(ListView):
    """View all recipies"""
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    context_object_name = 'recipes'

class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        print(self.request.user) 
        form.instance.user = self.request.user
        return super().form_valid(form)

    
