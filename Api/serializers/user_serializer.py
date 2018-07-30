from rest_framework import serializers
from Api import models

class User_Serializer(serializers.ModelSerializer):
    """
    Serializer for user

    fields exposed:
        'id',
        'first_name',
        'last_name',
        'date_created',
        'activate',
        'password',
        'email'
    """
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