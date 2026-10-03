from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from events.models import Event
from .models import Registration
from django.http import HttpResponse
import qrcode
import io

@login_required
def my_registrations(request):
    registrations = Registration.objects.filter(visitor = request.user).select_related('event').order_by('-registered_at')
    return render (request , 'visitors/my_registerations.html' , {'registrations':registrations})

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

@login_required
def registration_qr(request, badge_id):
    registration = get_object_or_404(Registration,badge_id=badge_id,visitor=request.user)

    qr = qrcode.QRCode(box_size=8, border = 2)
    qr.add_data(str(registration.badge_id))
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black" , back_color= "white")

    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    return HttpResponse(buffer.getvalue() , content_type ='img/png')
