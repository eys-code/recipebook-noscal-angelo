from django.urls import path
from .views import RecipeDetailView, RecipeListView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipes'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
]

app_name = 'ledger'