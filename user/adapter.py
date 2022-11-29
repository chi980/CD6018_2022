from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from user.models import User

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        user.username = user.email.split('@')[0]
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
        print("pre_social_login!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if sociallogin.user.id:
            print("sns로그인 되어 있음")
            return
        if request.user and request.user.is_authenticated:
            print("sns로그인 계정은 없고 이미 로그인 된 상황")
            try:
                print("email이 동일")
                login_user = User.objects.get(email=request.user)
                sociallogin.connect(request, login_user)
                
            except User.DoesNotExist:
                print("email이 비동일")
                pass

    def save_user(self, request, sociallogin, form):
        # serializer = UserResigerBaseSerializer(data=request.POST)
        # serializer.is_valid()
        #
        # user = super().save_user(request, sociallogin, form)
        # return user
        print("save_user!!!!!!!!!!!!!!!!!!!!")
        print(request.POST)
        print(type(form))
        user = super(CustomSocialAccountAdapter, self).save_user(request, sociallogin, form)
        # Do what ever you want with the user
        return user
