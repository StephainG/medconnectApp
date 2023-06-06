from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import get_user_model


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Please enter your email address')
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user