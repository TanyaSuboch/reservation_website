from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from reservation.models import Reservation


class ExamStage(models.Model):
    class Meta:
        db_table = "ExamStages"
        verbose_name = _('ExamStage')
        verbose_name_plural = _('ExamStages')

    FREQUENCY = [
        ('Раз в 10 дней', 'Раз в 10 дней'),
        ('Раз в месяц', 'Раз в месяц')
    ]

    exam_stage_id = models.AutoField(unique=True, primary_key=True, null=False)
    name = models.CharField(max_length=50)
    frequency = models.CharField(choices=FREQUENCY, default='Раз в 10 дней', max_length= 20)
    description = models.TextField()
     
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('examstage_details', args=[str(self.exam_stage_id)])


class ExamPlace(models.Model):
    class Meta:
        db_table = "ExamPlaces"
        verbose_name = _('ExamPlace')
        verbose_name_plural = _('ExamPlaces')

    exam_place_id = models.AutoField(unique=True, primary_key=True, null=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    description = models.TextField()
     
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('examplace_details', args=[str(self.exam_place_id)])


class Exam(models.Model):
    class Meta:
        db_table = "Exams"
        verbose_name = _('Exam')
        verbose_name_plural = _('Exams')

    RESULT = (
        ('Не сдан', 'Не сдан'),
        ('Cдан', 'Сдан')
    )

    exam_id = models.AutoField(unique=True, primary_key=True, null=False)
    result = models.CharField(choices = RESULT,default='Не сдан', max_length= 15)
    reservation_id = models.OneToOneField(Reservation, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.result

    def get_absolute_url(self):
        return reverse('exams_details', args=[str(self.exam_id)])