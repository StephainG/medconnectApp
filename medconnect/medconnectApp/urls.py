from django.urls import path
from . import views
from .views import AppointmentTemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('signin', views.signin, name='signin'),
    path('make-an-appointment', AppointmentTemplateView.as_view(), name="appointment"),
]
