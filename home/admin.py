from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Comment)


