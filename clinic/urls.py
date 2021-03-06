from django.conf.urls import url

from . import views


urlpatterns = [
    url('patient', views.new_patient, name = 'new-patient'),
    url('visit', views.new_visit, name = 'new-visit'),
    url('orm', views.new_orm, name = 'new-orm'),
    url('', views.index, name= 'clinic'),
]
