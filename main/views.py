from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render
from .models import Category
def index(request):
    # return HttpResponse("안녕하세요 main에 오신것을 환영합니다.")
    category_list = Category.objects.all()
    context = {'category_list':category_list}
    return render(request,'main/index.html',context)