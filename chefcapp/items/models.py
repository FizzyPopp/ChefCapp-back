from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'ingredients'

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=256, default='Full Name')
    abbreviation = models.CharField(max_length=256, default='xx')

    class Meta:
        db_table = 'units'

    def __str__(self):
        return self.name


class UnitIngredient(models.Model):
    quantity = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{} - {} {}'.format(self.ingredient, self.quantity, self.unit)


class Equipment(models.Model):
    name = models.CharField(max_length=256)
    # Later on add image, etc.

    class Meta:
        db_table = 'equipment'


class Step(models.Model):
    title = models.CharField(max_length=256, default='xxxxx-xx-step')
    ingredients_for_step = models.ManyToManyField(UnitIngredient)
    description = models.TextField()

    class Meta:
        db_table = 'steps'

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=256, default='Recipe Title')
    
    steps = models.ManyToManyField(Step)

    class Meta:
        db_table = 'recipes'

    def __str__(self):
        return self.title
