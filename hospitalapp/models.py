from django.db import models
from django.contrib.auth.models import User


# 1. Department
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# 2. Doctor
# Department → Doctors = One-to-Many
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='doctors'
    )

    def __str__(self):
        return self.name


# 3. Patient
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# 4. Patient Profile
# Patient → PatientProfile = One-to-One
class PatientProfile(models.Model):
    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    address = models.TextField()
    blood_group = models.CharField(max_length=5)
    emergency_contact = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.patient.name} Profile"


# 5. Appointment
# Department → Appointments = One-to-Many
# Doctor → Appointments = One-to-Many
# Patient → Appointments = One-to-Many
class Appointment(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"


# 6. Medicine
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# 7. Prescription
# Doctor → Prescriptions = One-to-Many
# Patient → Prescriptions = One-to-Many
class Prescription(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )
    medicines = models.ManyToManyField(
        Medicine,
        related_name='prescriptions'
    )
    date = models.DateField(auto_now_add=True)
    instructions = models.TextField()

    def __str__(self):
        return f"Prescription - {self.patient.name}"
# Staff/User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='staff_profile'
    )

    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"