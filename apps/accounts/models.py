from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Define this module's models here.

class User(AbstractBaseUser, PermissionsMixin):
    
    class Role(models.TextChoices):
        HOSPITAL_ADMIN = "HOSPITAL_ADMIN", "Hospital Admin"
        DOCTOR = "DOCTOR", "Doctor"
        NURSE = "NURSE", "Nurse"
        RECEPTIONIST = "RECEPTIONIST", "Receptionist"
        STAFF = "STAFF", "Staff"
        PATIENT = "PATIENT", "Patient"
        
    email = models.EmailField(
        max_length=254,
        unique=True,
        null=True,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )
    
    full_name = models.CharField(max_length=150)

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.PATIENT)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]


    def __str__(self):
        return self.full_name
    
    