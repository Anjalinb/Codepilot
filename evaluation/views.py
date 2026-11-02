from django.shortcuts import render,get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework import serializers
from rest_framework.generics import UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from evaluation.models import Submission,Answer
from evaluation.permissions import IsStudentUser
from evaluation.serializers import SubmissionSerializer,AnswerSerializer

from exams.models import Assessment
from problem.models import Question

class SubmissionStartView(APIView):

    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated,IsStudentUser]

    def post(self,request,pk=None):

        assessment_id=pk

        assessment_object=get_object_or_404(Assessment,id=assessment_id)

        instance=Submission.objects.create(student=request.user,assessment=assessment_object)

        serializer_instance=SubmissionSerializer(instance)

        return Response(data=serializer_instance.data)


class AnswerCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsStudentUser]

    def post(self,request,pk=None):

        submission_id=pk

        submission_obj=get_object_or_404(Submission,id=submission_id)

        form_data=request.data

        #validation start

        assessment_object=submission_obj.assessment

        assessment_questions=Question.objects.filter(assessment=assessment_object).values_list("id",flat=True)

        qusetion=form_data.get("question")

        if qusetion not in assessment_questions:

            raise serializers.ValidationError("Invalid question, question does not exist in assessment")

        #validation end

        serializer_instance=AnswerSerializer(data=form_data)

        if serializer_instance.is_valid():


            serializer_instance.save(submission=submission_obj)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


class SubmissionDetailView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def get(self,request,pk=None):


        submission_obj=get_object_or_404(Submission,id=pk)

        serializer_instance=SubmissionSerializer(submission_obj)

        return Response(data=serializer_instance.data)


class AnswerUpdateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    
    def patch(self,request,pk=None):

        answer_id=pk

        form_data=request.data

        answer_obj=get_object_or_404(Answer,id=answer_id)

        serializer_instance=AnswerSerializer(data=form_data,instance=answer_obj,partial=True)

        serializer_instance.fields["marks_awarded"].read_only=False

        serializer_instance.fields["feedback"].read_only=False

        question_obj=answer_obj.question

        question_score=question_obj.score

        if form_data.get("marks_awarded")>question_score:

            raise serializers.ValidationError("Marks should be less than the max score")

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

        