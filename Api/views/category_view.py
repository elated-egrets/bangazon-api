from rest_framework import viewsets
from Api import models
from Api import serializers


class Category_Viewset(viewsets.ModelViewSet):
    """Creates the Category_Viewset querys the models from Category objects and the seralized data."""

    queryset = models.Category.objects.all()
    serializer_class = serializers.Category_Serializer