from django.shortcuts import render

from __localcode.main import generate_recipe


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [generate_recipe() for _ in range(10)]
    })

def recipe(request, pk):
    return render(request, 'recipes/pages/recipe-detail.html', context={
        'recipe': generate_recipe(),
        'is_detail_page': True,
    })
