from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Organization
from .forms import EventForm

@login_required
def dashboard(request):
    if request.user.role != 'organization':
        messages.error(request, "You don't have access to this page.")
        return redirect('home')

    organization = get_object_or_404(Organization, user=request.user)
    events = organization.events.all().order_by('-created_at')
    return render(request, 'organizations/dashboard.html', {'organization': organization, 'events': events})

@login_required
def create_event(request):
    if request.user.role != 'organization':
        messages.error(request, "You don't have access to this page.")
        return redirect('home')

    organization = get_object_or_404(Organization, user=request.user)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = organization
            event.save()
            messages.success(request, "Event created successfully!")
            return redirect('org_dashboard')
    else:
        form = EventForm()

    return render(request, 'organizations/event_form.html', {'form': form})