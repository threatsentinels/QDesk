


from django.urls import path

from . import views


app_name = "tokens"


urlpatterns = [

    path(
        "generate/<int:event_id>/",
        views.generate_token,
        name="generate",
    ),

    path(
        "call-next/<int:event_id>/",
        views.call_next,
        name="call_next",
    ),

    path(
        "finish/<int:token_id>/",
        views.finish_token,
        name="finish",
    ),

    path(
        "print/<int:token_id>/",
        views.print_token,
        name="print",
    ),

]