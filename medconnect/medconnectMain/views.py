from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import Appointment
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        messages.add_message(request, messages.SUCCESS, f"{fname.upper()}, Thank you. We will contact you as soon as possible")
        return HttpResponseRedirect(request.path)
    

def signout(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('/')