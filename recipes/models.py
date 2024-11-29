from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, related_name='recipe_author', on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    description = models.TextField()
    posted_on = models.DateTimeField(auto_now=True) 
    updated_at = models.DateTimeField(auto_now=True)
    image = ResizedImageField(size=[400,None], quality= 75, upload_to='recipes/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering= ["-posted_on"]
