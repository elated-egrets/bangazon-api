from django.db import models
from django.utils import timezone
from safedelete.models import SafeDeleteModel
from safedelete.models import NO_DELETE

class User(SafeDeleteModel):
    '''Model for user information.

    Data:
        safedelete-policy --- module imported so the user cannot be deleted.
        first_name --- str, user's first name.
        last_name --- str, user's last name.
        date_created --- date, date when the user was created.
        active --- bool, showing if the user has placed an order.
        password --- str, for user authentication.
        email --- str, for user authentication and tracking.
    '''
    _safedelete_policy = NO_DELETE
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_created = timezone.now()
    active = False
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        '''A string representation of the user's first and last name.

        Returns:
            string -- the users first and last name.
        '''
        return f'{self.first_name}  {self.last_name}'
