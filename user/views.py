from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .models import User

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
        else:
            print("인증실패")
    return render(request, "user/login.html")


def user_logout(request):
    logout(request)
    return redirect("user:login")


def user_signup(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        lastname = request.POST["lastname"]

        user = User.objects.create_user(username, password)
        user.last_nam = lastname
        user.save()
        return redirect("user:login")

    return render(request, "user/signup.html")