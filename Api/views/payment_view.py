from rest_framework import viewsets
from Api import models
from Api import serializers


class Payment_Viewset(viewsets.ModelViewSet):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.Payment_Serializer