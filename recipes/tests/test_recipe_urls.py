from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_recipe_home_url(self):
        url = reverse('recipes:home')

        self.assertEqual(url, '/')

    def test_recipe_category_url(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})

        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url(self):
        url = reverse('recipes:detail', kwargs={'id': 1})

        self.assertEqual(url, '/recipes/1/')
