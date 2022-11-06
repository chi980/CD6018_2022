from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    category = models.ForeignKey('main.Category',on_delete=models.SET_NULL,null=True,blank=True,related_name='category')
    on_off = models.BooleanField(default=False)