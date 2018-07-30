from django.db import models
from django.utils import timezone
from .user_model import User
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

    def __str__(self):
        """ returns a string representation of the object """
        return f'{self.buyer_id} {self.payment} '
