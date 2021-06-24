from django.conf.urls import url, include
# addresses 폴더 내에 views.py import 시킴
from addresses.views import address_list, address_detail
from users.views import users, profile
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework_simplejwt import views as jwt_views

# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('addresses/', address_list),
    path('addresses/<int:pk>', address_detail),
    path('users/', users),
    path('profile/', profile),
    path('account', include('account.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
