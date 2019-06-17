from django import forms
from .models import Patient, Visit, Doctor

class PatientForm(forms.ModelForm):
    class Meta: 
        model = Patient
        fields = ('patient_ssid', 'patient_first_name','patient_second_name','patient_family_name',
                    'patient_birth_date','patient_street','patient_city', 'patient_country',
                    'patient_zip_code')

    #    widgets = {
    #        'patient_first_name': forms.TextInput(attrs={'class': 'form-control text-white',
    #                                                    'placeholder': 'First Name'}),
    #    }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control",
                    'placeholder': field.label
                })
                field.label = ''

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ('visit_date','patient','attending_doctor','referring_doctor','building',
                    'floor', 'room', 'bed')

    def __init__(self, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control",
                    'placeholder': field.label
                })
                field.label = ''
