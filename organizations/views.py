from django.shortcuts import render, redirect
from .forms import OrganizationForm


def create_organization(request):
    if request.method == "POST":
        form = OrganizationForm(request.POST, request.FILES)

        if form.is_valid():
            organization = form.save()

            return redirect(
                "events:create",
                organization_id=organization.id
            )

    else:
        form = OrganizationForm()

    return render(
        request,
        "organizations/create.html",
        {"form": form}
    )