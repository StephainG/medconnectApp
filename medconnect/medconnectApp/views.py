# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail

from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .form import UserRegistrationForm, UserLoginForm


from .decorator import user_not_authenticated


# Create your views here.

def home(request):
    return render(request, 'index.html')

@user_not_authenticated
def register(request):
    # if request.user.is_authenticated():
    #     return redirect('/')
    

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'New account created for {user.username}')
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(request, 'authenticate/register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('/')


@user_not_authenticated
def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect("/")

    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("/")

        else:
            for key, error in list(form.errors.items()):
                if key == "captcha" and error[0] == "This field is required.":
                    messages.error(request, "The recaptcha authentication must be completed")
                    continue

                messages.error(request, error) 

    form = UserLoginForm()


    return render(
        request=request,
        template_name="authenticate/login.html",
        context={"form": form}
        )    