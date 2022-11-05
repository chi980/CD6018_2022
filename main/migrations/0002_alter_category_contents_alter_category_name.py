# Generated by Django 4.1.3 on 2022-11-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='contents',
            field=models.CharField(choices=[('CSM', '맛+가격+서비스+분위기'), ('WS', '맛+웨이팅+서비스'), ('SC', '맛+서비스+가격'), ('W', '맛+웨이팅'), ('MS', '맛+분위기+서비스'), ('CSW', '맛+가격+서비스+웨이팅')], max_length=3),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('CSM', '저렴한 가격 & 좋은 분위기를 원하는 가성비 충'), ('WS', '오랜 대기와 불친절은 사절합니다.'), ('SC', '서비스가 중요한 당신!가격까지 착하길 원하신다구요?!'), ('W', '웨이팅 시간이 아까운 바쁜 당신'), ('MS', '오늘은 분위기에 취하고 싶은 날!'), ('CSW', '모든 것이 빠지지 않는 무난한 맛집을 찾으신다구요?!')], max_length=3),
        ),
    ]