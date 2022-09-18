from django.contrib import admin

from .models import User, UserProfile

class UserAdmin(admin.ModelAdmin): #отображение инфо о пользователе в админке
    list_display = ['last_name','first_name', 'patronymic_name','date_of_birth','registration_city']
    search_fields = ['user_id', 'passport_id', 'registration_city']

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)