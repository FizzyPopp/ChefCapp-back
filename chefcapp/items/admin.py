from django.contrib import admin
from .models import Ingredient
from .models import Recipe

class IngredentAdmin(admin.ModelAdmin):
    filter_horizontal = (Ingredient,)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe)

# Register your models here.
