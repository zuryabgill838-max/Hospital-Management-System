from django.contrib import admin

from .models import (
    Department,
    Doctor,
    Patient,
    PatientProfile,
    Appointment,
    Medicine,
    Prescription,
)


admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(PatientProfile)
admin.site.register(Appointment)
admin.site.register(Medicine)
admin.site.register(Prescription)