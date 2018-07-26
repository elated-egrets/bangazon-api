from django.db import models
from .user_model import User
from django.utils import timezone


class Product(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=400)
  price = models.CharField(max_length=10)
  date_created = timezone.now()
  seller_id = models.ForeignKey(User, related_name='product', on_delete=models.SET_NULL)

  def __str__(self):
    return f'{self.name}: {self.description}'
