from django.urls import path
from accounts.views import AdminRegisterView,StudentRegisterView,ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns=[
    path('admin/register/',AdminRegisterView.as_view()),
    path("student/register/",StudentRegisterView.as_view()),
    path('token/',ObtainAuthToken.as_view()),
    path('jwt/token/',TokenObtainPairView.as_view()),
    path('jwt/token/refresh/',TokenRefreshView.as_view()),
]