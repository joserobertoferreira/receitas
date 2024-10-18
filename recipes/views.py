from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        # 'recipes': [generate_recipe() for _ in range(10)]
        'recipes': recipes,
    })

def category(request, category_id):
    # recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')

    # if not recipes:
    #     raise Http404('Category not found.')

    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |',
    })

def recipe(request, id):
    #recipe = Recipe.objects.filter(pk=id, is_published=True).order_by('-id').first()

    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-detail.html', context={
        'recipe': recipe,
        'is_detail_page': True,
        'title': f'{recipe.title} |',
    })
