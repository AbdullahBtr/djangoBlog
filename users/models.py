from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age=models.PositiveIntegerField(default=0)
    created_time=models.DateTimeField(default=now)