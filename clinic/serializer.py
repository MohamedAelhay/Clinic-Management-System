from django.core.serializers.json import DjangoJSONEncoder
import json
import os 
from datetime import datetime

class ADTSerializer:
    meta_data = {
        'BROKER_KEY': os.environ.get('BROKER_KEY', ''),
        'TE': "ADT",
        'SCOPE': "A01",
        'DEVICE': "1"
    }

    def __init__(self,params):
        self.patient = params['patient']
        self.visit = params['visit']
        self.attending_doctor = params['attending_doctor']
        self.referring_doctor = params['referring_doctor']


    def serialize(self):
        msg_dict = {

            "META_DATA": self.meta_data,

            "DATA": {

                "PATIENT": {
                    "PATIENT_ID": {
                        "ID_NUMBER": str(self.patient.patient_ssid),
                        "ASSIGNING_AGENCY_OR_DEPARTMENT": "xxxxx"
                    },
                    "PATIENT_NAME": self.nameSerializer(),
                    "PATIENT_IDENTIFIER_LIST": {
                        "ID_NUMBER":str(self.patient.patient_ssid),
                        "ASSIGNING_AGENCY_OR_DEPARTMENT": "xxxxx"
                    },
                    "DATE_TIME_OF_BIRTH": {
                        "TIME": self.patient.patient_birth_date.strftime('%m/%d/%Y'),
                        "DEGREE_OF_PRECISION": "31"
                    },
                    "PATIENT_ADDRESS": self.addressSerializer(),
                    "DRIVER_S_LICENSE_NUMBER_PATIENT": {
                        "LICENSE_NUMBER": "DRIVER_S_LICENSE 1",
                        "EXPIRATION_DATE": "11/11/1999"
                    }
                },

                "VISIT": {
                    "ASSIGNED_PATIENT_LOCATION": self.visitLocationSerialize(),
                    "PREADMIT_NUMBER": {
                        "ID_NUMBER": "123",
                        "CHECK_DIGIT": "123",
                    },
                    "ATTENDING_DOCTOR": self.attendingDoctorSerialize(),
                    "REFERRING_DOCTOR": self.referringDoctorSerialize()
                }
            }
        }
        data_json = json.dumps(msg_dict)
        return data_json


    def nameSerializer(self):
        return {
            "FAMILY_NAME": self.patient.patient_family_name,
            "GIVEN_NAME": self.patient.patient_first_name,
            "SECOND_AND_FURTHER_GIVEN_NAMES_OR_INITIALS_THEREOF": self.patient.patient_second_name
        }
    

    def addressSerializer(self):
        return  {
            "STREET_ADDRESS": self.patient.patient_street,
            "CITY": self.patient.patient_city,
            "ZIP_OR_POSTAL_CODE": str(self.patient.patient_zip_code),
            "COUNTRY": self.patient.patient_country,
        }    


    def visitLocationSerialize(self):
        return {
            "ROOM": str(self.visit.room),
            "BED": str(self.visit.bed),
            "BUILDING": str(self.visit.building),
            "FLOOR": str(self.visit.floor),
        }

    def attendingDoctorSerialize(self):
        return {
            "ID_NUMBER":str(self.attending_doctor.doctor_ssid),
            "FAMILY_NAME":self.attending_doctor.doctor_family_name,
            "GIVEN_NAME":self.attending_doctor.doctor_first_name
        }


    def referringDoctorSerialize(self):
        return {
            "ID_NUMBER":str(self.attending_doctor.doctor_ssid),
            "FAMILY_NAME":self.attending_doctor.doctor_family_name,
            "GIVEN_NAME":self.attending_doctor.doctor_first_name
        } 