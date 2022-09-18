from django.urls import path
from .views import MainPageView, InfoPostDetailView,InfoPostListView, make_reservation, ReservationDetailsView, ReservationsListView, GeneratePdf


urlpatterns = [
    path('home/', MainPageView.as_view(), name='home'),
    path('post/<int:pk>/', InfoPostDetailView.as_view(), name='post_detail'),
    path('', InfoPostListView.as_view(), name='home'),
    path('make_reservation/', make_reservation, name='make_reservation'),
    path('make_reservation/reservation/<int:pk>/', ReservationDetailsView.as_view(), name='reservation_details'),
    path('make_reservation/reservations/', ReservationsListView.as_view(), name='reservations_list'),
    path('make_reservation/pdf/', GeneratePdf.as_view(), name='reservation_details_pdf'),

    #path('make_reservation/make_payment/', name='make_payment'),
]