from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    """
    Overriding the default Django user model to be able to update it in the
    future if needed
    """

    pass
