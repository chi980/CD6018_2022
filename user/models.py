from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

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
    category = models.ForeignKey('main.Category',on_delete=models.SET_NULL,null=True,blank=True,related_name='user')
    on_off = models.BooleanField(default=False) # False면 음식점만

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return "{}님({})".format(self.last_name or '익명',self.username)

class Pet(models.Model):
    # 참고: https://m.segye.com/view/20201020515846
    KIND_CHOICES = (
        (0, "강아지"),
        (1, "고양이"),
        (2, "어류"),
        (3, "조류"),
        (4,"파충류"),
        (5,"소동물"),
        (6,"기타")
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='pet')
    profile = models.ImageField(upload_to='media/',editable=True,null=True)
    name = models.CharField(max_length=20)
    kind = models.IntegerField(choices=KIND_CHOICES)
    breed = models.CharField(max_length=20)
    adoption_day = models.DateField()
    birthday = models.DateField(null=True)


