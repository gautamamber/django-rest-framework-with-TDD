from rest_framework import serializers
from core.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for tag object
    """
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredeientSerializer(serializers.ModelSerializer):
    """
    Serializer for ingredient
    """
    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)