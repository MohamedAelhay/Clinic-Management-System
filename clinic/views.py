from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Patient, Visit, Doctor
from .forms import PatientForm, VisitForm
from django.http import JsonResponse
import json
import requests
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers


def new_patient(request):
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            patient_form.save()
        #     return data_JSON(request)
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
            return data_JSON(request)
        #     return HttpResponseRedirect("/clinic/new")

    else:
        visit_form = VisitForm()
        context = {'visit_form': visit_form}
        return render(request, 'visit.html', context)


def data_JSON(request):
    #     data = list(Patient.objects.values())
    #     with open("request_body_example.json", "r") as read_file:
    #         data = json.load(read_file)
        # qs = Patient.objects.order_by('patient_id').last()
    _qs = [Visit.objects.order_by('visit_id').last()]
    qs_json = serializers.serialize('json', _qs)
#     with open("data_file.json", "w") as write_file:
#         json.dump(qs_json, write_file)
    url = 'http://127.0.0.1/8001/parse/'
    r = requests.post(url, data=qs_json, verify=False)
    print(r.status_code)
#     return JsonResponse(r.status_code, safe=False)
    return HttpResponse(r, content_type='application/json')
