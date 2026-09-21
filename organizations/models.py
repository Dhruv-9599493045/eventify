from django.db import models
from django.conf import settings

class Organization(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name='organization_profile'
    )
    org_name = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    logo = models.ImageField(upload_to='org_logos/', blank=True, null=True)
    website = models.URLField(blank = True)
    is_verified = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.org_name
    
