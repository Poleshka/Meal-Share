from django import forms
from .models import Recipe
from django_summernote import SummernoteTextField

class RecipeForm(forms.ModelForm):
    """ Form to create a recipe"""
    class Meta:
        model= Recipe
        fields= ['title','ingredients','description','image','image_alt']

        
