from django.test import TestCase
from .models import Recipe, RecipeCategory, RecipeMethod, Comment, Rating
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='testcustomuser@abc.pl', password='abcd')
        self.category = RecipeCategory.objects.create(food_type='bread')
        self.method = RecipeMethod.objects.create(recipe_method='frying')
        self.recipe = Recipe.objects.create(
            category=self.category, method=self.method, author_email=self.user, title='Test',
            ingredients='fish', instructions='cook', cooking_time='15', prep_time='30',
            servings='3', calories='300')

    def test_comment_default_approve_false(self):
        comment = Comment.objects.create(
            recipe = self.recipe,
            name = 'sadaf',
            email = self.user,
            comment = 'okay'
        )
        self.assertFalse(comment.approved)


class RecipeModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='testcustomuser@abc.pl', password='abcd')
        self.category = RecipeCategory.objects.create(food_type='bread')
        self.method = RecipeMethod.objects.create(recipe_method='frying')

    def test_recipe_title_max_length(self):
        user_email = self.user
        recipe = Recipe.objects.create(
            category=self.category, method=self.method, author_email=user_email, title='Test',
            ingredients='fish', instructions='cook', cooking_time='15', prep_time='30',
            servings='3', calories='300')
        max_length = recipe._meta.get_field('title').max_length
        self.assertEqual(max_length, 150)


class RatingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='testcustomuser@abc.pl', password='abcd')
        self.category = RecipeCategory.objects.create(food_type='bread')
        self.method = RecipeMethod.objects.create(recipe_method='frying')
        self.recipe = Recipe.objects.create(
            category=self.category, method=self.method, author_email=self.user, title='Test',
            ingredients='fish', instructions='cook', cooking_time='15', prep_time='30',
            servings='3', calories='300')

    def test_recipe_title_max_length(self):
        rating = Rating.objects.create(
            user = self.user,
            recipe = self.recipe,
        )
        self.assertEqual(rating.rating, 0)

class CategoryModelTest(TestCase):

    def test_max_length(self):
        category = RecipeCategory.objects.create(food_type="bread")
        max_length = category._meta.get_field('food_type').max_length
        self.assertEqual(max_length, 50)


class MethodModelTest(TestCase):

    def test_max_length(self):
        method = RecipeMethod.objects.create(recipe_method="frying")
        max_length = method._meta.get_field('recipe_method').max_length
        self.assertEqual(max_length, 50)


