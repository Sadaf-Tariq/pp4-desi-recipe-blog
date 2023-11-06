from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.full_recipe, name='full_recipe'),
    path('like/<slug:slug>', views.recipe_like, name='recipe_like'),
]
