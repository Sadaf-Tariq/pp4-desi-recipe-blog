from django.test import TestCase
from .forms import RecipeForm, CommentForm, RatingForm


class TestRecipeForm(TestCase):
    """
    Test for create new recipe form
    """

    def test_recipe_title_is_required(self):
        form = RecipeForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = RecipeForm()
        self.assertEqual(
            form.Meta.fields, (
                'title', 'category', 'method', 'author_name',
                'featured_image', 'ingredients', 'instructions',
                'prep_time', 'cooking_time', 'servings', 'calories')
        )


class TestCommentForm(TestCase):
    """
    Test for Comment Form
    """

    def test_recipe_content_is_required(self):
        form = CommentForm(({'comment': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(form.errors['comment'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(
            form.Meta.fields, ('name', 'comment')
        )


class TestRatingtForm(TestCase):
    """
    Test for Rating Form
    """

    def test_recipe_rating_is_required(self):
        form = RatingForm(({'rating': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = RatingForm()
        self.assertEqual(
            form.Meta.fields, ('rating',)
        )
