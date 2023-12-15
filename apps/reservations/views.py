from django.contrib import messages
from django.shortcuts import render
from apps.reservations.models import ReservationForm


def reserver(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre réservation a été soumise avec succès.')
    return render(request, 'reservations/reserver.html')
