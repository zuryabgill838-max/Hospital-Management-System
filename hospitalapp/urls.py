from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    # Departments
    path(
        'departments/',
        views.department_list,
        name='department_list'
    ),

    path(
        'departments/add/',
        views.department_add,
        name='department_add'
    ),

    path(
        'departments/edit/<int:id>/',
        views.department_edit,
        name='department_edit'
    ),

    path(
        'departments/delete/<int:id>/',
        views.department_delete,
        name='department_delete'
    ),

    # Doctors
    path(
        'doctors/',
        views.doctor_list,
        name='doctor_list'
    ),

    path(
        'doctors/add/',
        views.doctor_add,
        name='doctor_add'
    ),

    path(
        'doctors/edit/<int:id>/',
        views.doctor_edit,
        name='doctor_edit'
    ),

    path(
        'doctors/delete/<int:id>/',
        views.doctor_delete,
        name='doctor_delete'
    ),
    # Patients
path(
    'patients/',
    views.patient_list,
    name='patient_list'
),

path(
    'patients/add/',
    views.patient_add,
    name='patient_add'
),

path(
    'patients/edit/<int:id>/',
    views.patient_edit,
    name='patient_edit'
),

path(
    'patients/delete/<int:id>/',
    views.patient_delete,
    name='patient_delete'
),

path(
    'patients/<int:id>/profile/',
    views.patient_profile,
    name='patient_profile'
),
# Appointments

path(
    'appointments/',
    views.appointment_list,
    name='appointment_list'
),

path(
    'appointments/add/',
    views.appointment_add,
    name='appointment_add'
),

path(
    'appointments/edit/<int:id>/',
    views.appointment_edit,
    name='appointment_edit'
),

path(
    'appointments/delete/<int:id>/',
    views.appointment_delete,
    name='appointment_delete'
),
path('medicines/', views.medicine_list, name='medicine_list'),
path('medicines/add/', views.medicine_add, name='medicine_add'),
path('medicines/edit/<int:id>/', views.medicine_edit, name='medicine_edit'),
path('medicines/delete/<int:id>/', views.medicine_delete, name='medicine_delete'),
path('prescriptions/', views.prescription_list, name='prescription_list'),
path('prescriptions/add/', views.prescription_add, name='prescription_add'),
path('prescriptions/edit/<int:id>/', views.prescription_edit, name='prescription_edit'),
path('prescriptions/delete/<int:id>/', views.prescription_delete, name='prescription_delete'),
path("register/", views.register_view, name="register"),
path("login/", views.login_view, name="login"),
path("logout/", views.logout_view, name="logout"),
]