from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    """ User Model """

    username = models.CharField(max_length=140, unique=True)
    photo = models.ImageField()

    def __str__(self):
        return self.username

