from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
# Create your models here.

class User(AbstractUser):
    phone_Number = models.CharField(max_length=15)
    is_superuser=models.BooleanField(default=False)
    slug=AutoSlugField(populate_from=['first_name','last_name'],unique=True)
    def __str__(self):
        return self.username

