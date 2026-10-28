from rest_framework import serializers
from evaluation.models import Submission,Answer

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Submission
        fields="__all__"
        read_only_fields=[fields]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields="__all__"
        read_only_fields=["id","submission","marks_awarded","feedback","evaluated_at"]
