# Generated by Django 4.1 on 2022-09-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_rename_avatar_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default='default.jpg', height_field=100, upload_to='profile_images', width_field=100),
        ),
    ]
