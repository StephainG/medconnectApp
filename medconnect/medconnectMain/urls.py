from django.urls import path
from . import views
from .views import AppointmentTemplateView, ManageAppointmentTemplateView


urlpatterns = [
    path('signout', views.signout, name='signout'),
    # path('signin', views.signin, name='signin'),
    path('make-an-appointment', AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments", ManageAppointmentTemplateView.as_view(), name="manage"),
]
