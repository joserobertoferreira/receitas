from django.forms import ValidationError
from parameterized import parameterized

from recipes.tests.test_recipe_base import RecipeBaseTest


class RecipeModelTest(RecipeBaseTest):
    def setUp(self) -> None:
        self.recipe = self.create_recipe()
        return super().setUp()

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
