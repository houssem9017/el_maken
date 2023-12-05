from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vr_tour', views.vr_tour, name='vr_tour'),
]
