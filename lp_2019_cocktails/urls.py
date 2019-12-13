"""lp_2019_cocktails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from app.views import IndexView, CocktailSearchByIngredientView, CocktailListView, CocktailDetailView, CocktailSearchDetailView, sCocktailCreateView, CocktailUpdateView, CocktailDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='app_index'),
    path('cocktails/detail/<int:pk>', CocktailDetailView.as_view(), name='app_cocktail_detail'),
    path('cocktails/detail/search/<str:slug>', CocktailSearchDetailView.as_view(), name='app_cocktail_search_detail'),
    path('cocktails/create', CocktailCreateView.as_view(), name='app_cocktail_create'),
    path('cocktails/update/<int:pk>', CocktailUpdateView.as_view(), name='app_cocktail_update'),
    path('cocktails/delete/<int:pk>', CocktailDeleteView.as_view(), name='app_cocktail_delete'),
    path('cocktails/', CocktailListView.as_view(), name='app_cocktail_list'),
    path('cocktails/search-by-ingredient/<str:slug>', CocktailSearchByIngredientView.as_view(),
         name='app_cocktail_search_by_ingredient'),
]
