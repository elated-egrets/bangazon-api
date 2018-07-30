from rest_framework import serializers
from Api import models


class Product_Serializer(serializers.ModelSerializer):
    """
    Serializer for products

    fields exposed:
        'id',
        'seller_id',
        'category_id',
        'name',
        'description',
        'price',
        'date_created'
    """
    class Meta:
        fields = (
            'id',
            'seller_id',
            'category_id',
            'name',
            'description',
            'price',
            'date_created',
        )
        model = models.Product
