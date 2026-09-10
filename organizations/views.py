from django.shortcuts import render, redirect , get_object_or_404

from .forms import OrganizationForm 
from .models import Organization 

def organization_list(request):
    organizations = Organization.objects.order_by("-created_at")
    return render(
        request,
        "organizations/list.html",
        {
            "organizations":organizations,
        },
    )

def organization_detail(request,organization_id):
    organization= get_object_or_404(
        Organization,
        id=organization_id,
    )

    events = organization.events.order_by("-created_at")

    return render(
        request,
        "organizations/detail.html",{
        "organization":organization,
        "events":events,},
    )

def create_organization(request):
    if request.method == "POST":
        form = OrganizationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("organizations:list")
    else:
        form = OrganizationForm()

    return render(
        request,
        "organizations/create.html",
        {"form": form},
    )