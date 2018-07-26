from rest_framework import serializers
from Api import models

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'date_created',
            'active',
            'password',
            'email'
        )
        model = models.User