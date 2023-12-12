from django.core.serializers import deserialize, serialize
from django.shortcuts import render


def activities_list(request):
    with open('data/activities.json', 'r', encoding='utf-8') as file:
        serialized_activities = file.read()
    activity_objects = [obj.object for obj in deserialize('json', serialized_activities)]
    return render(request, 'activities/activities.html', {'activities': activity_objects})
