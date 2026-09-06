from django.shortcuts import render , redirect , get_object_or_404
from organizations.models import Organization 

from .models import Event

from .forms import EventForm
# Create your views here.


def create_event(request,organization_id):
    organization = get_object_or_404(
        Organization,
        id=organization_id
    )

    if request.method =="POST":

        form = EventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.organization = organization
            event.save()

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
                "form":form,
                "organization":organization,
            }

        )

def event_detail(request,event_id):
    event  = get_object_or_404(Event , id = event_id)

    return render(
        request,
        "events/detail.html",
        {"event":event}

    )
