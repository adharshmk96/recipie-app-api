from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient

from recipe import serializers


class BaseRecipieAttrViewset(viewsets.GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin):

    # Base Viewset for user Owned Recipe attribute
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Return objects for the current authenticated user only
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        # Create New Tag
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipieAttrViewset):
    # Manage Tags in the Database
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipieAttrViewset):
    # manage ingredients in DB]
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
