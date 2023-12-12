from django.contrib import messages
from django.shortcuts import render
from apps.reservations.models import ReservationForm
import json


def reserver(request):

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation_data = form.cleaned_data
            try:
                with open('data/reservations.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = []
            data.append(reservation_data)
            with open('data/reservations.json', 'w') as file:
                json.dump(data, file, indent=4)
            messages.success(request, 'Votre réservation a été soumise avec succès.')
    return render(request, 'reservations/reserver.html')
