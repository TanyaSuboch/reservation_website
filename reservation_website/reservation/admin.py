from django.contrib import admin

from .models import InfoPost, Reservation

class InfoPostAdmin(admin.ModelAdmin): #отображение поста в админке
    list_display = ('title', 'created_at')
    search_fields = ['title', 'body']

admin.site.register(InfoPost, InfoPostAdmin)
admin.site.register(Reservation)