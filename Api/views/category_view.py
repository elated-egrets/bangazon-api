from rest_framework import viewsets
from Api import models
from Api import serializers


class Category_Viewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.Category_Serializer