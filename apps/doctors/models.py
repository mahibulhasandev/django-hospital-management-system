
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


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


class DayOfWeek(models.TextChoices):
    SATURDAY = "SATURDAY", "Saturday"
    SUNDAY = "SUNDAY", "Sunday"
    MONDAY = "MONDAY", "Monday"
    TUESDAY = "TUESDAY", "Tuesday"
    WEDNESDAY = "WEDNESDAY", "Wednesday"
    THURSDAY = "THURSDAY", "Thursday"
    FRIDAY = "FRIDAY", "Friday"


class DoctorSchedule(models.Model):

    doctor = models.ForeignKey(
        DoctorProfile,
        on_delete=models.CASCADE,
        related_name="schedules"
    )

    day_of_week = models.CharField(
        max_length=10,
        choices=DayOfWeek.choices
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    slot_duration = models.PositiveSmallIntegerField(default=15)

    break_start = models.TimeField(null=True, blank=True)

    break_end = models.TimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["day_of_week", "start_time"]
        constraints = [
            models.UniqueConstraint(
                fields=["doctor", "day_of_week"],
                name="unique_doctor_schedule_per_day"
            )
        ]

    def clean(self):
        super().clean()

        if self.start_time and self.end_time:
            if self.start_time >= self.end_time:
                raise ValidationError({
                    "end_time": "End time must be after start time."
                })

        if self.slot_duration <= 0:
            raise ValidationError({
                "slot_duration": "Slot duration must be greater than zero."
            })

        if bool(self.break_start) != bool(self.break_end):
            raise ValidationError(
                "Both break start and break end must be provided."
            )

        if self.break_start and self.break_end:
            if self.break_start >= self.break_end:
                raise ValidationError({
                    "break_end": "Break end must be after break start."
                })

            if self.start_time and self.end_time:
                if not (
                    self.start_time <= self.break_start
                    and self.break_end <= self.end_time
                ):
                    raise ValidationError(
                        "Break time must be within the doctor's schedule."
                    )

    def __str__(self):
        return f"{self.doctor.user.full_name} - {self.day_of_week}"
