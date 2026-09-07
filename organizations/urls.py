from django.urls import path
from . import views

app_name = "organizations"

urlpatterns = [
    path(
        "",
        views.organization_list,
        name="list",
    ),
    path(
        "create/",
        views.create_organization,
        name="create",
    ),

    path("<int:organization_id>/",
         views.organization_detail,
         name="detail",
         ),
]