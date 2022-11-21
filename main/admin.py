from django.contrib import admin
from .models import Category,Review,Location
# Register your models here.

# 모델 검색
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

class LocationAdmin(admin.ModelAdmin):
    pass

class ReviewAdmin(admin.ModelAdmin):
    pass
# 모델 관리
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Review,ReviewAdmin)