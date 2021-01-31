from django.conf.urls import url, include
from addresses import views
# Serializers define the API representation.


# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^addresses/', views.address_list),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
