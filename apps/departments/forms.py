from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = [
            "name",
            "description",
            "head_of_department",
            "image",
            "is_active",
        ]
