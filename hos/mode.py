from django.db import models

# Create your models here.

'''class admins(models.Model):
    admin_id = models.IntegerField(max_length=100 ,primary_key=True)
    #admin_id=models.ForeignKey('admin_id')
    name = models.CharField(max_length=100,)
    password = models.CharField(max_length=100,)
    created_at = models.TimeField(max_length=100,)
    updated_at = models.TimeField(max_length=100,)'''

class appointments(models.Model):
    patient_appointment_id =models.CharField(max_length=100,primary_key=True)
    patient_email = models.EmailField()
    #appointment=models.ForeignKey('appointment_id')
    patient_phone = models.IntegerField()
    patient_name = models.CharField(max_length=100,)
    patient_age = models.IntegerField()
    patient_gender = models.CharField(max_length=100,)
    doctor_id = models.CharField(max_length=100,)
    slot_date = models.DateField(max_length=100,)
    slot_time = models.TimeField(max_length=100,)
    created_at = models.DateField(max_length=100,)
    udated_at = models.DateField(max_length=100,)

'''class departments(models.Model):
    department_id = models.CharField(max_length=100,primary_key=True)
    #department_id = models.ForeignKey('department_id')
    department_name = models.CharField(max_length=100,) 
    created_at = models.DateField(max_length=100 , )
    updated_at = models.DateField(max_length=100,)'''


class doctors(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    #phone_no = models.IntegerField(max_length=1000)



class receptionist(models.Model):
    recep_name = models.CharField(max_length=100)
    recep_id = models.EmailField(max_length=50 , primary_key=True)
    hospital_name = models.CharField(max_length=100)
    hospital_id = models.CharField(max_length=100   )





from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(appointments)
admin.site.register(receptionist)
#admin.site.register(departments)
#admin.site.register(patients)
admin.site.register(doctors)
'''admin.site.register(slots)
admin.site.register(users)
admin.site.register(password_reset)
admin.site.register(moderator)
admin.site.register(migration)'''



