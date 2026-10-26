from django.urls import path
from accounts.views import AdminRegisterView,StudentRegisterView,ObtainAuthToken

urlpatterns=[
    path('admin/register/',AdminRegisterView.as_view()),
    path("student/register/",StudentRegisterView.as_view()),
    path('token/',ObtainAuthToken.as_view()),
]