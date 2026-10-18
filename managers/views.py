from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import EventManagerAssignment


@login_required
def manager_dashboard(request):
    if request.user.role != 'event_manager':
        messages.error(request, "You don't have access to this page.")
        return redirect('home')

    assignments = (
        EventManagerAssignment.objects
        .filter(manager=request.user)
        .select_related('event')
        .order_by('event__start_date')
    )
    return render(request, 'managers/dashboard.html', {'assignments': assignments})