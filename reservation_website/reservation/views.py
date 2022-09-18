from django.views.generic import ListView, DetailView, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string


from .forms import MakeReservationForm
from .models import InfoPost, Reservation
from .pdf_convert import html_to_pdf


class MainPageView(ListView): #отображение главной страницы сайта
    model = InfoPost
    template_name = 'home.html'


class InfoPostListView(ListView): #список информационной/новостной статьи
    queryset = InfoPost.objects.order_by('-created_at')
    template_name = 'home.html'


class InfoPostDetailView(DetailView): #страница деталей инфопоста
    model = InfoPost
    template_name = 'post_detail.html'


@login_required
def make_reservation(request):
    if request.method == 'POST':
        make_reservation_form = MakeReservationForm(request.POST)
        
        if make_reservation_form.is_valid():
            reservation: reservation = make_reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect(to='home')

    else:
        make_reservation_form = MakeReservationForm()

    return render(request, 'make_reservation.html', {'make_reservation_form': make_reservation_form})


class ReservationsListView(ListView): #перечень записей на экзамен
    queryset = Reservation.objects.order_by('-created_at')
    template_name = 'reservations_list.html'


class ReservationDetailsView(DetailView): #детали записи на экзамен
    model = Reservation
    template_name = 'reservation_details.html'


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        open('temp.html', "w").write(render_to_string('templates/reservation_details_pdf.html'))
        pdf = html_to_pdf('temp.html')
      
        return HttpResponse(pdf, content_type='make_reservation/pdf')