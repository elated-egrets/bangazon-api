from rest_framework import serializers
from Api import models


class Payment_Serializer(serializers.ModelSerializer):
    """
    Serializer for payments

    fields exposed:
        'id',
        'name',
        'payment_type',
        'account_number',
        'expiration',
        'security_code',
        'bank',
        'user_id'
    """
    class Meta:
        fields = (
            'id',
            'name',
            'payment_type',
            'account_number',
            'expiration',
            'security_code',
            'bank',
            'user_id',
        )
        model = models.Payment
