from django.conf.urls import url, include
from addresses import views
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# Serializers define the API representation.


# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^addresses/', views.address_list),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff'] #유저 테이블 내 serialize할 필드 선택 


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
#users를 호출하면 UserViewSet을 호출
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    url(r'^addresses/', views.address_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
