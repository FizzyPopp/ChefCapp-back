from django.contrib import admin
from .models import Ingredient
from .models import Recipe
from .models import Step
from .models import UnitIngredient

class HorizontalRecipe(admin.ModelAdmin):
    filter_horizontal = ('ingredients','steps')


class HorizontalStep(admin.ModelAdmin):
    filter_horizontal = ('ingredients_for_step')


admin.site.register(Recipe, HorizontalRecipe)
admin.site.register(Step, HorizontalStep)
admin.site.register(Ingredient)
admin.site.register(UnitIngredient)

# Register your models here.
