from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('allrecipes', views.RecipeList.as_view(), name='recipes'),
    path('createrecipe/', views.CreateNewRecipe.as_view(),
         name='new_recipe'),
    path('editrecipe/<slug:slug>', views.EditRecipe.as_view(),
         name='edit_recipe'),
    path('deleterecipe/<slug:slug>',
         views.DeleteRecipe.as_view(), name='delete_recipe'),
    path('<slug:slug>/', views.FullRecipe.as_view(), name='full_recipe'),
    path('like/<slug:slug>', views.recipe_like, name='recipe_like'),
    path('category/<category>/', views.RecipeCatListView.as_view(),
         name='category'),
    path('method/<method>/', views.RecipeMethodListView.as_view(),
         name='method'),
]
