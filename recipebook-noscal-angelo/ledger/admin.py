from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Profile, Recipe, RecipeImage, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileInline,
    ]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)