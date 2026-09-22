from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField( max_length= 15, required=True)
    role = forms.ChoiceField(choices=User.Role.choices)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'role', 'password1', 'password2']