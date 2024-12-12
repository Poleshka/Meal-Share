from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    List fields for display in admin,
    fields for search,fields filters and rich-text editor.
    """

    list_display = ('title', 'posted_on')
    search_fields = ['title', 'updated_at']
    summernote_fields = ('description',)