from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from main.models import Location, Review, Category
from user.models import User
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
    return render(request,'main/index.html')


@csrf_exempt
@require_POST
def recommended(request):
    jsonObject = json.loads(request.body)
    # print("Ajax 데이터를 받았음")
    # print("남서쪽:",jsonObject.get('swLatlng'))
    # print("북동쪽:",jsonObject.get('neLatlng'))
    print(jsonObject.get('swLatlng')['Ma'])
    print(jsonObject.get('swLatlng')['La'])

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
        locations = Location.objects.filter(Q(longitude__range=(cur_longitude_min, cur_longitude_max)) & Q(latitude__range=(cur_latitude_min, cur_latitude_max)))
        locations_store = locations.filter(~Q(category=2)).values_list('id', flat=True)
        locations_cafe = locations.filter(Q(category=0)).values()
        locations_restau = locations.filter(Q(category=1)).values()

        locations_cafe_list = json.dumps(list(locations_cafe),cls=DecimalEncoder,ensure_ascii=False)
        locations_restau_list = json.dumps(list(locations_restau),cls=DecimalEncoder,ensure_ascii=False)
        # pet관련 장소 리스트
        if (request.user.on_off == 1):
            locations_pet = locations.filter(Q(category=2)).values()
            # locations_pet_list = serializers.serialize('json', locations_pet)
            locations_pet_list = json.dumps(list(locations_pet),cls=DecimalEncoder,ensure_ascii=False)
        # 추천 리스트
        if (request.user.category):
            raw_recommended = Review.objects.filter(Q(category_id=request.user.category)&Q(location_id__in=locations_store)).values('location_id').annotate(star_avg=Avg('star'))[:5]
            recommended = raw_recommended.values('location_id', 'location__name', 'location__category',
                                     'location__address','location__lot_address','location__phone',
                                     'location__time','location__url','location__is_animal_in',
                                     'location__latitude','location__longitude','star_avg')
            # user_favorites = User.objects.filter(id=request.user.id).
            recommended_list = json.dumps(list(recommended),cls=DecimalEncoder, ensure_ascii=False)
        else:
            response = JsonResponse({"error": "카테고리 설정이 필요합니다."})
            response.status_code = 403  # To announce that the user isn't allowed to publish
            # return response
            return HttpResponse("<script>alert('카테고리 설정이 필요합니다.');location.href='/auth/category';</script>")
        if not recommended:
            return JsonResponse({"locations_cafe":locations_cafe_list,"locations_restau":locations_restau_list,"locations_pet":locations_pet_list})
        print("*" * 100)
        print(recommended)
        return JsonResponse({"recommended":recommended_list,"locations_cafe":locations_cafe_list,"locations_restau":locations_restau_list,"locations_pet":locations_pet_list}, safe=False)
        # return HttpResponse("<script>alert('추천할 장소가 없습니다.');</script>")
    else:
        response = JsonResponse({"error": "로그인이 필요합니다."})
        response.status_code = 403  # To announce that the user isn't allowed to publish
        # return response
        return HttpResponse("<script>alert('로그인이 필요합니다');location.href='/auth/login';</script>")


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):

            return str(round(obj,2))
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)


