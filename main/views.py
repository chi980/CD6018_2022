# from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Location, Review, Category
from .models import Category
from django.db.models import Q
from django.db.models import Avg
# Create your views here.

def index(request):
    # return HttpResponse("안녕하세요 main에 오신것을 환영합니다.")
    # category_list = Category.objects.all()
    # context = {'category_list':category_list}
    # return render(request,'main/index.html',context)
    recommended = None
    if request.method == "POST":
        if request.user.is_authenticated:
            cur_logitude = request.logitude
            cur_latitude = request.latitude
            cur_scale = request.scale | 50
            cur_logitude_min = cur_logitude - cur_scale
            cur_latitude_min = cur_latitude - cur_scale
            cur_logitude_max = cur_logitude + cur_scale
            cur_latitude_max = cur_latitude + cur_scale
            # 화면에 들어오는 장소들의 id list
            # locations = Location.objects.filter(Q(longitude__range=(cur_logitude_min,cur_logitude_max)) & Q(latitude__range=(cur_latitude_min,cur_latitude_max))).values_list('id',flat=True)
            locations = Location.objects.filter(Q(longitude__range=(cur_logitude_min,cur_logitude_max)) & Q(latitude__range=(cur_latitude_min,cur_latitude_max)) & Q(category_id=request.user.category))
            recommended = Review.objects.filter(Q(location_id__in=locations) & Q(category_id=request.user.category)).values('location').annotate(avg=Avg('star')).order_by('-avg')[:10]

            return render(request,'main/index.html',{'recommended':recommended})
        else:
            return redirect('index')
    else:
        return render(request,'main/index.html',{'recommended':recommended})