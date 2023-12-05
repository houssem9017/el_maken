from django.shortcuts import render

from apps.common.utils import load_data_from_json


def home(request):
    home_page_data = load_data_from_json('home_page_data.json')
    return render(request, 'main_app/home.html', {'history_data': home_page_data})


def vr_tour(request):
    return render(request, 'main_app/vr.html')
