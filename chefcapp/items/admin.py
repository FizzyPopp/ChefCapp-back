from django.contrib import admin

from .models import Ingredient
from .models import Unit
from .models import UnitIngredient
from .models import Recipe
from .models import Step
from .models import SubType
from .models import SubSize
from .models import SubState


class HorizontalRecipe(admin.ModelAdmin):
    filter_horizontal = ('ingredients','steps',)


class HorizontalStep(admin.ModelAdmin):
    filter_horizontal = ('ingredients_for_step',)


admin.site.register(Recipe, HorizontalRecipe)
admin.site.register(Step, HorizontalStep)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(UnitIngredient)
admin.site.register(SubType)
admin.site.register(SubSize)
admin.site.register(SubState)

# Register your models here.
