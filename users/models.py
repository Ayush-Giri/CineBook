from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="profile_image", null=True, blank=True)
