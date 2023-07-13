from django.urls import path
from . import views
from .views import AppointmentTemplateView, ManageAppointmentTemplateView, Add_doctor


urlpatterns = [
    path('make-an-appointment', AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments", ManageAppointmentTemplateView.as_view(), name="manage"),
    path('emergency', views.emergency, name='emergency'),
    path('surgery', views.surgery, name='surgery'),
    path('dental', views.dental, name='dental'),
    path('dermatology', views.dermatology, name='dermatology'),
    path('familyMed', views.familyMed, name='familyMed'),
    path('neurology', views.neurology, name='neurology'),
    path('psychiatry', views.psychiatry, name='psychiatry'),
    path('security', views.security, name='security'),
    path('billing', views.billing, name='billing'),

    path('add_doctor', Add_doctor, name='add_doctor'),
    path('whatsapp/<int:pk>', views.whatsapp_redirect, name='whatsapp_redirect'),
]
