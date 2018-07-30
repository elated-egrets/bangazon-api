from rest_framework import serializers
from Api import models
"""
    Author: Ronnie Young

    Creates a searlizer for order.
    and converts the buyer_id, payment, and date_created to JSON data.

"""


class Order_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'buyer_id',
            'payment',
            'date_created'
        )
        model = models.Order
