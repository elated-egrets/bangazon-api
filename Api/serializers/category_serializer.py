from rest_framework import serializers
from Api import models


class Category_Serializer(serializers.ModelSerializer):
    """
    Serializer for categories.

    fields exposed:
      'id',
      'name',
      'description'
    """
    class Meta:
        fields = (
          'id',
          'name',
          'description'
        )
        model = models.Category
