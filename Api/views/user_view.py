from rest_framework import viewsets
from Api import models
from Api import serializers


class User_Viewset(viewsets.ModelViewSet):
    """Creates the Userr_Viewset querys the models from user objects and the seralized data."""

    queryset = models.User.objects.all()
    serializer_class = serializers.User_Serializer