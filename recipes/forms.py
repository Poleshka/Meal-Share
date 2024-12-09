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
        widgets = { 'ingredients':SummernoteWidget,}

        # ingredients = forms.CharField(SummernoteTextFormField)
        # description = forms.CharField(SummernoteTextFormField)
        
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ['body',]