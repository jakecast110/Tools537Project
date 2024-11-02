from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass
    role = models.CharField(max_length=7)

    def __str__(self):
        return self.username