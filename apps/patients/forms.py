from django import forms
from .models import PatientProfile


class PatientProfileForm(forms.ModelForm):

    class Meta:
        model = PatientProfile
        fields = [
            "date_of_birth",
            "gender",
            "blood_group",
            "address",
            "profile_picture",
            "emergency_contact_name",
            "emergency_contact_phone",
        ]
