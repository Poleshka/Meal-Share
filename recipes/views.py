from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
CreateView, ListView,
DeleteView, UpdateView)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm

# Create your views here.

class Recipes(ListView):
    """View all recipies"""
    template_name = 'recipes/recipes.html'
    model = Recipe
    context_object_name = 'recipes'


def recipe_detail(request, pk):
    """Display an individual :model:'recipe'.
    **Context**
    ``recipe``
        The most recent instance of :model:`recipe`.
        ``Comments``
            All aproved comments related to the recipe.
            ``comment_form``
            An instance of :form:recipe.CommentForm.

     **Template**
    :template:`recipe_detail.html`
    """
    queryset = Recipe.objects.filter(status=1)
    recipe= get_object_or_404(Recipe, pk=pk)
    # Get all the comments for this recipe, ordered by the creation date
    comments= recipe.comments.all().order_by("-created_on")
    # Count only approved comments
    comment_count= recipe.comments.filter(approved=True).count()
    comment_form = CommentForm
    
    # Handle POST request for comment submission
    if request.method == "POST":
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
        if not recipe.image:
            recipe.image = 'images/file.jpg'
    return render(request, 'recipes/recipe_detail.html', {
            'recipe': recipe,
            'comments':comments,
            'comment_form' :comment_form  
    })


class AddRecipe(LoginRequiredMixin, CreateView):
    """Add Recipe"""
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    form_class =RecipeForm
    #fields = ['title', 'ingredients', 'description']  replace these with the fields form your model. 
    success_url = reverse_lazy('recipes')

    def get_success_url(self):
        # return reverse('recipe_detail', kwargs={'pk': self.object.id})
        messages.success(self.request, "Your recipe been added!")
        return reverse('recipe_detail', kwargs={'pk': self.object.id})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe,self).form_valid(form)

class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Recipe"""
    template_name = 'recipes/edit_recipe.html'
    form_class = RecipeForm
    model = Recipe

    def get_success_url(self):
        # return reverse('recipe_detail', kwargs={'pk': self.object.id})
        messages.success(self.request, "Your recipe has been updated successfully!")
        return reverse('recipe_detail', kwargs={'pk': self.object.id})

    def test_func(self):
        return self.request.user == self.get_object().user

class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """DElete Recipe"""
    model= Recipe
    success_url= '/recipes/'

    def get_success_url(self):
        messages.success(self.request, "Your recipe has been deleted successfully!")
        return self.success_url

    def test_func(self):
        return self.request.user == self.get_object().user


