from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg, F, ExpressionWrapper, DurationField

from organizations.models import Organization
from .forms import EventForm
from .models import Event

def create_event(request, organization_id):
    organization = get_object_or_404(
        Organization,
        id=organization_id
    )

    if request.method == "POST":
        form = EventForm(request.POST)

        print("POST DATA:", request.POST)
        print("FORM VALID:", form.is_valid())
        print("FORM ERRORS:", form.errors)

        if form.is_valid():
            event = form.save(commit=False)
            event.organization = organization
            event.save()

            print("EVENT CREATED:", event.id)

            return redirect(
                "events:detail",
                event_id=event.id
            )

    else:
        form = EventForm()

    return render(
        request,
        "events/create.html",
        {
            "form": form,
            "organization": organization,
        }
    )

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    tokens = event.tokens.order_by("number")

    total_tokens = tokens.count()

    waiting_tokens = tokens.filter(
        status="waiting"
    ).count()

    serving_tokens = tokens.filter(
        status="serving"
    ).count()

    finished_tokens = tokens.filter(
        status="finished"
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

    return render(
        request,
        "events/detail.html",
        {
            "event": event,
            "tokens": tokens,
            "total_tokens": total_tokens,
            "waiting_tokens": waiting_tokens,
            "serving_tokens": serving_tokens,
            "finished_tokens": finished_tokens,
            "average_wait": average_wait,
            "average_service": average_service,
        }
    )
