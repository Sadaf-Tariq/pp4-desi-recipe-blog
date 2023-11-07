from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'category', 'method', 'author_name', 
                  'featured_image', 'ingredients', 'instructions',
                  'prep_time', 'cooking_time', 'servings', 'calories')
        widgets = {
            'instructions': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'prep_time': forms.NumberInput(
                attrs={'placeholder': 'Input in minutes'}),
            'cooking_time': forms.NumberInput(
                attrs={'placeholder': 'Input in minutes'})
        }
