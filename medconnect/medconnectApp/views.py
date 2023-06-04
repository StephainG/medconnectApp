from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.base import TemplateView
from .models import Appointment
from medconnect import settings
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            elif len(username) > 10:
                messages.info(request, 'Username too long')
            else:   
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
                user.save()
                return redirect('signin')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')
        
        # WELCOME EMAIL
        subject = 'Welcome to medConnect'
        message = 'Hello' + user.username + '! \n' + 'Thank you for registering on our website.\n' + 'A confirmation email will be sent to you shortly.\n' + 'Please click the following link to confirm your registration'
        from_email = settings.EMAIL_HOST_USER
        to_email = user.email
        send_mail(subject, message, from_email, to_email, fail_silently=True)

    else:   
        return render(request, 'authenticate/signup.html')
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('signin')
    else:
        return render(request, 'authenticate/signin.html')

def signout(request):
    logout(request)
    # messages.info(request, 'Logged out successfully')
    return redirect('/')


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