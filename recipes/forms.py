# forms.py
from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title', 'description', 'preparation_time',
            'preparation_time_unit', 'servings', 'servings_unit',
            'preparation_steps', 'cover', 'category', 'is_published'
        ]
        labels = {
            'title': 'Recipe Name',
            'description': 'Description',
            'preparation_time': 'Preparation Time',
            'preparation_steps': 'Preparation Steps',
            'cover': 'Image',
            'category': 'Category',
            'is_published': 'Published?'
        }
        
