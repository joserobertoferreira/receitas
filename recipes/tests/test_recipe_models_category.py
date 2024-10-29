from django.forms import ValidationError

from recipes.tests.test_recipe_base import RecipeBaseTest


class CategoryModelTest(RecipeBaseTest):
    def setUp(self) -> None:
        self.category = self.create_category(name="Test Category")
        return super().setUp()

    def test_category_max_length_fields(self):
        self.category.name = "A" * 66

        with self.assertRaises(ValidationError):
            self.category.full_clean()

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), self.category.name)
