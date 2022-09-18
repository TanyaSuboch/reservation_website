from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.utils.timezone import now

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

    EXAMTIMESLOTS = [
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
    ]

    RESERVATIONSTATUS = [
        ('Активна, не использована', 'Активна, не использована'),
        ('Использована', 'Использована'),
        ('Отменена', 'Отменена'),
    ]

    ISPAID = [
        ('Не оплачено', 'Не оплачено'),
        ('Оплачено', 'Оплачено'),
    ]

    reservation_id = models.AutoField(unique=True, primary_key=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_stage = models.OneToOneField("exams.ExamStage", on_delete=models.CASCADE, default=None)
    exam_date = models.DateField(default=datetime.now)
    exam_time = models.CharField(choices=EXAMTIMESLOTS, max_length=10, default='08:00')
    exam_place = models.OneToOneField("exams.ExamPlace", on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.CharField(default='Не оплачено', choices=ISPAID, max_length=25)
    payment_confirmation = models.ImageField(null =True, blank=True, upload_to='payment_confirmation')
    status = models.CharField(choices=RESERVATIONSTATUS, default='Активна, не использована', max_length=50)
     
    def __str__(self):
        return str(self.reservation_id)

    def get_absolute_url(self):
        return reverse('reservation_details', args=[str(self.reservation_id)])
