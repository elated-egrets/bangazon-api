from rest_framework import viewsets
from Api import models
from Api import serializers


class User_Viewset(viewsets.ModelViewSet):
    """Creates the Userr_Viewset querys the models from user objects and the seralized data."""

    serializer_class = serializers.User_Serializer

    def get_queryset(self):
        """ method to control the query of the users table
            The view should filter by active users if the url contains the filter
        """
        queryset = models.User.objects.all()
        query_string = self.request.query_params.get('active', None)

        # take the string value from the url and set a boolean value accordingly
        if query_string is not None:
            if query_string == 'false':
                active_query = False
            elif query_string == 'true':
                active_query = True
            # set the queryset if the filter was present
            queryset = queryset.filter(active=active_query)

        return queryset

