from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Patient, Visit, Doctor
from .forms import PatientForm, VisitForm

def new_patient(request):
    if request.method == 'POST':
        patient_form = PatientForm(request.POST) 
        if patient_form.is_valid():
            patient_form.save()
            return HttpResponseRedirect("/clinic/visit")
    else:
        patient_form = PatientForm()
        context = {'patient_form': patient_form}
        return render(request, 'new.html', context)

# Create your views here.

def new_visit(request):
    if request.method == 'POST':
        visit_form = VisitForm(request.POST)
        if visit_form.is_valid():
            visit_form.save()
            return HttpResponseRedirect("/clinic/new")
   
    else:
        visit_form = VisitForm()
        context = {'visit_form': visit_form}
        return render(request, 'visit.html', context)
