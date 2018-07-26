from rest_framework import serializers
from Api import models


class Product_Serializer(serializers.ModelSerializer):
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
        model = models.Payment
