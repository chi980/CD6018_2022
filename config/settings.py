"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import pymysql
from local_settings import DATABASES, SECRET_KEY, S3
import os
pymysql.install_as_MySQLdb()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['3.34.149.198', 'www.mjupetzone.com']


# Application definition

INSTALLED_APPS = [
    'main.apps.MainConfig',
    'common.apps.CommonConfig',
    'user', # custom User
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'django.contrib.sites', #사이트,url정보 관리 해주는 기능# migrate 할 때 필요
    'allauth', #설치한앱
    'allauth.account', # 가입한 계정 관리
    'allauth.socialaccount', # 소셜 계정으로 가입한 계정 관리
    'allauth.socialaccount.providers.google', # 구글 사용
    'allauth.socialaccount.providers.kakao', # 카카오 사용
    'allauth.socialaccount.providers.naver', # 네이버 사용

]

# 로그인 과정 전에 누구한테 맡길지
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', #기본장고 유저
    'allauth.account.auth_backends.AuthenticationBackend', #소셜로그인 인증체계
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = DATABASES


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.joinpath('static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 위에'django.contrib.sites'에 첫번째 인스턴스 사용
SITE_ID = 1

LOGIN_URL = "/auth/login/"

ACCOUNT_SIGNUP_REDIRECT_URL = "/"
# 로그인 성공후 이동하는 URL
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
ACCOUNT_SIGNUP_REDIRECT_URL = "/"
LOGIN_REDIRECT_URL = '/'

# 로그아웃시 이동하는 URL
ACCOUNT_AUTHENTICATED_LOGOUT_REDIRECTS = True
LOGOUT_REDIRECT_URL = '/'

# custom user
AUTH_USER_MODEL = 'user.User'

# https://github.com/pythonkr/pyconkr/issues/27
# sns로그인 버튼을 누르는 경우 바로 로그인 화면으로 redirect
SOCIALACCOUNT_LOGIN_ON_GET=True
# 이메일 중복 가능
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
# ACCOUNT_AUTHENTICATION_METHOD = 'username'
SOCIALACCOUNT_ADAPTER = "user.adapter.CustomSocialAccountAdapter"
ACCOUNT_UNIQUE_EMAIL = False
UNIQUE_EMAIL = False
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}


# 이미지 업로드(aws s3)(https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = S3['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = S3['aws_secret_access_key']
AWS_STORAGE_BUCKET_NAME = S3['aws_storage_bucket_name']
AWS_QUERYSTRING_AUTH = S3['aws_querystring_auth']

# 이미지 업로드(file)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


ALLOWED_HOSTS = []
