from django.shortcuts import render
from apps.common.utils import load_data_from_json


def timelines_list(request):
    history_data = load_data_from_json('timelines_data.json')
    timelines_data = history_data['timelines']
    return render(request, 'timelines/timelines.html', {'history_data': timelines_data})


def timeline_detail(request, number):
    history_data = load_data_from_json('timelines_data.json')
    timeline_data = history_data['timelines'][number - 1]
    return render(request, 'timelines/timeline.html', {'history_data': timeline_data})
