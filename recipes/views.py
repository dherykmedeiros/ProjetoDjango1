from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.utils import main
from recipes.models import Recipe
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(is_published= True)
    return render(request, 'recipes/pages/home.html',
                  context={
                      'recipes': recipes

                  })
    # HTTP Response

def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id,
        is_published=True
        )
    )
    #recipes = Recipe.objects.filter(
    #    category__id=category_id,
    #    is_published=True
    #    ).order_by('-id')
    #if not recipes:
    #    raise Http404('Not Found')
    return render(request, 'recipes/pages/category.html',
                  context={
                     'recipes': recipes,
                     'title': f'{recipes[0].category.name} -  Category | '

                  })
    # HTTP Response


def recipe(request, id):
    recipe = get_object_or_404(Recipe,
        pk=id,
        is_published = True
        ) 
    return render(request, 'recipes/pages/recipe-view.html',context={
                    'recipe': recipe,
                    'is_detail_page': True,
                  })
    # HTTP Response


def search(request):
    search_term = request.GET.get('search', '').strip()

    if not search_term:
        raise Http404('Errei, fui mlk')
    
    recipe = Recipe.objects.filter(
    Q(
        Q(title__icontains=search_term) |
        Q(description__icontains=search_term),
    ),
    is_published = True
    ).order_by('-id')
    return render(request,  'recipes/pages/search.html', context={
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': recipe


    })


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/pages/recipe-new.html'
    success_url = reverse_lazy('recipes-home')  
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



