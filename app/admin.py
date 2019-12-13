from django.contrib import admin
from django.utils.html import format_html

from app.models import Cocktail, Unit, CocktailIngredientUnit, Ingredient, Tag, CocktailTag


class CocktailTagInlineAdmin(admin.StackedInline):
    model = CocktailTag
    # par défaut : 3
    extra = 0


class CocktailAdmin(admin.ModelAdmin):

    def custom_description(self, obj):
        return format_html('<b>DESCRIPTION: </b> {}'.format(obj.description[:80]))

    custom_description.short_description = 'Summary'

    # champs qui apparaissent dans le tableau
    list_display = ('title', 'custom_description')
    # toute la list_display est cliquable :
    list_display_links = list_display
    # champs que l'on peut éditer
    fields = ('title', 'description')
    inlines = (CocktailTagInlineAdmin,)


admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Unit)
admin.site.register(CocktailIngredientUnit)
admin.site.register(Ingredient)
admin.site.register(Tag)
