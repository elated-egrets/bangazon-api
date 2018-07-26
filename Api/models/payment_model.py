from django.db import models
from .user_model import User


class Payment(models.Model):
    name = models.CharField(max_length=50)
    payment_type = models.Field.choices = (
        ('CD', 'Card'),
        ('BK', 'Bank Account')
    )
    account_number = models.IntegerField()
    expiration = models.DateField()
    security_code = models.IntegerField()
    bank = models.CharField(max_length=20)
    user_id = models.ForeignKey(User, related_name='payment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.bank}'