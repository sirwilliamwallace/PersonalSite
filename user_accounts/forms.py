from django import forms
from django.core.exceptions import ValidationError


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
        )
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
            }
        )
    )

    password = forms.CharField(
        label="Password",
        label_suffix="",
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "class": "form-control-lg",
            "id": "password",
            "placeholder": "Your Password", }
        )
    )

    confirm_password = forms.CharField(
        label="Confirm Password",
        label_suffix="",
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "class": "form-control-lg",
            "id": "confirm_password",
            "placeholder": "Confirm Your Password",
        }))

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
        )
    )

    password = forms.CharField(
        label="Password",
        label_suffix="",
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "class": "form-control-lg",
            "id": "password",
            "placeholder": "Your Password", }
        )
    )
