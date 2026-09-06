from django.db import models
from events.models import Event

# Create your models here.

class Counter(models.Model):
    event= models.ForeignKey(
        Event,
        on_delete = models.CASCADE,
        related_name="counters"
    )

    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event.name}-{self.name}"
    