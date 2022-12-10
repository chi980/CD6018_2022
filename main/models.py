from django.db import models
from user.utils import rename_category_image
# Create your models here.

class Category(models.Model):
    NAME = (
        ('CSM','저렴한 가격 & 좋은 분위기를 원하는 가성비 충'),
        ('WS','오랜 대기와 불친절은 사절합니다.'),
        ('SC','서비스가 중요한 당신!가격까지 착하길 원하신다구요?!'),
        ('W','웨이팅 시간이 아까운 바쁜 당신'),
        ('MS','오늘은 분위기에 취하고 싶은 날!'),
        ('CSW','모든 것이 빠지지 않는 무난한 맛집을 찾으신다구요?!')
    )
    CONTENTS = (
        ('CSM','맛+가격+서비스+분위기'),
        ('WS','맛+웨이팅+서비스'),
        ('SC','맛+서비스+가격'),
        ('W','맛+웨이팅'),
        ('MS','맛+분위기+서비스'),
        ('CSW','맛+가격+서비스+웨이팅')
    )
    name = models.CharField(max_length=3,choices=NAME)
    contents = models.CharField(max_length=3,choices=CONTENTS)
    profile = models.ImageField(upload_to='media/',editable=True,null=True, blank=True,max_length=255)

    def __str__(self):
        return f'{self.get_name_display()}'

# location
class Location(models.Model):
    ANIMAL_IN_CHOICE=(
        (0,'불가'),
        (1,'가능'),
        (2,'정보 없음')
    )
    # ON_OFF_CHOICE=(
    #     (0,'음식점'),
    #     (1,'애견')
    # )
    CATEGORY_CHOICE=(
        (0,'카페'),
        (1,'음식점'),
        (2,'애견')
    )
    name = models.CharField(max_length=50)
    # category = models.CharField(max_length=30, blank=True)
    category = models.IntegerField(blank=True, default=1, choices=CATEGORY_CHOICE, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    lot_address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    time = models.CharField(max_length=128,blank=True, null=True)
    url = models.URLField()
    is_animal_in = models.IntegerField(default=2, choices=ANIMAL_IN_CHOICE, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=10, default=0.0, null=True)     #위도
    longitude = models.DecimalField(max_digits=13, decimal_places=10, default=0.0, null=True)    #경도
    # on_off = models.IntegerField(default=0,choices=ON_OFF_CHOICE)

    def __str__(self):
        return f'{self.name}(<a href="{self.url}"></a>)'

class Review(models.Model):
    category = models.ForeignKey('main.Category',on_delete=models.CASCADE, related_name='review',null=True,blank=True)
    location = models.ForeignKey('main.Location',on_delete=models.SET_NULL,related_name='review',null=True,blank=True)
    contents = models.TextField(blank=True,null=True)
    star = models.DecimalField(max_digits=2,decimal_places=1,default=0.0)

    def __str__(self):
        return f'{self.star} | {self.contents} [{self.category.get_name_display()}]'