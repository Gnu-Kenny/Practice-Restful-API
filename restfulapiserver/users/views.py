from rest_framework.serializers import Serializer
from .decorators import login_decorator
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

# Http 통신: request / response

# JWT to login
from .decorators import login_decorator
# from rest_framework.views import APIView

# import jwt
# from rest_framework.permissions import IsAuthenticated


@csrf_exempt
def users(request, format=None):
    if request.method == 'GET':
        query_set = User.objects.all()  # 테이블 내 튜플 모두 조회 - QuerySet
        serializer = UserSerializer(query_set, many=True)  # json 형태로

        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():  # 지정해준 형식과 client에서 받아온 JSON 포맷이 같다면
            serializer.save()  # object 생성 == Database에 튜플 생성
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def login(request, format=None):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         session = request.session

#         print(type(session['JWT_TOKEN']))
#         if 'JWT_TOKEN' in session:
#             prev_dic = jwt.decode(
#                 session['JWT_TOKEN'], SECRET_PRE, algorithm='HS256')
#         else:
#             prev_dic = {}
#         print(prev_dic)
#         serializer = UserSerializer(data=data)
#         # user = authenticate(
#         #     username=request.POST['username'], password=request.POST['password'])

#         if serializer.is_valid():  # 지정해준 형식과 client에서 받아온 JSON 포맷이 같다면
#             serializer.save()  # object 생성 == Database에 튜플 생성
#         user = User.objects.get(username=data['username'])
#         user_serializer = UserSerializer(user)
#         print(user_serializer.data)
#         encoded = jwt.encode(dict(user_serializer.data),
#                              SECRET_PRE, algorithm="HS256")
#         session['JWT_TOKEN'] = encoded
#         return HttpResponse(status=200)


# @csrf_exempt
# def HelloView(request):
#     permission_classes = (IsAuthenticated,)
#     if request.method == "GET":
#         content = {'message': 'Hello, World!'}
#         return Response(content)

# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)

@csrf_exempt
@login_decorator
def profile(request):

    if request.method == "GET":

        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
