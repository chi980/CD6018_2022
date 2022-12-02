from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from user.utils import rename_image

# Create your models here.

# first_name:이름, email:이메일,username:아이디 ->template request.user.first_name형식으로 받아오면 됩니다!
class User(AbstractUser):
    GENDER_MALE = "m"
    GENDER_FEMALE = "f"

    GENDER_CHOICES = (
        (GENDER_MALE,"남자"),
        (GENDER_FEMALE,"여자")
    )

    ON_OFF_CHOICE=(
        (0,'음식점'),
        (1,'전체')
    )

    email = models.EmailField(unique=False)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default=GENDER_MALE)
    birthday = models.DateField(null=True)
    category = models.ForeignKey('main.Category',on_delete=models.SET_NULL,null=True,blank=True,related_name='user')
    # on_off = models.BooleanField(default=False) # False면
    on_off = models.IntegerField(default=0,choices=ON_OFF_CHOICE)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def __str__(self):
        # return "{}님({})".format(self.last_name or '익명',self.username)
        return f"아이디: {self.username} | 이름: {self.last_name} {self.first_name}| 성별: {self.gender} | 생일: {self.birthday} | 카테고리: {self.category} | on_off: {self.on_off}"
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
    # profile = models.ImageField(upload_to='media/',editable=True,null=True) s3사용시
    # profile = models.ImageField(upload_to='images/',editable=True,null=True)
    profile = models.ImageField(upload_to=rename_image,editable=True,null=True, max_length=255)

    name = models.CharField(max_length=20)
    kind = models.IntegerField(choices=KIND_CHOICES)
    breed = models.CharField(max_length=20)
    adoption_day = models.DateField()
    birthday = models.DateField(null=True)

    def __str__(self):
        return "{}님의 {}".format(self.user.last_name or "익명",self.name)

class Favorite(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='favorite')
    location = models.OneToOneField('main.Location',on_delete=models.CASCADE, related_name='favorite')

    def __str__(self):
        return f'{self.user.id}님의 {self.location.name}'