from django.db import models
from django.utils import timezone
from .user_model import User
from .product_model import Product
# from .order_product_model import Order_Product
# from .order_model import Order
#from .payment_model import Payment



class Order(models.Model):
    """[Class]
    Author: Ronnie Young

    Creates a model of order.
    Sets the buyer id equal to the foreign key to user and if deleted deletes on a cascading effect.
    Sets date_created equal to timezone.
    """
    buyer_id = models.ForeignKey(User, related_name="order", on_delete=models.CASCADE)
    payment = models.ForeignKey("Payment", related_name="order", on_delete=models.CASCADE)
    date_created = timezone.now()
    # product = models.ForeignKey(Order_Product, related_name="order_product_intersection", on_delete=models.CASCADE)

    def __str__(self):
        """ returns a string representation of the object """
        return f'{self.buyer_id} {self.payment}'
