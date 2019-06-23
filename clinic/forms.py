from django import forms
from .models import Patient, Visit, Doctor
import datetime

class PatientForm(forms.ModelForm):
    class Meta: 
        model = Patient
        fields = ('patient_ssid', 'patient_first_name','patient_second_name','patient_family_name',
                    'patient_birth_date','patient_street','patient_city', 'patient_country',
                    'patient_zip_code')

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['patient_ssid'].widget.attrs['min'] = 0
        self.fields['patient_zip_code'].widget.attrs['min'] = 0


        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "input100",
                })

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ('visit_date','patient','attending_doctor','referring_doctor','building',
                    'floor', 'room', 'bed')

    def __init__(self, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)
        self.fields['building'].widget.attrs['min'] = 0
        self.fields['floor'].widget.attrs['min'] = 0
        self.fields['room'].widget.attrs['min'] = 0
        self.fields['bed'].widget.attrs['min'] = 0

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "input100",
                })


class ORMForm(forms.Form):
    study_cases = [('StudyID-70','StudyID-70'),('StudyID-90','StudyID-90')]
    genders = [('M','Male'),('F','Female')]
    cases = [('X-rays Ankle','X-rays Ankle'),('X-rays Arm','X-rays Arm')]
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
    case = forms.ChoiceField(choices=cases)
    gender = forms.ChoiceField(choices=genders)
    study_id = forms.ChoiceField(choices= study_cases)

    def __init__(self, *args, **kwargs):
        super(ORMForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "input100",
                })