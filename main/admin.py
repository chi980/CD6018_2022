from django.contrib import admin
from .models import Category
# Register your models here.

# 모델 검색
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

# 모델 관리
admin.site.register(Category, CategoryAdmin)