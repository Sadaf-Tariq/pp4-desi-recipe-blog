from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('createrecipe/', views.CreateNewRecipe.as_view(), name='new_recipe'),
    path('<slug:slug>/', views.full_recipe, name='full_recipe'),
    path('like/<slug:slug>', views.recipe_like, name='recipe_like'),
    path('category/<category>/', views.RecipeCatListView.as_view(), name='category'),
    path('method/<method>/', views.RecipeMethodListView.as_view(), name='method'),
    
]
