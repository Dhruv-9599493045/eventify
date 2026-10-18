from django.db import models
from django.conf import settings
from events.models import Event


class EventManagerAssignment(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='manager_assignments'
    )
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='manager_assignments',
        limit_choices_to={'role': 'event_manager'}
    )
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'manager')

    def __str__(self):
        return f"{self.manager.username} -> {self.event.title}"