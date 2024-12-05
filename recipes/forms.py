from django import forms
from .models import Recipe
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
