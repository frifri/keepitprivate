from django.contrib.auth import get_user_model

from rest_framework import viewsets

from .serializers import AccountSerializer

user_model = get_user_model()


class AccountViewSet(viewsets.ModelViewSet):
    """ Model viewset related to the Account model """

    queryset = user_model.objects.all()
    serializer_class = AccountSerializer
