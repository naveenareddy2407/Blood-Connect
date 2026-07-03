from django import forms
from .models import donardetail

class Formdonar(forms.ModelForm):
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    Date_of_Birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Drinking = forms.BooleanField(required=False)
    Smoking = forms.BooleanField(required=False)
    Blood_type = forms.ChoiceField(choices=BLOOD_TYPE_CHOICES)
    class Meta:
        model = donardetail
        fields = ['Name', 'Phone', 'Blood_type', 'Address', 'current_Address', 'Date_of_Birth', 'Drinking', 'Smoking', 'Health_issue']
