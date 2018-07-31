from django.db import models
from .order_model import Order
from .product_model import Product

class Order_Product(models.Model):
    """Model for order product intersection table
        This model is used to ensure that the nested products are available to the order resource

    fields:
        order_id: the id of the order
        product_id: the id of the product on the order
    """

    order_id = models.ForeignKey(Order, related_name="order_intersection", on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name="product_intersection", on_delete=models.CASCADE)
