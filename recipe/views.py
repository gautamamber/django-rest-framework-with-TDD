from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Tag, Ingredient
from . import serializers
from rest_framework import viewsets, mixins


class BaseRecipeViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    """
    Manage base objects in the database
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Return objects for the current authenticated user only
        :return:
        """
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """
        Create a new base object
        :param serializer:
        :return:
        """
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeViewSet):
    """
    Manage tags in the database
    """
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeViewSet):
    """
    Manage ingredient  in database
    """
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredeientSerializer

