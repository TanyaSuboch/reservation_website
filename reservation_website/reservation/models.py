from time import timezone
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from datetime import timezone

from account.models import User


class InfoPost(models.Model): #блок с информацией, создаётся и редактируется только через админку
    class Meta:
        verbose_name = _('InfoPost')
        verbose_name_plural = _('InfoPosts')
        ordering = ['-created_at']

    id = models.AutoField(unique=True, primary_key=True, null=False)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Reservation(models.Model): #модель записи на экзамен
    class Meta:
        db_table = "Reservations"
        verbose_name = _('Reservation')
        verbose_name_plural = _('Reservations')

    reservation_id = models.AutoField(unique=True, primary_key=True, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_stage = models.OneToOneField("exams.ExamStage", on_delete=models.CASCADE, default=None)
    #exam_date = models.DateField()
    #exam_time = models.TimeField()
    exam_place = models.OneToOneField("exams.ExamPlace", on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    is_used = models.BooleanField(default=False)
    #deleted_at = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.reservation_id

    def get_absolute_url(self):
        return reverse('reservation_details', args=[str(self.reservation_id)])
