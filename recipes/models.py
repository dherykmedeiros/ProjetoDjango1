from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65) #VARCHAR(65)

    def __str__(self):
        return self.name #método mágico para nomear o model na interface



class Recipe(models.Model):
    title = models.CharField(max_length=65) #VARCHAR(65)
    description = models.CharField(max_length=165) #VARCHAR(165)
    slug = models.SlugField(unique=True) #VARCHAR
    preparation_time = models.IntegerField() #INTEGER
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField() #INTEGER
    servings_unit = models.CharField(max_length=65) #VARCHAR(65)
    preparation_steps = models.TextField() #TEXT
    preparation_steps_is_html = models.BooleanField(default=False) #BOOLEAN
    created_at = models.DateTimeField(auto_now_add=True) #TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) #TIMESTAMP
    is_published = models.BooleanField(default=False) #BOOLEAN
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/') #VARCHAR
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None
        ) #VARCHAR(65)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
        ) #VARCHAR

    def __str__(self):
        return self.title #método mágico para nomear o model na interface





