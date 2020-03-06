from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(appointments)
admin.site.register(receptionist)
admin.site.register(DaySchedule)
admin.site.register(doctors)
admin.site.register(patient)
admin.site.register(labReports)
