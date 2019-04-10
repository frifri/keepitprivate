from django.contrib.auth import get_user_model
from django.db import models

from django_extensions.db.models import TimeStampedModel

user_model = get_user_model()


class File(TimeStampedModel):
    """
    The main logical object from this project. This will store all the data and
    metadata related to a saved file.
    """

    target_file = models.FileField(help_text="Represent the actual stored file")
    owner = models.ForeignKey(user_model,
                              on_delete=models.DO_NOTHING,
                              help_text="The owner of the stored file")
