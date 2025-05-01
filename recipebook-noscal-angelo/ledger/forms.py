from django import forms
from .models import Recipe, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ["author"]

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        exclude = ["recipe"]
