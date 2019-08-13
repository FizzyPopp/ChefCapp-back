from django.contrib import admin
from .models import Ingredient
from .models import Recipe

class YourAdmin(admin.ModelAdmin):
    filter_horizontal = (Ingredient,)


admin.site.register(YourAdmin)
admin.site.register(Ingredient)
admin.site.register(Recipe)

# Register your models here.
