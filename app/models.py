from django.db import models


class Tag(models.Model):
    description = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.description


class Cocktail(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, default='(no title)')
    description = models.TextField(blank=True, null=True, default=None)
    recipe = models.TextField(blank=True, null=True, default=None)
    tags = models.ManyToManyField(Tag, related_name='cocktails',
                                  through='CocktailTag')

    def __str__(self):
        result = self.title
        if self.description is not None:
            result += ' ' + self.description[:80]
        return result


class CocktailTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)


class Unit(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True, default='(no title)')

    def __str__(self):
        return self.description if self.description is not None else '? ?'


class Ingredient(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True, default='(no title)')

    def __str__(self):
        return self.description if self.description is not None else '? ?'


class CocktailIngredientUnit(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE, related_name='ingredients')
    value = models.FloatField(default=1.0, blank=False)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f'{self.value} {self.unit} {self.ingredient}'
