from django.shortcuts import render
from .models import Event

def home(request):
    events = Event.objects.filter(status=Event.Status.PUBLISHED).order_by('start_date')
    return render(request, 'home.html', {'events': events})
