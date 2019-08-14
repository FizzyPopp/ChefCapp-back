from django.contrib import admin
from .models import Ingredient
from .models import Recipe
from .models import Step

class YourAdmin(admin.ModelAdmin):
    filter_horizontal = ('ingredients',)


admin.site.register(Recipe, YourAdmin)
admin.site.register(Step)
admin.site.register(Ingredient)

# Register your models here.
