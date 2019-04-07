from django.db import models
from django.contrib.auth.models import  AbstractUser


class User(AbstractUser):
    email_id = models.EmailField(max_length=100, unique=True)
    phone = models.PositiveIntegerField()
    is_seller = models.BooleanField(default=False)
    description = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='images/', default='images/profile_default.png')
