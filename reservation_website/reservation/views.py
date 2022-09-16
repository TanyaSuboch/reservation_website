from django.views.generic import ListView, DetailView

from .models import InfoPost, Reservation


class MainPageView(ListView): #отображение главной страницы сайта
    model = InfoPost
    template_name = 'home.html'


class InfoPostListView(ListView): #список информационной/новостной статьи
    queryset = InfoPost.objects.order_by('-created_at')
    template_name = 'home.html'


class InfoPostDetailView(DetailView): #страница деталей инфопоста
    model = InfoPost
    template_name = 'post_detail.html'


class MakeReservationView(ListView): #страница записи на экзамен
    model = Reservation
    template_name = 'make_reservation.html'