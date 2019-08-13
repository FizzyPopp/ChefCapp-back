from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    
    class Meta:
        db_table = 'ingredients'


class Equipment(models.Model):
    name = models.CharField(max_length=256)
    # Later on add image, etc.

    class Meta:
        db_table = 'equipment'


class Recipe(models.Model):
    title = models.CharField(max_length=256)
    ingredients = models.ManyToManyField(Ingredient)
    required_equipment = models.ManyToManyField(Equipment)
    description = models.TextField()

    class Meta:
        db_table = 'recipes'
