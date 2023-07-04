from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import Appointment, Doctor
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage, message

from django.conf import settings


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

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"{fname.upper()}, Thank you. We will contact you as soon as possible")
        return HttpResponseRedirect(request.path)
    

class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3


    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        try:
            email.send()
        except Exception as e:
            messages.error(request, f"There was an error sending the email: {str(e)}")

        messages.success(request, f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({   
            "title":"Manage Appointments"
        })
        return context
    
def Add_doctor(request):
    error = ""
    # if not request.user.is_staff:
    #     return redirect('login')
    
    if request.method == "POST":
        i = request.POST.get('image')
        n = request.POST.get('name')
        m = request.POST.get('mobile')
        sp = request.POST.get('special')

        try:
            Doctor.objects.create(image = i, name = n, mobile = m, special = sp)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_doctor.html', d)

def emergency(request):
    # if not request.user.is_staff:
    #     return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request, 'emergency.html', d)

def signout(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('/')

def surgery(request):
    return render(request, 'services/surgery.html')

def dental(request):
    return render(request, 'services/dental.html')

def dermatology(request):
    return render(request, 'services/dermatology.html')

def familyMed(request):
    return render(request, 'services/familyMed.html')

def neurology(request):
    return render(request, 'services/neurology.html')

def psychiatry(request):
    return render(request, 'services/psychiatry.html')

# def emergency(request):
#     return render(request, 'emergency.html')