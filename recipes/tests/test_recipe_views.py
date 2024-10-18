from http import HTTPStatus

from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


class RecipeViewTest(TestCase):
    def test_recipe_home_function_view_ok(self):
        view = resolve(reverse('recipes:home'))

        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_ok(self):
        response = self.client.get(reverse('recipes:home'))

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_recipe_home_view_renders_correct_template(self):
        response = self.client.get(reverse('recipes:home'))

        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_no_show_recipes(self):
        response = self.client.get(reverse('recipes:home'))

        self.assertIn('No recipes found', response.content.decode('utf-8'))

    def test_recipe_category_function_view_ok(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1000}))

        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_status_not_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000}))

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_recipe_detail_function_view_ok(self):
        view = resolve(reverse('recipes:detail', kwargs={'id': 1}))

        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_status_not_found(self):
        response = self.client.get(reverse('recipes:detail', kwargs={'id': 1000}))

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
