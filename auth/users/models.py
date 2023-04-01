from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None #Overide the default username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []