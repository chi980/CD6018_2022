# from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Location, Review, Category
from .models import Category
from django.db.models import Q
from django.db.models import Avg
# Create your views here.

def index(request):
    recommended = None
    if request.user.is_authenticated:
            #남서쪽 위도 경도(swLatlng): '33.44953470033243, 126.56849976573322'
            #북동쪽 위도 경도(neLatlng): '33.451124628187245, 126.5719981820737'

            cur_longitude = 127.0117172
            cur_latitude = 37.5563644
            cur_scale = 50.0
            cur_longitude_min = cur_longitude - cur_scale
            cur_latitude_min = cur_latitude - cur_scale
            cur_longitude_max = cur_longitude + cur_scale
            cur_latitude_max = cur_latitude + cur_scale

            # cur_latitude_min = str(request.swLatlng).split(,)[0]
            # cur_latitude_max = str(request.neLatlng).split(,)[0]
            # cur_longitude_min = str(request.swLatlng).split(,)[1]
            # cur_longitude_max = str(request.neLatlng).split(,)[1]

            # locations = Location.objects.all()

            # recommended = Review.objects.filter(Q(location_id__in=locations) & Q(category=request.user.category)).values('location').annotate(avg=Avg('star')).order_by('-avg')[:10]

            locations = Location.objects.filter(Q(logitude__range=[cur_longitude_min,cur_longitude_max]) & Q(latitude__range=[cur_latitude_min,cur_latitude_max])).values_list('id',flat=True)
            # locations = Location.objects.filter(Q(logitude__range=[cur_longitude_min,cur_longitude_max]) & Q(latitude__range=[cur_latitude_min,cur_latitude_max]))

            recommended= Review.objects.filter(Q(location_id__in=locations) & Q(category=request.user.category)).values('location','location__name','location__address','location__lot_address','location__phone','location__time','location__url','location__is_animal_in','location__latitude','location__logitude').annotate(avg=Avg('star')).order_by('-avg')[:10]
    return render(request,'main/index.html',{'recommended':recommended})