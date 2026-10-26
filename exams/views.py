from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveAPIView,DestroyAPIView,UpdateAPIView

from exams.models import Assessment
from exams.serializers import AssessmentSerializer
from exams.permissions import IsOwner

from datetime import datetime,time

class AssessmentListCreateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        qs=Assessment.objects.filter(created_by=request.user)
        serializer_instance=AssessmentSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=AssessmentSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(created_by=request.user)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class AssessmentRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    serializer_class=AssessmentSerializer
    queryset=Assessment.objects.all()
    
        

