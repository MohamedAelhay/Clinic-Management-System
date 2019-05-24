from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_ssid = models.IntegerField()
    patient_first_name = models.CharField(max_length = 200)
    patient_second_name = models.CharField(max_length = 200)
    patient_family_name = models.CharField(max_length = 200)
    patient_birth_date = models.DateTimeField()
    patient_street = models.CharField(max_length = 200)
    patient_city = models.CharField(max_length = 200)
    patient_country = models.CharField(max_length = 200)
    patient_zip_code = models.IntegerField()

    def __str__(self):
        return self.patient_first_name
        
class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_ssid = models.IntegerField()
    doctor_first_name = models.CharField(max_length = 200)
    doctor_family_name = models.CharField(max_length = 200)
    doctor_degree = models.CharField(max_length = 200)
	
    def __str__(self):
        return self.doctor_first_name


class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    visit_date = models.DateTimeField()
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
