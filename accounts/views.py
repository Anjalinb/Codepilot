from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

from accounts.models import User
from accounts.serializers import UserSerializer

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