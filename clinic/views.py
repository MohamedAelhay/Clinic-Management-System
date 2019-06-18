from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from clinic.models import Patient, Visit, Doctor
from .forms import PatientForm, VisitForm
from django.http import JsonResponse
import json
import requests
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from clinic.serializer import DataSerializer
from CMS import settings

def index(request):
    return render(request, 'index.html')

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

def new_visit(request):
    if request.method == 'POST':
        visit_form = VisitForm(request.POST)
        if visit_form.is_valid():
            visit_form.save()
            return data_JSON(request)
        #     return HttpResponseRedirect("/clinic/new")
    else:
        visit_form = VisitForm()
        context = {'visit_form': visit_form}
        return render(request, 'visit.html', context)


def data_JSON(request):

    visit = Visit.objects.order_by('visit_id').last()
    patient = Patient.objects.get(pk=visit.patient_id)
    attending_doctor = Doctor.objects.get(pk=visit.attending_doctor_id)
    referring_doctor = Doctor.objects.get(pk=visit.referring_doctor_id)

    meta_data = {
        'BROKER_KEY': settings.BROKER_KEY,
        'TE': "ADT",
        'SCOPE': "A01",
        'DEVICE': "1"
    }
    
    msg_data_arr = [patient,visit,attending_doctor,referring_doctor,meta_data]
    
    serialize_obj = DataSerializer(msg_data_arr)
    serialized_data = serialize_obj.serialize()
    print(serialized_data)
    url = 'http://127.0.0.1:8001/api/parse/'
    req = requests.post(url, data=serialized_data, verify=False)
    print(req.status_code)
#     return JsonResponse(req.status_code, safe=False)
    return HttpResponse(req, content_type='application/json')    