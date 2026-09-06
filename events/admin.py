from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "organization",
        "location",
        "token_prefix",
        "is_active",
    )