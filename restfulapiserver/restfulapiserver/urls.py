from django.conf.urls import url, include
# addresses 폴더 내에 views.py import 시킴
from addresses.views import address_list, address_detail
from users import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('addresses/', address_list),
    path('addresses/<int:pk>', address_detail),
    path('users/', views.users),
    path('login/', views.login),
    url(r'^api-jwt-auth/$', obtain_jwt_token),          # JWT 토큰 획득
    url(r'^api-jwt-auth/refresh/$', refresh_jwt_token),  # JWT 토큰 갱신
    url(r'^api-jwt-auth/verify/$', verify_jwt_token),   # JWT 토큰 확인
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
