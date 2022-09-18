from django.contrib import admin

from .models import InfoPost, Reservation

class InfoPostAdmin(admin.ModelAdmin): #отображение поста в админке
    list_display = ('title', 'created_at')
    search_fields = ['title', 'body']


class ReservationAdmin(admin.ModelAdmin): #отображение записи на экзамен в админке
    list_display = ('reservation_id','user', 'exam_stage','exam_date','created_at', 'status')
    search_fields = ['reservation_id', 'user','exam_stage', 'exam_date', 'exam_time', 'exam_place', 'status']

admin.site.register(InfoPost, InfoPostAdmin)
admin.site.register(Reservation, ReservationAdmin)