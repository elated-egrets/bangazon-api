from rest_framework import serializers
from Api import models



class Order_Product_Serializer(serializers.ModelSerializer):
    """
    Author: Ronnie Young

    Creates a searlizer for order.
    and converts the buyer_id, payment, and date_created to JSON data.

    """
    class Meta:
        fields = (
            'id',
            'order_id',
            'product_id'
        )
        model = models.Order_Product