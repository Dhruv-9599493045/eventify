from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Organization 
from .forms import EventForm , SessionForm
from events.models import Event , Session
from django.contrib.auth import get_user_model
from managers.models import EventManagerAssignment

User = get_user_model()

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

@login_required
def add_session(request, event_pk):
    organization = get_object_or_404(Organization, user=request.user)
    event = get_object_or_404(Event, pk=event_pk, organizer=organization)

    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.event = event
            session.save()
            messages.success(request, "Session added successfully!")
            return redirect('org_dashboard')
    else:
        form = SessionForm()

    return render(request, 'organizations/session_form.html', {'form': form, 'event': event})

@login_required
def edit_event(request, pk):
    organization = get_object_or_404(Organization, user=request.user)
    event = get_object_or_404(Event, pk=pk, organizer=organization)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully!")
            return redirect('org_dashboard')
    else:
        form = EventForm(instance=event)

    return render(request, 'organizations/event_form.html', {'form': form, 'event': event, 'editing': True})

@login_required
def delete_event(request, pk):
    organization = get_object_or_404(Organization, user=request.user)
    event = get_object_or_404(Event, pk=pk, organizer=organization)

    if request.method == 'POST':
        event.delete()
        messages.success(request, f'"{event.title}" has been deleted.')
        return redirect('org_dashboard')

    return render(request, 'organizations/event_confirm_delete.html', {'event': event})

@login_required
def assign_manager(request, event_pk):
    if request.user.role != 'organization':
        messages.error(request, "You don't have access to this page.")
        return redirect('home')

    organization = get_object_or_404(Organization, user=request.user)
    event = get_object_or_404(Event, pk=event_pk, organizer=organization)

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        try:
            manager = User.objects.get(username=username, role='event_manager')
        except User.DoesNotExist:
            messages.error(request, f'No Event Manager account found with username "{username}".')
        else:
            _, created = EventManagerAssignment.objects.get_or_create(event=event, manager=manager)
            if created:
                messages.success(request, f"{manager.username} was assigned to this event.")
            else:
                messages.info(request, f"{manager.username} is already assigned.")
        return redirect('assign_manager', event_pk=event.pk)

    assignments = event.manager_assignments.select_related('manager')
    return render(request, 'organizations/assign_manager.html', {'event': event, 'assignments': assignments})


@login_required
def remove_manager(request, assignment_pk):
    organization = get_object_or_404(Organization, user=request.user)
    assignment = get_object_or_404(EventManagerAssignment, pk=assignment_pk, event__organizer=organization)
    event_pk = assignment.event.pk

    if request.method == 'POST':
        assignment.delete()
        messages.success(request, "Manager removed.")
    return redirect('assign_manager', event_pk=event_pk)