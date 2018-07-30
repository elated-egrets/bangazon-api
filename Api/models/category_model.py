from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from safedelete.managers import SafeDeleteManager
from safedelete import DELETED_VISIBLE_BY_PK


class MyModelManager(SafeDeleteManager):
    _safedelete_visibility = DELETED_VISIBLE_BY_PK

class Category(SafeDeleteModel):
    '''Model for the categories.

    Data:
      name --- name representation of the category
      description --- description of the category
    '''
    _safedelete_policy = SOFT_DELETE
    objects = MyModelManager()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

    def __str__(self):
      '''A string representation of the Category.

      Returns:
        string --- category name and then description of said category.
      '''
      return f'{self.name}: {self.description}'