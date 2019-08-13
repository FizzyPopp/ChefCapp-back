from django.contrib import admin

from .models import Ingredient

admin.site.register(Ingredient)

from .models import Recipe

admin.site.register(Recipe)

# Register your models here.
