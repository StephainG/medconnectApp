# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .form import UserRegistrationForm, UserLoginForm, UserUpdateForm


from .decorator import user_not_authenticated
from .tokens import account_activation_token


from django.conf import settings
from django.views.generic.base import TemplateView



# Create your views here.

def home(request):
    return render(request, 'index.html')

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('/')


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')



@user_not_authenticated
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            #user = form.save(commit=False)
            # user.is_active = False
            # user.save()
            # activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request = request,
        template_name= 'authenticate/register.html', 
        context= {'form': form}
    )

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


def profile(request, username):
    if request.method == "POST":
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f"{user_form.username}, Your profile has been updated successfully")
            return redirect("profile", user_form.username)
        

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)

        return render(
            request=request,
            template_name="profile.html",
            context={"form": form}
        )
    
    return redirect("/")


class HomeTemplateView(TemplateView):
    template_name = "index.html"
    
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from doctor family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully!")
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')