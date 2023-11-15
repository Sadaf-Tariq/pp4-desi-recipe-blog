from django.test import TestCase
from .models import Recipe, RecipeMethod, RecipeCategory
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

User = get_user_model()


class TestViews(TestCase):
    """
    Test cases to test app views
    """

    def setUp(self):
        self.user = User.objects.create_user(
            email='testcustomuser@abc.pl', password='abcd')
        self.category = RecipeCategory.objects.create(food_type='bread')
        self.method = RecipeMethod.objects.create(recipe_method='frying')
        self.recipe = Recipe.objects.create(
            category=self.category, method=self.method, author_email=self.user,
            title='Test', ingredients='fish', instructions='cook',
            cooking_time='15', prep_time='30', servings='3', calories='300')

    def test_home_page(self):
        """Test for home page template"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_recipes_page(self):
        """Test for recipes page template"""
        response = self.client.get('/allrecipes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_recipes.html')

    def test_create_recipe_page(self):
        """Test for recipes page template"""
        response = self.client.get('/createrecipe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_new_recipe.html')

    def test_food_category_page(self):
        """Test for categories page template"""
        response = self.client.get('/category/<category>/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes_category.html')

    def test_food_method_page(self):
        """Test for categories page template"""
        response = self.client.get('/method/<method>/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes_method.html')

    def test_full_recipe_page(self):
        response = self.client.get(reverse('full_recipe',
                                           args=[self.recipe.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'full_recipe.html')

    def test_edit_recipe_page(self):
        response = self.client.get(reverse('edit_recipe',
                                           args=[self.recipe.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_recipe.html')

    def test_delete_recipe_page(self):
        response = self.client.get(reverse('delete_recipe',
                                           args=[self.recipe.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_recipe.html')
