from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

from .models import (
    Department,
    Doctor,
    Patient,
    PatientProfile,
    Appointment,
    Medicine,
    Prescription,
)

from .forms import (
    DepartmentForm,
    DoctorForm,
    PatientForm,
    PatientProfileForm,
    AppointmentForm,
    MedicineForm,
    PrescriptionForm,
)
@login_required
def dashboard(request):
    return render(request, 'hospitalapp/dashboard.html')


# Department List
@permission_required('hospitalapp.view_department', raise_exception=True)
def department_list(request):
    departments = Department.objects.all()

    return render(
        request,
        'hospitalapp/departments.html',
        {'departments': departments}
    )


# Add Department
@permission_required('hospitalapp.add_department', raise_exception=True)
def department_add(request):

    if request.method == 'POST':
        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('department_list')

    else:
        form = DepartmentForm()

    return render(
        request,
        'hospitalapp/department_form.html',
        {
            'form': form,
            'title': 'Add Department'
        }
    )


# Edit Department
@permission_required('hospitalapp.change_department', raise_exception=True)
def department_edit(request, id):

    department = get_object_or_404(Department, id=id)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)

        if form.is_valid():
            form.save()
            return redirect('department_list')

    else:
        form = DepartmentForm(instance=department)

    return render(
        request,
        'hospitalapp/department_form.html',
        {
            'form': form,
            'title': 'Edit Department'
        }
    )


# Delete Department
@permission_required('hospitalapp.delete_department', raise_exception=True)
def department_delete(request, id):

    department = get_object_or_404(Department, id=id)

    if request.method == 'POST':
        department.delete()
        return redirect('department_list')

    return render(
        request,
        'hospitalapp/department_confirm_delete.html',
        {'department': department}
    )
# Doctor List
@permission_required('hospitalapp.view_doctor', raise_exception=True)
def doctor_list(request):

    doctors = Doctor.objects.select_related('department').all()

    return render(
        request,
        'hospitalapp/doctors.html',
        {'doctors': doctors}
    )


# Add Doctor
@permission_required('hospitalapp.add_doctor', raise_exception=True)
def doctor_add(request):

    if request.method == 'POST':

        form = DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('doctor_list')

    else:
        form = DoctorForm()

    return render(
        request,
        'hospitalapp/doctor_form.html',
        {
            'form': form,
            'title': 'Add Doctor'
        }
    )


# Edit Doctor
@permission_required('hospitalapp.change_doctor', raise_exception=True)
def doctor_edit(request, id):

    doctor = get_object_or_404(Doctor, id=id)

    if request.method == 'POST':

        form = DoctorForm(
            request.POST,
            instance=doctor
        )

        if form.is_valid():
            form.save()
            return redirect('doctor_list')

    else:

        form = DoctorForm(instance=doctor)

    return render(
        request,
        'hospitalapp/doctor_form.html',
        {
            'form': form,
            'title': 'Edit Doctor'
        }
    )


# Delete Doctor
@permission_required('hospitalapp.delete_doctor', raise_exception=True)
def doctor_delete(request, id):

    doctor = get_object_or_404(Doctor, id=id)

    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')

    return render(
        request,
        'hospitalapp/doctor_confirm_delete.html',
        {'doctor': doctor}
    )
# Patient List
@permission_required('hospitalapp.view_patient', raise_exception=True)
def patient_list(request):
    patients = Patient.objects.all().order_by('-id')

    return render(
        request,
        'hospitalapp/patients.html',
        {'patients': patients}
    )


# Add Patient
@permission_required('hospitalapp.add_patient', raise_exception=True)
def patient_add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(
        request,
        'hospitalapp/patient_form.html',
        {
            'form': form,
            'title': 'Add Patient'
        }
    )


# Edit Patient
@permission_required('hospitalapp.change_patient', raise_exception=True)
def patient_edit(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)

    return render(
        request,
        'hospitalapp/patient_form.html',
        {
            'form': form,
            'title': 'Edit Patient'
        }
    )


# Delete Patient
@permission_required('hospitalapp.delete_patient', raise_exception=True)
def patient_delete(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')

    return render(
        request,
        'hospitalapp/patient_confirm_delete.html',
        {'patient': patient}
    )


# Add or Edit Patient Profile
@login_required
def patient_profile(request, id):
    patient = get_object_or_404(Patient, id=id)

    profile = PatientProfile.objects.filter(
        patient=patient
    ).first()
    required_permission = (
        'hospitalapp.change_patientprofile' if profile
        else 'hospitalapp.add_patientprofile'
    )
    if not request.user.has_perm(required_permission):
        raise PermissionDenied

    if request.method == 'POST':
        form = PatientProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():
            saved_profile = form.save(commit=False)
            saved_profile.patient = patient
            saved_profile.save()

            return redirect('patient_list')

    else:
        form = PatientProfileForm(instance=profile)

    title = 'Edit Patient Profile' if profile else 'Add Patient Profile'

    return render(
        request,
        'hospitalapp/patient_profile_form.html',
        {
            'form': form,
            'patient': patient,
            'title': title,
        }
    )
# Appointment List
@permission_required('hospitalapp.view_appointment', raise_exception=True)
def appointment_list(request):

    appointments = Appointment.objects.select_related(
        'doctor',
        'patient'
    ).all().order_by('-appointment_date')

    return render(
        request,
        'hospitalapp/appointments.html',
        {'appointments': appointments}
    )


# Add Appointment
@permission_required('hospitalapp.add_appointment', raise_exception=True)
def appointment_add(request):

    if request.method == 'POST':

        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('appointment_list')

    else:
        form = AppointmentForm()

    return render(
        request,
        'hospitalapp/appointment_form.html',
        {
            'form': form,
            'title': 'Add Appointment'
        }
    )


# Edit Appointment
@permission_required('hospitalapp.change_appointment', raise_exception=True)
def appointment_edit(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    if request.method == 'POST':

        form = AppointmentForm(
            request.POST,
            instance=appointment
        )

        if form.is_valid():
            form.save()
            return redirect('appointment_list')

    else:

        form = AppointmentForm(
            instance=appointment
        )

    return render(
        request,
        'hospitalapp/appointment_form.html',
        {
            'form': form,
            'title': 'Edit Appointment'
        }
    )


# Delete Appointment
@permission_required('hospitalapp.delete_appointment', raise_exception=True)
def appointment_delete(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')

    return render(
        request,
        'hospitalapp/appointment_confirm_delete.html',
        {
            'appointment': appointment
        }
    )
@permission_required('hospitalapp.view_medicine', raise_exception=True)
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(
        request,
        'hospitalapp/medicines.html',
        {'medicines': medicines}
    )


@permission_required('hospitalapp.add_medicine', raise_exception=True)
def medicine_add(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()

    return render(
        request,
        'hospitalapp/medicine_form.html',
        {
            'form': form,
            'title': 'Add Medicine'
        }
    )


@permission_required('hospitalapp.change_medicine', raise_exception=True)
def medicine_edit(request, id):
    medicine = get_object_or_404(Medicine, id=id)

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)

        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=medicine)

    return render(
        request,
        'hospitalapp/medicine_form.html',
        {
            'form': form,
            'title': 'Edit Medicine'
        }
    )


@permission_required('hospitalapp.delete_medicine', raise_exception=True)
def medicine_delete(request, id):
    medicine = get_object_or_404(Medicine, id=id)

    if request.method == 'POST':
        medicine.delete()
        return redirect('medicine_list')

    return render(
        request,
        'hospitalapp/medicine_confirm_delete.html',
        {'medicine': medicine}
    )
@permission_required('hospitalapp.view_prescription', raise_exception=True)
def prescription_list(request):
    prescriptions = Prescription.objects.all()

    return render(
        request,
        'hospitalapp/prescriptions.html',
        {'prescriptions': prescriptions}
    )


@permission_required('hospitalapp.add_prescription', raise_exception=True)
def prescription_add(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()

    return render(
        request,
        'hospitalapp/prescription_form.html',
        {
            'form': form,
            'title': 'Add Prescription'
        }
    )


@permission_required('hospitalapp.change_prescription', raise_exception=True)
def prescription_edit(request, id):
    prescription = get_object_or_404(Prescription, id=id)

    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)

        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm(instance=prescription)

    return render(
        request,
        'hospitalapp/prescription_form.html',
        {
            'form': form,
            'title': 'Edit Prescription'
        }
    )


@permission_required('hospitalapp.delete_prescription', raise_exception=True)
def prescription_delete(request, id):
    prescription = get_object_or_404(Prescription, id=id)

    if request.method == 'POST':
        prescription.delete()
        return redirect('prescription_list')

    return render(
        request,
        'hospitalapp/prescription_confirm_delete.html',
        {'prescription': prescription}
    )
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(
        request,
        "hospitalapp/register.html",
        {"form": form}
    )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
    else:
        form = AuthenticationForm(request)

    return render(
        request,
        "hospitalapp/login.html",
        {"form": form}
    )


def logout_view(request):
    logout(request)
    return redirect("login")
