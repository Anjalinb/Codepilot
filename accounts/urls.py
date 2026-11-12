from django.urls import path
from accounts.views import AdminRegisterView,StudentRegisterView,ObtainAuthToken,ProfileUpdateView,ProfileDetailView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns=[
    path('admin/register/',AdminRegisterView.as_view()),
    path("student/register/",StudentRegisterView.as_view()),
    path('token/',ObtainAuthToken.as_view()),
    path('jwt/token/',TokenObtainPairView.as_view()),
    path('jwt/token/refresh/',TokenRefreshView.as_view()),
    path('profile/complete/',ProfileUpdateView.as_view()),
    path('profile/detail/',ProfileDetailView.as_view()),
]