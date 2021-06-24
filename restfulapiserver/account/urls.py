from django.urls import path
from account.views import SignUpView, SignInView


urlpatterns = [
    path('/up', SignUpView.as_view()),
    path('/in', SignInView.as_view()),
]
