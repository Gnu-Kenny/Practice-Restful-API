from django.conf.urls import url, include
#addresses 폴더 내에 views.py import 시킴
from addresses import views
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^addresses/', views.address_list),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
