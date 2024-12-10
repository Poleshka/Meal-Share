from django.shortcuts import render, get_object_or_404, reverse

from django.contrib import messages
from django.views.generic import (
CreateView, ListView, 
DeleteView, UpdateView
)
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class Recipes(ListView):
    """View all recipies"""
    template_name = 'recipes/recipes.html'
    model = Recipe
    context_object_name = 'recipes'


def recipe_detail(request, pk):
    queryset = Recipe.objects.filter(status=1)
    recipe= get_object_or_404(Recipe, pk=pk)
    # Get all the comments for this recipe, ordered by the creation date
    comments= recipe.comments.all().order_by("-created_on")
    # Count only approved comments
    comment_count= recipe.comments.filter(approved=True).count()
    comment_form = CommentForm
    # Handle POST request for comment submission
    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            # Add a success message to be displayed on the page
            messages.success(request, 
                'Comment submitted and waiting approval')
        else:
            comment_form = CommentForm()
            print("About to render template")

        if not recipe.image:
            recipe.image = 'images/file.jpg'

    return render(request, 'recipes/recipe_detail.html', {
            'recipe': recipe,
            'comments':comments,
            'comment_form' :comment_form  
    })


class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    form_class =RecipeForm
    #fields = ['title', 'ingredients', 'description']  replace these with the fields form your model. 
    success_url = reverse_lazy('recipes')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe,self).form_valid(form)

class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'recipes/edit_recipe.html'
    form_class = RecipeForm
    model = Recipe
    success_url= 'recipes/'


    def test_func(self):
        return self.request.user == self.get_object().user

class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """DElete Recipe"""
    model= Recipe
    success_url= '/recipes/'

    def test_func(self):
        return self.request.user == self.get_object().user


class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    form_class =RecipeForm
    #fields = ['title', 'ingredients', 'description']  replace these with the fields form your model. 
    success_url = reverse_lazy('recipes')
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe,self).form_valid(form)

class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'recipes/edit_recipe.html'
    form_class = RecipeForm
    model = Recipe
    success_url= 'recipes/'


    def test_func(self):
        return self.request.user == self.get_object().user

class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """DElete Recipe"""
    model= Recipe
    success_url= '/recipes/'

    def test_func(self):
        return self.request.user == self.get_object().user

