from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, ListView

from app.models import Cocktail, Ingredient, CocktailIngredientUnit
from forms.cocktail import CocktailForm


class IndexView(ListView):
    template_name = 'index.html'
    model = Cocktail

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Tous les cocktails !'
        return result


class CocktailDetailView(DetailView):
    template_name = 'cocktail_detail.html'
    model = Cocktail


class CocktailSearchDetailView(ListView):
    template_name = 'index.html'
    model = Cocktail

    def get_queryset(self):
        title = self.kwargs.get('slug', '')
        return Cocktail.objects.filter(title__contains=title)

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     result = super().get_context_data(**kwargs)
    #     title = self.kwargs.get('slug', '')
    #     result['object.list'] = Cocktail.objects.filter(title__contains=title)
    #     return result


class CocktailCreateView(LoginRequiredMixin, CreateView):
    template_name = 'cocktail_create.html'
    model = Cocktail
    form_class = CocktailForm

    def get_success_url(self):
        return reverse('app_index')


class CocktailUpdateView(UpdateView):
    template_name = 'cocktail_update.html'
    model = Cocktail
    form_class = CocktailForm

    def get_success_url(self):
        return reverse('app_index')


class CocktailDeleteView(DeleteView):
    template_name = 'cocktail_delete.html'
    model = Cocktail
    form_class = CocktailForm

    def get_success_url(self):
        return reverse('app_index')


class CocktailListView(ListView):
    template_name = 'cocktail_list.html'
    model = Cocktail


class CocktailSearchByIngredientView(generic.ListView):
    template_name = 'cocktail_list.html'

    def get_queryset(self):
        search = self.kwargs['slug']
        return Cocktail.objects.filter(ingredients__ingredient__description__icontains=search)
