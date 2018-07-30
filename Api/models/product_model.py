from django.db import models
from .user_model import User
from django.utils import timezone
from .category_model import Category


class Product(models.Model):
  """
  Product Model

  Returns:

  name - name of product
  description - description of product
  price - price of product
  date created - when the product was added
  seller id - foreign key of the user that is offering the product for sale on bangazon
  category id - foreign key of the category id that the product belongs to
  """

  name = models.CharField(max_length=50)
  description = models.CharField(max_length=400)
  price = models.CharField(max_length=10)
  date_created = timezone.now()
  seller_id = models.ForeignKey(User, related_name='product', on_delete=models.CASCADE)
  category_id = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)

  def __str__(self):
    """ returns a string representation of the object """
    return f'{self.name}: {self.description}'
