import json

from django.http.response import HttpResponse

from .models import Account

from django.views import View
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# Create your views here.


class SignUpView(View):

    def post(self, request):
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email=data['email']).exists():
                return HttpResponse(status=400)
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

        if Account.objects.filter(email=data['email']).exists():
            user = Account.objects.get(email=data['email'])
            if user.password == data['password']:
                return JsonResponse({'message': f'{user.email} sign up!'}, status=200)
            else:
                return JsonResponse({'message': 'wrong password'}, status=200)

        return JsonResponse({'message': 'not registered email'}, status=200)
