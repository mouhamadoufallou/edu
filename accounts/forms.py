from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    is_admin = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    is_student = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    is_teacher = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_student', 'is_teacher')
        
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )