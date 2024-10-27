from django.test import TestCase

from recipes.models import Category, Recipe, User


class RecipeBaseTest(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def create_category(self, name="Test Category") -> Category:
        return Category.objects.create(name=name)

    def create_author(
        self,
        first_name="test",
        last_name="user",
        username="testuser",
        email="testuser@example.com",
        password="testuser",
    ) -> User:
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )

    def create_recipe(
        self,
        title="Title Recipe",
        description="Description Recipe",
        slug="slug-recipe",
        preparation_time=10,
        preparation_time_unit="minutes",
        servings=5,
        servings_unit="portions",
        preparation_steps="Preparation Steps",
        preparation_steps_is_html=False,
        is_published=True,
        category_data=None,
        author_data=None,
    ) -> Recipe:
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            category=self.create_category(**category_data),
            author=self.create_author(**author_data),
        )
