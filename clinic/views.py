from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from clinic.models import Patient, Visit, Doctor
from .forms import PatientForm, VisitForm, ORMForm
from django.http import JsonResponse
import json
import requests
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from clinic.serializer import ADTSerializer, ORMSerializer
import os

def index(request):
    return render(request, 'index.html')

def new_orm(request):
    if request.method == 'POST':
        form = ORMForm(request.POST)
        if form.is_valid():
            serialized_obj = ORMSerializer(form)
            serialized_data = serialized_obj.serialize()
            
            url = 'http://127.0.0.1:'+os.environ.get('BROKER_PORT', '')+'/api/parse/mwl/'
            req = requests.post(url, data=serialized_data, verify=False)
            print(req.status_code)
            if (req.status_code == 200):
                return render(request, 'success.html', msg_data_dict)
            else:
                return render(request, 'fail.html')
            return HttpResponseRedirect('/')

    else:
        form = ORMForm()

    return render(request, 'orm.html', {'form': form})


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
            return send_request(request)
            # if(is_request_sent):
            #     return render(request, 'success.html')
            # else:
            #     return render(request, 'fail.html')


    else:
        visit_form = VisitForm()
        context = {'visit_form': visit_form}
        return render(request, 'visit.html', context)


def send_request(request):

    visit = Visit.objects.order_by('visit_id').last()
    patient = Patient.objects.get(pk=visit.patient_id)
    attending_doctor = Doctor.objects.get(pk=visit.attending_doctor_id)
    referring_doctor = Doctor.objects.get(pk=visit.referring_doctor_id)

    msg_data_dict = {
        'patient' : patient,
        'visit': visit,
        'attending_doctor': attending_doctor,
        'referring_doctor': referring_doctor
    }

    serialize_obj = ADTSerializer(msg_data_dict)
    serialized_data = serialize_obj.serialize()
    url = 'http://127.0.0.1:'+os.environ.get('BROKER_PORT', '')+'/api/parse/'
    req = requests.post(url, data=serialized_data, verify=False)
    if (req.status_code == 200):
        return render(request, 'success.html', msg_data_dict)
    else:
        return render(request, 'fail.html')