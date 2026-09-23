from django.db import models
from django.conf import settings
from events.models import Event
import uuid

class Registration(models.Model):
    visitor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='registrations'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='registrations'
    )
    badge_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    checked_in = models.BooleanField(default=False)

    class Meta:
        unique_together = ('visitor', 'event')

    def __str__(self):
        return f"{self.visitor.username} - {self.event.title}"