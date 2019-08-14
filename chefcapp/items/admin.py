from django.contrib import admin
from .models import Ingredient
from .models import Recipe
from .models import Step
from .models import UnitIngredient

class YourAdmin(admin.ModelAdmin):
    filter_horizontal = ('ingredients','steps','ingredients_for_step')


admin.site.register(Recipe, YourAdmin)
admin.site.register(Step)
admin.site.register(Ingredient)
admin.site.register(UnitIngredient)

# Register your models here.
