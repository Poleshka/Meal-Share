from django import forms
from .models import Recipe,Comment
from django_summernote.fields import SummernoteTextFormField
from django_summernote.widgets import SummernoteWidget

class RecipeForm(forms.ModelForm):
    """ Form to create a recipe"""
    class Meta:
        model= Recipe
        fields= [
            'title',
            'ingredients',
            'description',
            'image'
            ]
        widgets = { 'ingredients':SummernoteWidget}

class CommentForm(forms.ModelForm):
    """Form to add comment to recipes"""
    class Meta:
        model= Comment
        fields = ['body',]