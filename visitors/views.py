from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from events.models import Event
from .models import Registration

@login_required
def register_for_event(request, pk):
    event = get_object_or_404(Event, pk=pk, status=Event.Status.PUBLISHED)

    already_registered = Registration.objects.filter(visitor=request.user, event=event).exists()

    if already_registered:
        messages.info(request, "You're already registered for this event.")
    else:
        Registration.objects.create(visitor=request.user, event=event)
        messages.success(request, f"You've successfully registered for {event.title}!")

    return redirect('event_detail', pk=event.pk)