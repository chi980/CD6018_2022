from django.db import models

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

    def __str__(self):
        return f'{self.name} : {self.get_name_display()}'
