from django import forms
from django.core.exceptions import ValidationError

from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "class": "form-control",
            "name": "password",
            "id": "password",
            "placeholder": "Your Password", })
    )
    confirm_password = forms.PasswordInput(attrs={
        "type": "password",
        "class": "form-control",
        "name": "confirm_password",
        "id": "confirm_password",
        "placeholder": "Confirm Your Password", })

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError('Passwords dont match')