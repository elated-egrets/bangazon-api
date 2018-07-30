from rest_framework import viewsets
from Api import models
from Api import serializers


class Order_Product_Viewset(viewsets.ModelViewSet):
    """
    Creates the Order_Viewset querys the models from order objects and the seralized data.
    """
    queryset = models.Order_Product.objects.all()
    serializer_class = serializers.Order_Product_Serializer