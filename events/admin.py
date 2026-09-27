from django.contrib import admin
from .models import Event, Session

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'organizer', 'venue', 'start_date', 'end_date', 'status']
    list_filter = ['status', 'category']
    search_fields = ['title', 'venue']

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'event', 'speaker', 'start_time', 'end_time', 'capacity']
    list_filter = ['event']
    search_fields = ['title', 'speaker']