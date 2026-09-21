from django.contrib import admin
from .models import Organization

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['org_name', 'user', 'is_verified', 'created_at']
    list_filter = ['is_verified']
    search_fields = ['org_name']
