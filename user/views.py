from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,HttpResponseRedirect,get_object_or_404,HttpResponse
from .models import User,Pet,Favorite
from main.models import Location
from user.forms import UserForm,PetForm, MyUserChangeForm, CategoryChangeForm
from django.contrib import messages

from django.contrib.auth import get_user_model
# 로그인 필요
from django.contrib.auth.decorators import login_required

# json 처리
from django.http import JsonResponse,HttpResponse
from django.core import serializers
import json
from django.template.loader import render_to_string
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        print("sns로그인도  useR_login?")
        print(request.POST)
        print(request.POST['password'])
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
            return redirect('index')
        else:
            print("인증실패")
            # return redirect('user:login')
            return HttpResponse("<script>alert('입력하신 내용을 다시 확인해주세요.');location.href='/';</script>")
    # return render(request, "user/login.html")
    else:
        return render(request,'base.html')

@login_required
def user_logout(request):
    logout(request)
    # return redirect("user:login")
    return redirect('index')

def user_signup(request):
    # if request.method == "POST":
    #     print(request.POST)
    #     # username = request.POST["username"]
    #     username = request.POST.get('username')
    #     # password = request.POST["password"]
    #     password = request.POST.get('password')
    #     # lastname = request.POST['lastname']
    #     firstname = request.POST.get('firstname')
    #     # email = request.POST['email']
    #     email = request.POST.get('email')
    #
    #     # gender = request.POST.get('gender')
    #
    #     user = User.objects.create_user(username=username, password=password,first_name=firstname,email=email)
    #     # user.gender = gender
    #     # user.last_name = lastname
    #     # user.email = email
    #
    #     user.save()
    #     # return redirect("user:login")
    #     print("user 생성!")
    #     return redirect('index')
    # return render(request, "user/signup.html")
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return render(request,'user/catecory.html')
    else:
        form = UserForm()
        print(form.GENDER_CHOICES)
        print(form.GENDER_CHOICES)

    return render(request, 'user/signup.html', {'form': form})
    # return render(request, 'navbar.html', {'form': form})

def sociallogin(request):
    return render(request,'base.html')

@login_required
def mypage_pet(request):
    # pet_form = PetForm(request=request,user = request.user)
    # pet_form = PetForm()
    my_pet = Pet.objects.filter(user=request.user)
    return render(request, 'user/mypage_pet.html', {'my_pet': my_pet})
#https://han-py.tistory.com/147
@login_required
def mypage_user(request):
    if request.method == 'POST':
        form = MyUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user:mypage_user')
    else:
        form = MyUserChangeForm(instance=request.user)
        return render(request, 'user/mypage_user.html',{'form':form})    #여기 user 수정 폼 들어가야함

@login_required
def mypage_place(request):
    favorites = Favorite.objects.filter(user=request.user)
    # favorites_json = json.loads(serializers.serialize('json', favorites, ensure_ascii=False))
    # pet_form = PetForm()
    return render(request, 'user/mypage_place.html',{'favorites':favorites})
    # return JsonResponse({
    #     'html': render_to_string('user/mypage_place.html', {'favorites':favorites_json or None}, request=request),
    # })
@login_required(login_url='/')
def pet(request, pet_id):
    # my_pet = Pet.objects.get(user = request.user)
    # current_pet = Pet.objects.get(id=pet_id)
    # pet_form = PetForm(request=request, user=request.user)
    my_pet = get_object_or_404(Pet,pk=pet_id)
    # Post 방식 요청
    if request.method == 'POST':
        form = PetForm(request.POST,instance=my_pet)
        if form.is_valid():
            print("form is valid")
            my_pet = form.save(commit=False)
            my_pet.save()
            return redirect('/')
            # return redirect('user:mypage_pet',pet_id=my_pet.pk)
        else:
            return redirect('/')
    else:
        print(my_pet)
        pet_form = PetForm(instance=my_pet)
        # pet_form = PetForm(instance=my_pet)
        # return redirect('user:mypage_pet')
    # # Get 방식 요청
    # else:
    #     pet_form = PetForm(request=request,user = request.user)
    #     # pet_form = PetForm()
    #     return render(request, 'user/pet.html', {'pet_form': pet_form})
        return render(request, 'user/pet.html', {'my_pet':my_pet,'pet_form':pet_form})


@login_required
#로그인 추가하기
def favorite(request):
    # if request.user.is_authenticated:
    #     if request.method == "POST":
    #         location_id = request.POST.get('location_id')
    #         location = Location.objects.get(id=location_id)
    #         my_favorite = Favorite.objects.get_or_create(user=request.user, location__id=location_id)
    #         return HttpResponse(status=201)
    #     else:
    #         # favorites = Favorite.objects.all()
    #         favorites = Favorite.objects.filter(user=request.user)
    #         favorites_json = json.loads(serializers.serialize('json',favorites,ensure_ascii=False))
    #         # return HttpResponse(favorites_json,content_type="text/json-comment-filtered")
    #         return JsonResponse({'reload_all': False, 'favorites_json': favorites_json})
    # else:
    #     #401상태코드
    #     #https://devlog.jwgo.kr/2020/10/17/fancy-messaging-system-in-django/
    #     #https://han-py.tistory.com/105
    #     return HttpResponse(status=401)
    if request.method == "POST":
        location_id = request.POST.get('location_id')
        location = Location.objects.get(id=location_id)
        my_favorite = Favorite.objects.get_or_create(user=request.user, location__id=location_id)
        return HttpResponse(status=201)
    else:
        # favorites = Favorite.objects.all()
        favorites = Favorite.objects.filter(user=request.user)
        favorites_json = json.loads(serializers.serialize('json',favorites,ensure_ascii=False))
        # return HttpResponse(favorites_json,content_type="text/json-comment-filtered")
        return JsonResponse({'reload_all': False, 'favorites_json': favorites_json})

# 페이징
# def business_list(request):
#    business_list = Business.objects.all().order_by('-id') #데이터 역순 정렬
#    page = request.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
#    paginator = Paginator(business_list, '2') #Paginator(분할될 객체, 페이지 당 담길 객체수)
#    paginated_business_lists = paginator.get_page(page) #페이지 번호를 받아 해당 페이지를 리턴
#    ctx = {'business_list':business_list,'paginated_business_lists':paginated_business_lists}
#
#    return render(request, template_name='list.html', context=ctx)

#message사용법:https://stackoverflow.com/questions/28240746/django-how-to-implement-alertpopup-message-after-complete-method-in-view

def delFavorite(request):
    if request.method=='POST':
        try:
            favorite_id = request.favorite_id
            record = Favorite.objects.get(id=favorite_id)
            record.delete()
            messages.info(request,'성공적으로 지워졌습니다.')
            return HttpResponseRedirect('user:mypage_place')
        except:
            messages.info(request, '없는 객체입니다.')
            return HttpResponse(status=400)
    return HttpResponse(status=200)

    
def user_catecory(request):
    # return render(request,'user/catecory.html')
    if request.method == 'POST':
        change_form = CategoryChangeForm(request.POST, instance=request.user)
        if change_form.is_valid():
            change_form.save()
            return redirect('index')
    else:
        change_form = CategoryChangeForm(instance=request.user)
        return render(request,'user/change_category.html', {'change_form':change_form})

def user_category_change(request):
    if request.method == 'POST':
        print('POST')
        change_form = CategoryChangeForm(request.POST, instance=request.user)
        if change_form.is_valid():
            print('form valid')
            change_form.save()
            return redirect('index')
        else:
            print('form invalid')
            return redirect('index')
    else:
        change_form = CategoryChangeForm(instance=request.user)
        return render(request,'user/change_category.html', {'change_form':change_form})
#     pass
