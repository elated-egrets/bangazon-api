from rest_framework import serializers
from Api import models


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = (
          'id',
          'name',
          'description'
        )
        model = models.Category
