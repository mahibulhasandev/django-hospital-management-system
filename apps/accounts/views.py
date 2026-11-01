from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

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
                return redirect("dashboard")

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
    return HttpResponse(
        f"Welcome to Hospital Management System, {request.user.full_name}!"
    )