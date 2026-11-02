from django.urls import path
from evaluation.views import SubmissionStartView,AnswerCreateView
from evaluation.views import SubmissionDetailView,AnswerUpdateView

urlpatterns=[
    path('assessment/<int:pk>/submission/',SubmissionStartView.as_view()),
    path('submission/<int:pk>/answer/',AnswerCreateView.as_view()),
    path('submission/<int:pk>/',SubmissionDetailView.as_view()),
    path('answers/<int:pk>/',AnswerUpdateView.as_view()),
]