from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from reservation_website.settings import MEDIA_URL, MEDIA_ROOT
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('account.urls')),
    path('', include('reservation.urls')),
    path('', include('exams.urls')),
    #path('api-auth/', include('rest_framework.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
