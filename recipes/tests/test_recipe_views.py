from http import HTTPStatus

from django.urls import resolve, reverse

from recipes import views
from recipes.tests.test_recipe_base import RecipeBaseTest


class RecipeViewTest(RecipeBaseTest):
    def test_recipe_home_function_view_ok(self):
        view = resolve(reverse("recipes:home"))

        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_ok(self):
        response = self.client.get(reverse("recipes:home"))

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_recipe_home_view_renders_correct_template(self):
        response = self.client.get(reverse("recipes:home"))

        self.assertTemplateUsed(response, "recipes/pages/home.html")

    def test_recipe_home_no_show_recipes(self):
        response = self.client.get(reverse("recipes:home"))

        self.assertIn("No recipes found", response.content.decode("utf-8"))

    def test_recipe_home_shows_recipes(self):
        self.create_recipe(author_data={"first_name": "jrf"})
        response = self.client.get(reverse("recipes:home"))
        content = response.content.decode("utf-8")
        number_of_recipes = response.context["recipes"]

        # verify if the recipe title is in the response content
        self.assertIn("Title Recipe", content)

        # verify if the preparation time is in the response content
        self.assertIn("10 minutes", content)

        # verify if the author name is in the response content
        self.assertIn("jrf", content)

        # verify if the number of recipes is 1
        self.assertEqual(number_of_recipes.count(), 1)

    def test_recipe_home_no_show_recipes_not_published(self):
        self.create_recipe(is_published=False)
        response = self.client.get(reverse("recipes:home"))
        content = response.content.decode("utf-8")

        self.assertIn("No recipes found", content)

    def test_recipe_category_function_view_ok(self):
        view = resolve(reverse("recipes:category", kwargs={"category_id": 1000}))

        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_status_not_found(self):
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": 1000})
        )

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_recipe_category_template_renders_recipes(self):
        title = "Category test"

        self.create_recipe(title=title)

        response = self.client.get(reverse("recipes:category", args=(1,)))
        content = response.content.decode("utf-8")

        self.assertIn(title, content)

    def test_recipe_category_no_show_recipes_not_published(self):
        recipe = self.create_recipe(is_published=False)
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": recipe.category.id})
        )

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_recipe_detail_function_view_ok(self):
        view = resolve(reverse("recipes:detail", kwargs={"id": 1}))

        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_status_not_found(self):
        response = self.client.get(reverse("recipes:detail", kwargs={"id": 1000}))

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_recipe_detail_template_renders_recipe(self):
        title = "Recipe test"

        self.create_recipe(title=title)

        response = self.client.get(reverse("recipes:detail", kwargs={"id": 1}))
        content = response.content.decode("utf-8")

        self.assertIn(title, content)

    def test_recipe_detail_no_show_recipes_not_published(self):
        recipe = self.create_recipe(is_published=False)
        response = self.client.get(reverse("recipes:detail", kwargs={"id": recipe.id}))

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
