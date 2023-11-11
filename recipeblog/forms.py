from .models import Comment, Recipe, Rating
from django import forms
from django_summernote.widgets import SummernoteWidget

class CommentForm(forms.ModelForm):
    comment_hidden_field = forms.BooleanField(widget=forms.HiddenInput, initial=True)

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

class RatingForm(forms.ModelForm):
    rating_hidden_field = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta: 
        model = Rating
        fields = ('rating',)
        CHOICE = (
            ('0',0),
            ('1', 1),
            ('2', 2),
            ('3', 3),
            ('4', 4),
            ('5', 5),
            )
        widgets = {
            'rating': forms.Select(choices=CHOICE)
        }