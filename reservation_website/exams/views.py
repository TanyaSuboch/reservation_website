from django.views.generic import ListView, DetailView

from .models import ExamPlace, ExamStage


class ExamStageListView(ListView): #отображение перечня этапов экзамена
    queryset = ExamStage.objects.order_by('exam_stage_id')
    template_name = 'exam_stages.html'


class ExamStageDetailView(DetailView): #страница описания конкретного этапа экзамена
    model = ExamStage
    template_name = 'examstage_detail.html'


class ExamPlacesListView(ListView): #отображение перечня мест экзамена
    queryset = ExamPlace.objects.all()
    template_name = 'exam_places.html'