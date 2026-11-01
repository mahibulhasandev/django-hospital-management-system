from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.core.exceptions import PermissionDenied
from .forms import LoginForm, PatientRegistrationForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            identifier = form.cleaned_data["identifier"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=identifier,
                password=password,
            )

            if user is not None:
                login(request, user)
                return redirect("accounts:dashboard")

            messages.error(request, "Invalid email/phone or password.")

    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return render(request, "accounts/logout.html")

    return redirect("login")


@login_required
def dashboard_view(request):

    dashboards = {
        "HOSPITAL_ADMIN": "dashboards/admin.html",
        "DOCTOR": "dashboards/doctor.html",
        "NURSE": "dashboards/nurse.html",
        "RECEPTIONIST": "dashboards/receptionist.html",
        "STAFF": "dashboards/staff.html",
        "PATIENT": "dashboards/patient.html",
        "LABORATORY_TECHNICIAN": "dashboards/laboratory.html",
        "PHARMACIST": "dashboards/pharmacy.html",
    }

    template = dashboards.get(request.user.role)

    if not template:
        raise PermissionDenied("You don't have dashboard access.")

    return render(request, template)


def register_view(request):

    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your account has been created successfully. Please login."
            )

            return redirect("accounts:login")

    else:
        form = PatientRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )
