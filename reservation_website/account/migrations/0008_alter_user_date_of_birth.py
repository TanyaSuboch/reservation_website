# Generated by Django 4.1 on 2022-09-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default='01.01.2000'),
        ),
    ]