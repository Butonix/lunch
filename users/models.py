from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    """
    Extension of the User Model. We need to extend it
    to be able to add profile photo
    """

    photo = models.ImageField()

    def __str__(self):
        """
        Returning the user name as a string rep.
        """
        return self.username

