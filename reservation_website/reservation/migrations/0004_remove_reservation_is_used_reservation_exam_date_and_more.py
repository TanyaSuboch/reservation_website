# Generated by Django 4.1 on 2022-09-17 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_reservation_exam_place_reservation_exam_stage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='is_used',
        ),
        migrations.AddField(
            model_name='reservation',
            name='exam_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='reservation',
            name='exam_time',
            field=models.CharField(choices=[('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00')], default='08:00', max_length=10),
        ),
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Активна, не использована', 'Активна, не использована'), ('Использована', 'Использована'), ('Отменена', 'Отменена')], default='Активна, не использована', max_length=50),
        ),
    ]