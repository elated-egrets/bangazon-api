from rest_framework import viewsets
from Api import models
from Api import serializers

"""
    Creates the Order_Viewset querys the models from order objects and the seralized data.
"""
class Order_Viewset(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.Order_Serializer
