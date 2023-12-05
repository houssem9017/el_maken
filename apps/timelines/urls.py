from django.urls import path
from . import views

urlpatterns = [
    path('', views.timelines_list, name='timelines_list'),
    path('<int:number>', views.timeline_detail, name='timeline_detail'),
    path('aa', views.timeline_detail, name='aa'),
]
