from django.db import models
from .order_model import Order
from .product_model import Product

class Order_Product(models.Model):

    order_id = models.ForeignKey(Order, related_name="order_intersection", on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name="product_intersection", on_delete=models.CASCADE)
