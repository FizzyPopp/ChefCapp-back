from django.contrib import admin
from .models import Ingredient
from .models import Recipe

class YourAdmin(admin.ModelAdmin):
    filter_horizontal = ('ingredient',)


admin.site.register(Recipe, YourAdmin)
admin.site.register(Ingredient)

# Register your models here.
