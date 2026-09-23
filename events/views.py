from django.shortcuts import render, get_object_or_404
from .models import Event

def home(request):
    events = Event.objects.filter(status=Event.Status.PUBLISHED).order_by('start_date')
    return render(request, 'home.html', {'events': events})

def event_details(request,pk):
    event = get_object_or_404(Event,pk=pk,status = Event.Status.PUBLISHED)
    return render(request,'events/event_details.html',{'event':event})