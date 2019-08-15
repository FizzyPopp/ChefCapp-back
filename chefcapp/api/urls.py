from django.conf.urls import url

from .views import RecipeListView

urlpatterns = [
    url(r'^recipes/?$', RecipeListView.as_view(), name='recipe_api'),
]
