from django.db import models
from organizations.models import Organization 

# Create your models here.

class Event(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name ="events"
    )

    name = models.CharField(max_length=150)
    location = models.CharField(max_length=200, blank=True)

    token_prefix = models.CharField(
        max_length=10,
        default="A"
    )

    starting_number = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.organization.name}-{self.name}"
    

