from django.conf.urls import url, include
# addresses 폴더 내에 views.py import 시킴
from addresses.views import address_list, address_detail
from users.views import users, login, HelloView
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views

# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('addresses/', address_list),
    path('addresses/<int:pk>', address_detail),
    path('users/', users),
    path('login/', login),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('hello/', HelloView, name='hello'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
