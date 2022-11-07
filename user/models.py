from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    GENDER_MALE = "m"
    GENDER_FEMALE = "f"

    GENDER_CHOICES = (
        (GENDER_MALE,"남자"),
        (GENDER_FEMALE,"여자")
    )

    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default=GENDER_MALE)
    birthday = models.DateField(null=True)
    category = models.ForeignKey('main.Category',on_delete=models.SET_NULL,null=True,blank=True,related_name='category')
    on_off = models.BooleanField(default=False) # False면 음식점만

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return "{}님({})".format(self.last_name or '익명',self.username)


