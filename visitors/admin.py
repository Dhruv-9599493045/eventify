from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['visitor', 'event', 'badge_id', 'checked_in', 'registered_at']
    list_filter = ['checked_in', 'event']
    search_fields = ['visitor__username', 'event__title']