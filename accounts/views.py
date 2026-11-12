from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

from accounts.models import User,StudentProfile
from accounts.serializers import UserSerializer,StudentProfileSerializer

from evaluation.permissions import IsStudentUser


class AdminRegisterView(APIView):

    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            admin_obj=User.objects.create_superuser(role="admin",**cleaned_data)
            serializer_instance=UserSerializer(admin_obj)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class StudentRegisterView(APIView):

    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            student_obj=User.objects.create_user(**cleaned_data)
            serializer_instance=UserSerializer(student_obj)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class ProfileUpdateView(APIView):

    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated,IsStudentUser]

    def put(self,request):

        form_data=request.data

        student_profile_obj=StudentProfile.objects.get(student=request.user)

        serializer_instance=StudentProfileSerializer(data=form_data,instance=student_profile_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


class ProfileDetailView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated,IsStudentUser]

    def get(self,request):

        qs=StudentProfile.objects.get(student=request.user)
        serializer_instance=StudentProfileSerializer(qs)
        return Response(data=serializer_instance.data)