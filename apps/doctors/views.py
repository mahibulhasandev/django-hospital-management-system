from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from .models import DoctorProfile
from .forms import DoctorCreationForm, DoctorUpdateForm


def hospital_admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("accounts:login")

        if request.user.role != "HOSPITAL_ADMIN":
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrapper


@login_required
@hospital_admin_required
def doctor_list(request):
    doctors = DoctorProfile.objects.select_related(
        "user", "department"
    ).all()

    return render(
        request,
        "doctors/doctor_list.html",
        {"doctors": doctors}
    )


@login_required
@hospital_admin_required
def doctor_create(request):
    if request.method == "POST":
        form = DoctorCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Doctor created successfully.")
            return redirect("doctors:doctor_list")
    else:
        form = DoctorCreationForm()

    return render(
        request,
        "doctors/doctor_form.html",
        {"form": form, "title": "Add Doctor"}
    )


@login_required
@hospital_admin_required
def doctor_detail(request, pk):
    doctor = get_object_or_404(
        DoctorProfile.objects.select_related("user", "department"),
        pk=pk
    )

    return render(
        request,
        "doctors/doctor_detail.html",
        {"doctor": doctor}
    )


@login_required
@hospital_admin_required
def doctor_update(request, pk):
    doctor = get_object_or_404(DoctorProfile, pk=pk)

    if request.method == "POST":
        form = DoctorUpdateForm(request.POST, instance=doctor)

        if form.is_valid():
            form.save()
            messages.success(request, "Doctor updated successfully.")
            return redirect("doctors:doctor_list")
    else:
        form = DoctorUpdateForm(instance=doctor)

    return render(
        request,
        "doctors/doctor_form.html",
        {"form": form, "title": "Update Doctor"}
    )


@login_required
@hospital_admin_required
def doctor_delete(request, pk):
    doctor = get_object_or_404(DoctorProfile, pk=pk)

    if request.method == "POST":
        doctor.delete()
        messages.success(request, "Doctor profile deleted successfully.")
        return redirect("doctors:doctor_list")

    return render(
        request,
        "doctors/doctor_detail.html",
        {"doctor": doctor, "confirm_delete": True}
    )
