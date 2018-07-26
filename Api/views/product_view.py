from rest_framework import viewsets
from Api import models
from Api import serializers


class Product_Viewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.Product_Serializer