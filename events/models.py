from django.db import models
from organizations.models import Organization

class Event(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'
        
    organizer = models.ForeignKey(
        Organization,
        on_delete = models.CASCADE,
        related_name='events'
    ) 
    
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True)
    banner_image = models.ImageField(upload_to='event_banners/', blank=True, null=True)
    venue = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    category = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
