from django.urls import path
from .import views 

app_name = "events"

urlpatterns = [
    path(
        "create/<int:organization_id>/",
        views.create_event,
        name="create",
    ),

    path(
        "<int:event_id>/",
        views.event_detail,
        name="detail",
    ),
    path(
    "<int:event_id>/display/",
    views.public_display,
    name="display",
    ),

    path(
    "<int:event_id>/display/data/",
    views.public_display_partial,
    name="display_data",
    ),
]