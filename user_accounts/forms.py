from django import forms
from django.core.exceptions import ValidationError
from django.core import validators


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Username",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control-lg",
                "id": "username",
                "placeholder": "Your Username",
            }
        ),
        validators=[validators.MaxLengthValidator(50)]
    )
    email = forms.CharField(
        label="Email Address",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control-lg",
                "id": "email",
                "placeholder": "Your Email Address",
            },
        ),
        validators=[
            validators.EmailValidator,
            validators.MaxLengthValidator(100)
        ]
    )

    password = forms.CharField(
        label="Password",
        label_suffix="",
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "class": "form-control-lg",
            "id": "password",
            "placeholder": "Your Password", }
        ),
        validators=[
            validators.MinLengthValidator(8),
        ]
    )

    confirm_password = forms.CharField(
        label="Confirm Password",
        label_suffix="",
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "class": "form-control-lg",
            "id": "confirm_password",
            "placeholder": "Confirm Your Password",
        }
        ),
        validators=[
            validators.MinLengthValidator(8),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError('Passwords dont match')


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control-lg",
                "id": "username",
                "placeholder": "Your Username",
            }
        ),
    )

    password = forms.CharField(
        label="Password",
        label_suffix="",
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "class": "form-control-lg",
            "id": "password",
            "placeholder": "Your Password", }
        ),
    )
