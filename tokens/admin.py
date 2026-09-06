from django.contrib import admin
from .models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "event",
        "status",
        "counter",
        "generated_at",
        "called_at",
        "finished_at",
    )

    list_filter = (
        "status",
        "event",
        "counter",
    )

    search_fields = (
        "number",
    )