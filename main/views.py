from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from main.models import Location, Review, Category
from .models import Category
from django.db.models import Q
from django.db.models import Avg
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import json
from django.core import serializers
from decimal import Decimal
# Create your views here.


def index(request):
    recommended = None
    locations_pet = None
    locations_pet_list = None
    recommended_list = None
    # if request.method == 'POST':
    #     if request.user.is_authenticated:
    #         cur_latitude_min = request.get('swLatlng_lat')
    #         cur_latitude_max = request.get('neLatlng_lat')
    #         cur_longitude_min = request.get('swLatlng_lon')
    #         cur_longitude_max = request.get('neLatlng_lon')
    #
    #         locations = Location.objects.filter(Q(logitude__range=(cur_longitude_min, cur_longitude_max)) & Q(latitude__range=(cur_latitude_min, cur_latitude_max)))
    #         locations_res = locations.filter(Q(on_off=0)).values_list('id', flat=True)
    #
    #         # pet관련 장소 리스트
    #         if (request.user.on_off == 1):
    #             locations_pet = locations.filter(Q(on_off=1))
    #             locations_pet_list = serializers.serialize('json', locations_pet)
    #
    #         # 추천 리스트
    #         if (request.user.category):
    #             recommended = Review.objects.filter(
    #                 Q(category_id=request.user.category) & Q(location_id__in=locations_res)).values('location_id').annotate(
    #                 star_avg=Avg('star'))[:5] \
    #                 .values('location_id', 'location__name', 'location__category',
    #                         'location__address', 'location__lot_address', 'location__phone',
    #                         'location__time', 'location__url', 'location__is_animal_in',
    #                         'location__latitude', 'location__logitude', 'location__on_off', 'star_avg')
    #             # print(recommended)
    #             recommended_list = json.dumps(list(recommended), cls=DecimalEncoder, ensure_ascii=False)
    #         else:
    #             # response = JsonResponse({"error": "카테고리 설정이 필요합니다."})
    #             # response.status_code = 403  # To announce that the user isn't allowed to publish
    #             # return response
    #             return HttpResponse("<script>alert('카테고리 설정이 필요합니다.');location.href='/';</script>")
    #         if not recommended:
    #             # response = JsonResponse({"error": "추천할 장소가 없습니다."})
    #             # response.status_code = 403  # To announce that the user isn't allowed to publish
    #             # return response
    #             return HttpResponse("<script>alert('추천할 장소가 없습니다.');location.href='/';</script>")
    #     else:
    #         # response = JsonResponse({"error": "로그인이 필요합니다."})
    #         # response.status_code = 403  # To announce that the user isn't allowed to publish
    #         # return response
    #         return HttpResponse("<script>alert('로그인이 필요합니다.');location.href='/';</script>")
    #     # return render(request,'main/index.html',{"recommended":recommended,"locations_pet":locations_pet,"locations":locations})
    #     return redirect("/");
    # # if request.user.is_authenticated:
    # #         #남서쪽 위도 경도(swLatlng): '33.44953470033243, 126.56849976573322'
    # #         #북동쪽 위도 경도(neLatlng): '33.451124628187245, 126.5719981820737'
    # #
    # #         cur_longitude = 127.0117172
    # #         cur_latitude = 37.5563644
    # #         cur_scale = 50.0
    # #         cur_longitude_min = cur_longitude - cur_scale
    # #         cur_latitude_min = cur_latitude - cur_scale
    # #         cur_longitude_max = cur_longitude + cur_scale
    # #         cur_latitude_max = cur_latitude + cur_scale
    # #         print(cur_latitude_min,cur_latitude_max)
    # #         print( cur_longitude_min, cur_longitude_max)
    # #
    # #         # cur_latitude_min = str(request.swLatlng).split(,)[0]
    # #         # cur_latitude_max = str(request.neLatlng).split(,)[0]
    # #         # cur_longitude_min = str(request.swLatlng).split(,)[1]
    # #         # cur_longitude_max = str(request.neLatlng).split(,)[1]
    # #
    # #         # locations = Location.objects.all()
    # #
    # #         # recommended = Review.objects.filter(Q(location_id__in=locations) & Q(category=request.user.category)).values('location').annotate(avg=Avg('star')).order_by('-avg')[:10]
    # #
    # #         # locations = Location.objects.filter(Q(logitude__range=[cur_longitude_min,cur_longitude_max]) & Q(latitude__range=[cur_latitude_min,cur_latitude_max])).values_list('id',flat=True)
    # #         # locations = Location.objects.filter(Q(logitude__range=[cur_longitude_min,cur_longitude_max]) & Q(latitude__range=[cur_latitude_min,cur_latitude_max]))
    # #         locations = Location.objects.filter(Q(logitude__range=[cur_longitude_min,cur_longitude_max]) & Q(latitude__range=[cur_latitude_min,cur_latitude_max]))
    # #         locations_res = locations.filter(Q(on_off = 0)).values_list('id',flat=True)
    # #
    # #         if(request.user.on_off == 1):
    # #             locations_pet = locations.filter(Q(on_off = 1))
    # #         print(locations_pet)
    # #         recommended= Review.objects.filter(Q(location_id__in=locations_res) & Q(category=request.user.category)).values('location','location__name','location__address','location__lot_address','location__phone','location__time','location__url','location__is_animal_in','location__latitude','location__logitude').annotate(avg=Avg('star')).order_by('-avg')[:10]
    # #
    # # return render(request,'main/index.html')
    # else:
    return render(request,'main/index.html')
@csrf_exempt
@require_POST
def recommended(request):
    jsonObject = json.loads(request.body)
    # print("Ajax 데이터를 받았음")
    # print("남서쪽:",jsonObject.get('swLatlng'))
    # print("북동쪽:",jsonObject.get('neLatlng'))
    cur_latitude_min = jsonObject.get('swLatlng')['Ma']
    cur_latitude_max = jsonObject.get('neLatlng')['Ma']
    cur_longitude_min = jsonObject.get('swLatlng')['La']
    cur_longitude_max = jsonObject.get('neLatlng')['La']

    # cur_latitude_min = 37.47919116788586
    # cur_latitude_max = 37.48531880573196
    # cur_longitude_min = 126.97144148512074
    # cur_longitude_max = 126.97486509760063

    locations_pet = None
    recommended = None
    locations_pet_list = None
    recommended_list = None
    if request.user.is_authenticated:
        # 해당 지역 내의 location
        locations = Location.objects.filter(Q(logitude__range=(cur_longitude_min, cur_longitude_max)) & Q(latitude__range=(cur_latitude_min, cur_latitude_max)))
        locations_res = locations.filter(Q(on_off=0)).values_list('id', flat=True)

        # pet관련 장소 리스트
        if (request.user.on_off == 1):
            locations_pet = locations.filter(Q(on_off=1))
            locations_pet_list = serializers.serialize('json', locations_pet)

        # 추천 리스트
        if (request.user.category):
            recommended = Review.objects.filter(Q(category_id=request.user.category)&Q(location_id__in=locations_res)).values('location_id').annotate(star_avg=Avg('star'))[:5]\
                .values('location_id', 'location__name', 'location__category',
                                     'location__address','location__lot_address','location__phone',
                                     'location__time','location__url','location__is_animal_in',
                                     'location__latitude','location__logitude','location__on_off','star_avg')
            # print(recommended)
            recommended_list = json.dumps(list(recommended),cls=DecimalEncoder, ensure_ascii=False)
        else:
            response = JsonResponse({"error": "카테고리 설정이 필요합니다."})
            response.status_code = 403  # To announce that the user isn't allowed to publish
            return response
        if not recommended:
            response = JsonResponse({"error": "추천할 장소가 없습니다."})
            response.status_code = 403  # To announce that the user isn't allowed to publish
            return response
        return JsonResponse({"recommended":recommended_list,"locations_pet":locations_pet_list}, safe=False)
    else:
        response = JsonResponse({"error": "로그인이 필요합니다."})
        response.status_code = 403  # To announce that the user isn't allowed to publish
        return response


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):

            return str(round(obj,2))
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)


