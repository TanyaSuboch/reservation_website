# Generated by Django 4.1 on 2022-09-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('result', models.IntegerField(choices=[(0, 'Не сдан'), (1, 'Сдан')], default='Не сдан')),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exams',
                'db_table': 'Exams',
            },
        ),
        migrations.CreateModel(
            name='ExamPlace',
            fields=[
                ('exam_place_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'ExamPlace',
                'verbose_name_plural': 'ExamPlaces',
                'db_table': 'ExamPlaces',
            },
        ),
        migrations.AlterField(
            model_name='examstage',
            name='frequency',
            field=models.IntegerField(choices=[(10, 'Раз в 10 дней'), (30, 'Раз в месяц')], default=10),
        ),
    ]