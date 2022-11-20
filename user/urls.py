from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "user"

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("signup/", views.user_signup, name="signup"),
    path("mypage/", views.mypage,name="mypage"),
    path("petcreate/",views.petcreate,name="petcreate"),
    # path('api/user/',include('allauth.urls')),
    # path('',views.sociallogin,name='sociallogin')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)