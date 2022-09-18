from urllib import request
from django import forms

from .models import Reservation
from account.models import User


class MakeReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['exam_stage', 'exam_date', 'exam_time','exam_place', 'is_paid','payment_confirmation']

    
    EXAMSTAGESCHOICE = [
        ('1','Теория'),
        ('2','Площадка'),
        ('3','Город'),
    ]

    exam_stage = forms.CharField(label='Этап экзамена:',
        max_length=50, 
        required=True, 
        widget=forms.RadioSelect(choices=EXAMSTAGESCHOICE))

    RESERVATIONYEARS = ['2022','2023']

    exam_date = forms.DateField(label='Дата экзамена:',
        required=True,
        widget=forms.SelectDateWidget(years=RESERVATIONYEARS))
        
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

    exam_time = forms.CharField(label='Время экзамена:',
        max_length=10,
        required=True, 
        widget=forms.Select(choices=EXAMTIMESLOTS))

    EXAMPLACESCHOICE = [('1','Минское областное ГАИ'),('2','Минское городское ГАИ')]

    exam_place = forms.CharField(label='Место экзамена:',
        max_length=200, 
        required=True, 
        widget=forms.RadioSelect(choices=EXAMPLACESCHOICE))
    
    PAYMENTSTATUS = [('Не оплачено', 'Не оплачено'), ('Оплачено', 'Оплачено')]

    is_paid = forms.CharField(label='Наличие оплаты:',
        max_length=25,
        required=True, 
        widget=forms.RadioSelect(choices=PAYMENTSTATUS))

    payment_confirmation = forms.ImageField(label='Подтверждение оплаты:', 
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control-file'}))