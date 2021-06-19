from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Addresses
from .serializers import AddressesSerializer
from django.views.decorators.csrf import csrf_exempt

# Http 통신: request / response
@csrf_exempt
def address_list(request):
    if request.method == 'GET':
        query_set = Addresses.objects.all() #테이블 내 튜플 모두 조회 - QuerySet
        serializer = AddressesSerializer(query_set, many=True)  # json 형태로
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)  #JSON의 형식으로 request가 들어옴.
        serializer = AddressesSerializer(data=data) #전자의 data는 Serializer에서 만든 포맷
        if serializer.is_valid(): #지정해준 형식과 client에서 받아온 JSON 포맷이 같다면
            serializer.save() #object 생성 == Database에 튜플 생성 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)
