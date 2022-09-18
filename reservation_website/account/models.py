from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.utils.timezone import now


class User(AbstractUser): #экзаменуемый
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    patronymic_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    passport_id = models.CharField(max_length=14)
    date_of_birth = models.DateField(default='01.01.2000')
    registration_city = models.CharField(max_length=50)
    
    class Meta():
        db_table = "Users"
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username


class UserProfile(models.Model): #профиль экзаменуемого
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.png', upload_to='profile_images')
    additional_info = models.TextField()
       
    def __str__(self):
        return self.user.username