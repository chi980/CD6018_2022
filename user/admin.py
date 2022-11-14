from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Pet
# Register your models here.

# 모델 검색
# foreign key로 검색(foreignmodel__modelfield)
class PetAdmin(admin.ModelAdmin):
    search_fields = ['user__id']

admin.site.register(User,UserAdmin)
admin.site.register(Pet,PetAdmin)