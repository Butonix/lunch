from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    """
    Extension of the User Model. Because of the profile photo
    """

    photo = models.ImageField()

    def __str__(self):
        """
        Returning the user name as a string representation
        """
        return self.username

