from django.db import models
from .user_model import User
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from safedelete.managers import SafeDeleteManager
from safedelete import DELETED_VISIBLE_BY_PK

class MyModelManager(SafeDeleteManager):
    _safedelete_visibility = DELETED_VISIBLE_BY_PK

class Payment(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    objects = MyModelManager()
    """model for payment information

    data:
        name -- str, user defined string representing the payment type
        payment_type -- str, either card or bank account
        account_number -- int, bank account or card number
        expiration -- date, expiration of the payment type
        security_code -- int, security code for card
        bank -- str, issuing bank or bank account holder
        user_id -- FK, reference to user who registered payment type
    """
    name = models.CharField(max_length=50)
    CARD = 'CD'
    ACCOUNT = 'AC'
    payment_choices = (
        (CARD, 'Card'),
        (ACCOUNT, 'Bank Account'),
    )
    payment_type = models.CharField(max_length=2, choices=payment_choices, default=CARD)
    account_number = models.IntegerField()
    expiration = models.DateField()
    security_code = models.IntegerField()
    bank = models.CharField(max_length=20)
    user_id = models.ForeignKey(User, related_name='payment', on_delete=models.CASCADE)

    def __str__(self):
        """a string representation of the object

        Returns:
            string -- name of payment type as well as issuing bank
        """
        return f'{self.name}: {self.bank}'
