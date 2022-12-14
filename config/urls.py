"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf.urls.static import static
from django.conf import settings

# sns 로그인
# from auth.apis import (
#     LoginApi,
#     LogoutApi,
#     GoogleLoginApi,
#     GoogleSigninCallBackApi
# )
# from auth.googleapi import *


# login_patterns = [
#     path('google', GoogleLoginApi.as_view(), name='google_login'),
#     path('google/callback', GoogleSigninCallBackApi.as_view(), name='google_login_callback'),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include('main.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path
    path('auth/',include('user.urls')),
    path('accounts/',include('allauth.urls'))
]

# 디버그 환경에서 media 확인 가능하게 함
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
