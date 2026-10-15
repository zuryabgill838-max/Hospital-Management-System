from django import forms
from .models import (
    Department,
    Doctor,
    Patient,
    PatientProfile,
    Appointment,
    Medicine,
    Prescription
    )

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-cyan-500',
                'placeholder': 'Enter department name'
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-cyan-500',
                'placeholder': 'Enter department description',
                'rows': 4
            }),
        }


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = [
            'name',
            'specialization',
            'phone',
            'department'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'placeholder': 'Enter doctor name'
            }),

            'specialization': forms.TextInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'placeholder': 'e.g. Cardiologist'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'placeholder': '03XXXXXXXXX'
            }),

            'department': forms.Select(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3'
            }),
        }
class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'phone']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'placeholder': 'Enter patient name'
            }),

            'age': forms.NumberInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'placeholder': 'Enter age'
            }),

            'gender': forms.TextInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'placeholder': 'Enter gender'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'placeholder': '03XXXXXXXXX'
            }),
        }


class PatientProfileForm(forms.ModelForm):

    class Meta:
        model = PatientProfile
        fields = [
            'address',
            'blood_group',
            'emergency_contact',
        ]

        widgets = {
            'address': forms.Textarea(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'placeholder': 'Enter patient address',
                'rows': 3
            }),

            'blood_group': forms.TextInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'placeholder': 'e.g. B+'
            }),

            'emergency_contact': forms.TextInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'placeholder': 'Emergency contact number'
            }),
        }
class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            'doctor',
            'patient',
            'appointment_date',
            'appointment_time',
            'reason',
        ]

        widgets = {

            'doctor': forms.Select(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3'
            }),

            'patient': forms.Select(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3'
            }),

            'appointment_date': forms.DateInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'type': 'date'
            }),

            'appointment_time': forms.TimeInput(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'type': 'time'
            }),

            'reason': forms.Textarea(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'placeholder': 'Enter reason for appointment',
                'rows': 4
            }),
        }
class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'manufacturer', 'price']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border rounded p-2'
            }),
            'manufacturer': forms.TextInput(attrs={
                'class': 'w-full border rounded p-2'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full border rounded p-2',
                'step': '0.01'
            }),
        }
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['doctor', 'patient', 'medicines', 'instructions']

        widgets = {
            'doctor': forms.Select(attrs={
                'class': 'w-full border rounded-lg p-2'
            }),

            'patient': forms.Select(attrs={
                'class': 'w-full border rounded-lg p-2'
            }),

            'medicines': forms.SelectMultiple(attrs={
                'class': 'w-full border rounded-lg p-2',
                'size': '6'
            }),

            'instructions': forms.Textarea(attrs={
                'class': 'w-full border rounded-lg p-2',
                'rows': 4,
                'placeholder': 'Enter instructions...'
            }),
        }