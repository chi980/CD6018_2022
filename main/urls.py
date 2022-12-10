from django.urls import path

from . import views
app_name = 'main'

# front_end에서 url: {% url 'app_name:url별칭' 어쩌구저쩌구 %}
urlpatterns = [
    # path('', views.index,name='index'),
    path('recommended/',views.recommended,name='recommended'),
    path('favorites/',views.favorite,name='favorite')
]