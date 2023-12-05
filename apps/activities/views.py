from django.shortcuts import render
from apps.activities.models import Activity


def activities_list(request):
    activity_objects = Activity.objects.all().order_by('date')
    return render(request, 'activities/activities.html', {'activities': activity_objects})
