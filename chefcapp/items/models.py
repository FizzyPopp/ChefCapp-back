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


class SubType(models.Model):
    type = models.CharField(max_length=256, default='Ingredient Sub Type')

    class Meta:
        db_table = 'subtype'

    def __str__(self):
        return self.type


class SubSize(models.Model):
    size = models.CharField(max_length=256, default='Ingredient Sub Size')

    class Meta:
        db_table = 'subsize'

    def __str__(self):
        return self.size


class SubState(models.Model):
    state = models.CharField(max_length=256, default='Ingredient Sub State')

    class Meta:
        db_table = 'substate'

    def __str__(self):
        return self.state


class UnitIngredient(models.Model):
    quantity = models.PositiveIntegerField(default=0)

    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        default=0,
    )

    state = models.ForeignKey(
        SubState,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    size = models.ForeignKey(
        SubSize,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    type = models.ForeignKey(
        SubType,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{}{}{} {} - {} {}'.format(
            '{} '.format(self.state) if self.state else '',
            '{} '.format(self.size) if self.size else '',
            '{} '.format(self.type) if self.type else '',
            self.ingredient,
            self.quantity,
            self.unit
        )


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
    publish = models.BooleanField(default=False)
    ingredients = models.ManyToManyField(UnitIngredient)
    steps = models.ManyToManyField(Step)

    class Meta:
        db_table = 'recipes'

    def __str__(self):
        return self.title
