from rest_framework import viewsets
from Api import models
from Api import serializers


class User_Viewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.User_Serializer