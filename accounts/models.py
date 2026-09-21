from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ORGANISATION = 'organization' , 'Organization'
        EVENT_MANAGER = 'event_manager' , 'Event Manager'
        VISITOR = 'Visitor' , 'visitor'

    role = models.CharField(
        max_length = 20,
        choices = Role.choices,
        default = Role.VISITOR
    )
    phone_number = models.CharField(max_length = 15 , blank = False, null = False)
    REQUIRED_FIELDS = ['email' , 'phone_number']
    def __str__(self):
        return f"{self.username} ({self.role})"
