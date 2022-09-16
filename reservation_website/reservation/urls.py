from django.urls import path
from .views import MainPageView, InfoPostDetailView,InfoPostListView, MakeReservationView


urlpatterns = [
    path('home/', MainPageView.as_view(), name='home'),
    path('post/<int:pk>/', InfoPostDetailView.as_view(), name='post_detail'),
    path('', InfoPostListView.as_view(), name='home'),
    path('make_reservation/', MakeReservationView.as_view(), name='make_reservation'),
]