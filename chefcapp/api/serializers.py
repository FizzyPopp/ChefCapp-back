from rest_framework import serializers

from items.models import Recipe


class RecipeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
