from django.forms import ValidationError
from parameterized import parameterized

from recipes.models import Recipe
from recipes.tests.test_recipe_base import RecipeBaseTest


class RecipeModelTest(RecipeBaseTest):
    def setUp(self) -> None:
        self.recipe = self.create_recipe()
        return super().setUp()

    def create_recipe_without_defaults(self):
        recipe = Recipe(
            title="Recipe Title",
            description="Recipe Description",
            slug="recipe-slug",
            preparation_time=10,
            preparation_time_unit="minutes",
            servings=5,
            servings_unit="portions",
            preparation_steps="Steps Preparation",
            category=self.create_category(name="Test Default Category"),
            author=self.create_author(username="newuser"),
        )
        recipe.full_clean()
        recipe.save()

        return recipe

    @parameterized.expand(
        [
            ("title", 65),
            ("description", 165),
            ("preparation_time_unit", 20),
            ("servings_unit", 20),
        ]
    )
    def test_recipe_max_length_fields(self, field, max_length):
        setattr(self.recipe, field, "A" * (max_length + 1))

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_default_value_for_preparation_steps_is_html(self):
        recipe = self.create_recipe_without_defaults()

        self.assertFalse(recipe.preparation_steps_is_html)

    def test_recipe_default_value_for_is_published(self):
        recipe = self.create_recipe_without_defaults()

        self.assertFalse(recipe.is_published, msg="Recipe is not published by default")

    def test_recipe_string_representation(self):
        self.recipe.title = "Test Representation"
        self.recipe.full_clean()
        self.recipe.save()

        self.assertEqual(str(self.recipe), "Test Representation")
