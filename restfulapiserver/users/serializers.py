from rest_framework import serializers
from .models import User

# data를 JSON 형태로 바꿔줌
# serializers.Serializer vs serializers.ModelSerializer
# 전자에 경우 클래스 내에 사용할 모델(테이블)의 필드 각각을 serialize 해줄 수 있다.
# 후자는 Meta 클래스에서 import 시킨 모델(테이블)명을 입력하면 일일이 필드 값 입력없이 전체를 불러온 것처럼 사용할 수 있다.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
