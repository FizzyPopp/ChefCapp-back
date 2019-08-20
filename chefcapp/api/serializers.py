from rest_framework import serializers

from items.models import Ingredient, Unit, SubType, SubSize, SubState, UnitIngredient, Step, Recipe


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name',]


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['name',]


class SubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubType
        fields = ['type',]


class SubSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSize
        fields = ['size',]


class SubStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubState
        fields = ['state',]


class UnitIngredientSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()
    state = SubStateSerializer()
    size = SubSizeSerializer()
    type = SubTypeSerializer()
    ingredient = IngredientSerializer()
    class Meta:
        model = UnitIngredient
        fields = [
            'unit',
            'state',
            'size',
            'type',
            'ingredient',
        ]

class StepSerializer(serializers.ModelSerializer):
    ingredients_for_step = UnitIngredientSerializer(many=True)
    class Meta:
        model = Step
        fields = [
            'title',
            'ingredients_for_step',
            'description',
        ]

class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredients = UnitIngredientSerializer(many=True)
    steps = StepSerializer(many=True)
    class Meta:
        model = Recipe
        fields = [
            'title',
            'ingredients',
            'steps',
        ]
