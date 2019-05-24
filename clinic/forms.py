from django import forms
from .models import Patient, Visit, Doctor

class PatientForm(forms.ModelForm):
    class Meta: 
        model = Patient
        fields = ('patient_ssid', 'patient_first_name','patient_second_name','patient_family_name',
                    'patient_birth_date','patient_street','patient_city', 'patient_country',
                    'patient_zip_code')

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ('visit_date','patient','attending_doctor','referring_doctor','building',
                    'floor', 'room', 'bed')