from rest_framework import serializers
from Api import models
from .product_serializer import Product_Serializer
from .order_product_serializer import Order_Product_Serializer



class Order_Serializer(serializers.ModelSerializer):
    """
    Author: Ronnie Young

    Creates a searlizer for order.
    and converts the buyer_id, payment, and date_created to JSON data.

    """
    products = Product_Serializer(many=True, read_only=True)
    class Meta:
        fields =  (
            'id',
            'buyer_id',
            'payment',
            'date_created',
            'products'
        )
        model = models.Order