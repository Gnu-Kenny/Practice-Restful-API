from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Addresses
from .serializers import AddressesSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.response import Response
# Http 통신: request / response


@csrf_exempt
def address_list(request, format=None):
    if request.method == 'GET':
        query_set = Addresses.objects.all()  # 테이블 내 튜플 모두 조회 - QuerySet
        serializer = AddressesSerializer(query_set, many=True)  # json 형태로

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)  # JSON의 형식으로 request가 들어옴.
        # 전자의 data는 Serializer에서 만든 포맷
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():  # 지정해준 형식과 client에서 받아온 JSON 포맷이 같다면
            serializer.save()  # object 생성 == Database에 튜플 생성
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)


@csrf_exempt
def address_detail(request, pk, format=None):
    try:
        # 전자 pk는 모델에서 정한 포맷 후자 pk는 request
        address = Addresses.objects.get(pk=pk)
    except Addresses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddressesSerializer(address)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':

        data = JSONParser().parse(request)  # JSON의 형식으로 request가 들어옴.

        # 전자의 data는 Serializer에서 만든 포맷
        # 어떤 pk에 관한 하나의 튜플, JSON형식의 request
        serializer = AddressesSerializer(address, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        address.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def login(request, format=None):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        requested_name = data['name']

        obj = Addresses.objects.get(name=requested_name)

        if data['phone_number'] == obj.phone_number:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
        # data = JSONParser().parse(request)
        # serializer = LoginSerializer(data=data)
        # if serializer.is_valid():
        # requested_name = serializer.data['name']
        # requested_phone_number = serializer.data['phone_number']
        #     if Addresses.objects.filter(name=requested_name, phone_number=requested_phone_number) is not None:
        #         return HttpResponse(status=status.HTTP_200_OK)
        #     return JsonResponse(serializer.data, status=202)

        # return JsonResponse(serializer.error, status=400)
