from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'category','method', 'author_name', 'featured_image', 'ingredients', 'instructions', 
        'prep_time', 'cooking_time', 'servings', 'calories')
