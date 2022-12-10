from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from user.models import User
from django.shortcuts import HttpResponse
class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def populate_user(self, request, sociallogin, data):
        social_app_name = sociallogin.account.provider.lower()
        user = super().populate_user(request, sociallogin, data)
        user.username = user.email.split('@')[0] + social_app_name
        # print("여기는 adaoter")
        # print(user)
        # print(user.email)
        #
        # print("*"*10)
        # print(sociallogin.user)
        # print("*"*10)
        # print(data)
        # print("*"*10)
        # print(request.POST)


        return user

    def pre_social_login(self, request, sociallogin):
        # print("pre_social_login!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # if sociallogin.user.id:
            # print("sns로그인 되어 있음")
            # return
        if request.user and request.user.is_authenticated:
            # print("sns로그인 계정은 없고 이미 로그인 된 상황")
            try:
                # print("email이 동일")
                login_user = User.objects.get(email=request.user)
                sociallogin.connect(request, login_user)
                
            except User.DoesNotExist:
                # print("email이 비동일")
                pass

    def save_user(self, request, sociallogin, form):
        # data = form.cleaned_data
        # user = super().save_user(request, sociallogin, form)
        # return user
        # print("save_user!!!!!!!!!!!!!!!!!!!!")
        # print(type(form))
        # pre_user = User.objects.get(email = sociallogin.user.email)
        # if not pre_user:
        #     user = super(CustomSocialAccountAdapter, self).save_user(request, sociallogin, form)
        #         # Do what ever you want with the user
        #     return user
        # return super(CustomSocialAccountAdapter, self).save_user(request, pre_user, form)
        # return HttpResponse("<script>alert('입력하신 내용을 다시 확인해주세요.');location.href='/';</script>")
        user = super(CustomSocialAccountAdapter, self).save_user(request, sociallogin, form)
        # Do what ever you want with the user
        return user