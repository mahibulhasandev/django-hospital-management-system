
from django.db import models
from django.conf import settings


class DoctorProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile"
    )

    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.PROTECT,
        related_name="doctors"
    )

    specialization = models.CharField(max_length=150)

    qualification = models.CharField(max_length=255)

    experience_years = models.PositiveIntegerField(default=0)

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.full_name
