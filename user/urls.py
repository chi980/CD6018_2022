from django.urls import path,include
from . import views

app_name = "user"

urlpatterns = [
    path("login", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("signup", views.user_signup, name="signup"),
    path('api/user/',include('allauth.urls')),
    path('',views.sociallogin,name='sociallogin')
]