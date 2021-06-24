import json
import bcrypt                            # 암호화에 사용
import jwt                               # 토큰 발행에 사용

from restfulapiserver.settings import SECRET_KEY  # 토큰 발행에 사용할 secret key
from .models import Account

from django.views import View
from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# Create your views here.


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email=data['email']).exists():
                return HttpResponse(status=400)

            #==== 비밀번호 암호화====#

            password = data['password'].encode(
                'utf-8')                 # 입력된 패스워드를 바이트 형태로 인코딩
            password_crypt = bcrypt.hashpw(
                password, bcrypt.gensalt())  # 암호화된 비밀번호 생성
            password_crypt = password_crypt.decode(
                'utf-8')  # DB에 저장할 수 있는 유니코드 문자열 형태로 디코딩

            #====================#

            Account(
                email=data['email'],
                password=data['password']
            ).save()						# 받아온 데이터를 DB에 저장시켜줌

            return JsonResponse({'message': 'successfully signed in'}, status=200)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)


# @method_decorator(csrf_exempt)
class SignInView(View):

    def post(self, request):
        data = json.loads(request.body)

        try:
            if Account.objects.filter(email=data['email']).exists():
                user = Account.objects.get(email=data['email'])

                if user.password == data['password']:
                    return HttpResponse(status=200)

                return HttpResponse(status=401)

            return HttpResponse(status=400)

        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)
