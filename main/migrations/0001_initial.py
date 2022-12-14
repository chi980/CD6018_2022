# Generated by Django 4.1.3 on 2022-12-09 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('CSM', '저렴한 가격 & 좋은 분위기를 원하는 가성비 충'), ('WS', '오랜 대기와 불친절은 사절합니다.'), ('SC', '서비스가 중요한 당신!가격까지 착하길 원하신다구요?!'), ('W', '웨이팅 시간이 아까운 바쁜 당신'), ('MS', '오늘은 분위기에 취하고 싶은 날!'), ('CSW', '모든 것이 빠지지 않는 무난한 맛집을 찾으신다구요?!')], max_length=3)),
                ('contents', models.CharField(choices=[('CSM', '맛+가격+서비스+분위기'), ('WS', '맛+웨이팅+서비스'), ('SC', '맛+서비스+가격'), ('W', '맛+웨이팅'), ('MS', '맛+분위기+서비스'), ('CSW', '맛+가격+서비스+웨이팅')], max_length=3)),
                ('profile', models.ImageField(blank=True, max_length=255, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.IntegerField(blank=True, choices=[(0, '카페'), (1, '음식점'), (2, '애견')], default=1, null=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('lot_address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('time', models.CharField(blank=True, max_length=128, null=True)),
                ('url', models.URLField()),
                ('is_animal_in', models.IntegerField(choices=[(0, '불가'), (1, '가능'), (2, '정보 없음')], default=2, null=True)),
                ('latitude', models.DecimalField(decimal_places=10, default=0.0, max_digits=12, null=True)),
                ('longitude', models.DecimalField(decimal_places=10, default=0.0, max_digits=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField(blank=True, null=True)),
                ('star', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='main.category')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review', to='main.location')),
            ],
        ),
    ]
