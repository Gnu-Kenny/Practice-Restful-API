from django.conf.urls import url, include
# addresses 폴더 내에 views.py import 시킴
from addresses import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('addresses/', views.address_list),
    path('addresses/<int:pk>', views.address_detail),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
