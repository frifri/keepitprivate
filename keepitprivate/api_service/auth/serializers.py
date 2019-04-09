from django.contrib.auth import get_user_model

from rest_framework import serializers

user_model = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    """ Serializer class for the Account model """

    class Meta:
        model = user_model
        fields = ('id', 'username', 'is_staff', 'email',)
