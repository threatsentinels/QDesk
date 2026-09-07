from django.db import models
from events.models import Event
from counters.models import Counter


class Token(models.Model):

    class Status(models.TextChoices):
        WAITING = "waiting", "Waiting"
        SERVING = "serving", "Serving"
        FINISHED = "finished", "Finished"
        CANCELLED = "cancelled", "Cancelled"

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="tokens"
    )

    number = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.WAITING
    )

    counter = models.ForeignKey(
        Counter,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tokens"
    )

    generated_at = models.DateTimeField(auto_now_add=True)

    called_at = models.DateTimeField(null=True, blank=True)

    started_at = models.DateTimeField(null=True, blank=True)

    finished_at = models.DateTimeField(null=True, blank=True)



    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["event","number"],
                name = "unique_token_number_per_event",
                
            )
        ]
    def __str__(self):
        return f"{self.event.token_prefix}-{self.number:03d}"