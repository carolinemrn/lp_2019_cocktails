from django.forms import models

from app.models import Cocktail


class CocktailForm(models.ModelForm):
    class Meta:
        model = Cocktail
        fields = ['title', 'description', 'recipe']