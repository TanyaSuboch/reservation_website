from django.urls import path
from .views import ExamStageListView, ExamStageDetailView, ExamPlacesListView


urlpatterns = [
    path('exams/', ExamStageListView.as_view(), name='exam_stages'),
    path('exams/<int:pk>/', ExamStageDetailView.as_view(), name= 'examstage_detail'),
    path('exams/places', ExamPlacesListView.as_view(), name= 'exam_places'),
]