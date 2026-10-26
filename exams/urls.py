from django.urls import path
from exams.views import AssessmentListCreateView,AssessmentRetrieveUpdateDeleteView

urlpatterns=[
    path('assessments/',AssessmentListCreateView.as_view()),
    path('assessments/<int:pk>/',AssessmentRetrieveUpdateDeleteView.as_view()),
    
]