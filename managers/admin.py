from django.contrib import admin
from .models import EventManagerAssignment


@admin.register(EventManagerAssignment)
class EventManagerAssignmentAdmin(admin.ModelAdmin):
    list_display = ['manager', 'event', 'assigned_at']
    list_filter = ['event']