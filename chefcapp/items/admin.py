from django.contrib import admin
from .models import Ingredient
from .models import Unit
from .models import UnitIngredient
from .models import Recipe
from .models import Step

class HorizontalRecipe(admin.ModelAdmin):
    filter_horizontal = ('steps',)


class HorizontalStep(admin.ModelAdmin):
    filter_horizontal = ('ingredients_for_step',)


admin.site.register(Recipe, HorizontalRecipe)
admin.site.register(Step, HorizontalStep)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(UnitIngredient)

# Register your models here.
