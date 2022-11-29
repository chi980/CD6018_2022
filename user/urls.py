from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "user"

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("signup/", views.user_signup, name="signup"),
    # path("mypage/", views.mypage,name="mypage"),
    path("pet/<int:pet_id>",views.pet,name="pet"),
    path("mypage_pet/", views.mypage_pet,name="mypage_pet"),
    path("mypage_user/", views.mypage_user,name="mypage_user"),
    path("mypage_place/", views.mypage_place,name="mypage_place"),
    # path('api/user/',include('allauth.urls')),
    # path('',views.sociallogin,name='sociallogin')
    path("favorite/",views.favorite,name="favorite"),
    path("catecory/",views.user_catecory,name="catecory"),
    path("change_category/",views.user_category_change,name="change_category"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)