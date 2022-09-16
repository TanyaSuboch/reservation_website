from django.contrib import admin

from exams.models import ExamStage, ExamPlace, Exam

admin.site.register(ExamStage)
admin.site.register(ExamPlace)
admin.site.register(Exam)
