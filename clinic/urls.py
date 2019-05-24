from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^new', views.new_patient),
    url(r'^visit', views.new_visit),

]
