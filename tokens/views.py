from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Avg, F, ExpressionWrapper, DurationField

from events.models import Event
from .models import Token


def dashboard_context(event):
    tokens = event.tokens.order_by("number")

    total_tokens = tokens.count()

    waiting_tokens = tokens.filter(
        status=Token.Status.WAITING
    ).count()

    serving_tokens = tokens.filter(
        status=Token.Status.SERVING
    ).count()

    finished_tokens = tokens.filter(
        status=Token.Status.FINISHED
    ).count()

    completed_tokens = tokens.filter(
        finished_at__isnull=False,
        called_at__isnull=False,
    )

    average_wait = completed_tokens.annotate(
        wait_time=ExpressionWrapper(
            F("called_at") - F("generated_at"),
            output_field=DurationField(),
        )
    ).aggregate(
        average=Avg("wait_time")
    )["average"]

    average_service = completed_tokens.annotate(
        service_time=ExpressionWrapper(
            F("finished_at") - F("started_at"),
            output_field=DurationField(),
        )
    ).aggregate(
        average=Avg("service_time")
    )["average"]

    return {
        "event": event,
        "tokens": tokens,
        "total_tokens": total_tokens,
        "waiting_tokens": waiting_tokens,
        "serving_tokens": serving_tokens,
        "finished_tokens": finished_tokens,
        "average_wait": average_wait,
        "average_service": average_service,
    }

def generate_token(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":

        last_token = (
            Token.objects
            .filter(event=event)
            .order_by("-number")
            .first()
        )

        if last_token:
            next_number = last_token.number + 1
        else:
            next_number = event.starting_number

        Token.objects.create(
            event=event,
            number=next_number,
        )

    if request.headers.get("HX-Request"):
        return render(
            request,
            "events/partials/dashboard.html",
            dashboard_context(event),
        )

    return redirect(
        "events:detail",
        event_id=event.id
    )


def call_next(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":

        token = (
            Token.objects
            .filter(
                event=event,
                status=Token.Status.WAITING,
            )
            .order_by("number")
            .first()
        )

        if token:

            now = timezone.now()

            token.status = Token.Status.SERVING
            token.called_at = now
            token.started_at = now

            token.save()

    if request.headers.get("HX-Request"):
        return render(
            request,
            "events/partials/dashboard.html",
            dashboard_context(event),
        )

    return redirect(
        "events:detail",
        event_id=event.id
    )

def finish_token(request, token_id):

    token = get_object_or_404(Token, id=token_id)

    if request.method == "POST":

        token.status = Token.Status.FINISHED
        token.finished_at = timezone.now()

        token.save()

    if request.headers.get("HX-Request"):
        return render(
            request,
            "events/partials/dashboard.html",
            dashboard_context(token.event),
        )

    return redirect(
        "events:detail",
        event_id=token.event.id
    )