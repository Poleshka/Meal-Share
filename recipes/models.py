from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from django_resized import ResizedImageField

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, related_name='recipe_author', on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    description = models.TextField()
    posted_on = models.DateTimeField(auto_now=True) 
    updated_at = models.DateTimeField(auto_now=True)
    image = ResizedImageField(size=[400,None], quality= 75, upload_to='recipes/', blank=True, null=True, default='media/file.jpg')
    image_alt = models.CharField(max_length=100, null=True, blank=True, default="Recipe image")


    def __str__(self):
        return self.title

    class Meta:
        ordering= ["-posted_on"]

class Comment(models.Model):
    """
    comment entry related to:model:'auth.User' 
    and :model:Recipe
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
