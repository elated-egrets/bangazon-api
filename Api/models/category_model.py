from django.db import models


class Category(models.Model):
      '''Model for the categories.

      Data:
        name --- name representation of the category
        description --- description of the category
      '''
      name = models.CharField(max_length=50)
      description = models.CharField(max_length=400)

      def __str__(self):
        '''A string representation of the Category.

        Returns:
          string --- category name and then description of said category.
        '''
        return f'{self.name}: {self.description}'