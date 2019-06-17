from django.conf.urls import url

from . import views


urlpatterns = [
    url('patient', views.new_patient, name = 'new-patient'),
    url('visit', views.new_visit, name = 'new-visit'),
    url('', views.index, name= 'clinic'),
]
