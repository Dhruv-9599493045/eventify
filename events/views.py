from django.shortcuts import render, get_object_or_404
from .models import Event

def home(request):
    events = Event.objects.filter(status=Event.Status.PUBLISHED).order_by('start_date')
    return render(request, 'home.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, status=Event.Status.PUBLISHED)
    return render(request, 'events/event_detail.html', {'event': event})

def home(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')

    events = Event.objects.filter(status=Event.Status.PUBLISHED)

    if query:
        events = events.filter(title__icontains=query)
    if category:
        events = events.filter(category__iexact=category)

    events = events.order_by('start_date')

    categories = Event.objects.filter(status=Event.Status.PUBLISHED).exclude(category='').values_list('category', flat=True).distinct()

    return render(request, 'home.html', {'events': events, 'query': query, 'category': category, 'categories': categories})