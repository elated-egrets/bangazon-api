from rest_framework import viewsets
from Api import models
from Api import serializers


class Payment_Viewset(viewsets.ModelViewSet):
    '''Creates the Payment_Viewset querys the models from payment objects and the seralized data.'''

    queryset = models.Payment.objects.all()
    serializer_class = serializers.Payment_Serializer