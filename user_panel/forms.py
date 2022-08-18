from django.core import validators
from django import forms
from user_accounts.models import User

extensions = [x.lower() for x in validators.get_available_image_extensions()]


class EditProfileModelForm(forms.ModelForm):
    avatar = forms.ImageField(
        widget=forms.FileInput(),
        validators=[
            validators.FileExtensionValidator(allowed_extensions=extensions)
        ]
    )
    username = forms.CharField(
        label="Username",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control-lg",
                "placeholder": "Username",
            }
        ),
        validators=[
            validators.MaxLengthValidator(50),
            validators.ProhibitNullCharactersValidator]
    )
    first_name = forms.CharField(
        label="First name",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control-lg",
                "placeholder": "First Name",
            }
        ),
        validators=[validators.MaxLengthValidator(100),
                    validators.ProhibitNullCharactersValidator]

    )
    last_name = forms.CharField(
        label="Last name",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control-lg",
                "placeholder": "First Name",
            }
        ),
        validators=[validators.MaxLengthValidator(100),
                    validators.ProhibitNullCharactersValidator]
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'avatar',)


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label="Current password",
        label_suffix="",
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "class": "form-control-lg",
            "placeholder": "Your Current Password", }
        ),
        validators=[
            validators.MinLengthValidator(8),
        ]
    )
    password = forms.CharField(
        label="New Password",
        label_suffix="",
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "class": "form-control-lg",
            "placeholder": "Your New Password", }
        ),
        validators=[
            validators.MinLengthValidator(8),
        ]
    )

    confirm_password = forms.CharField(
        label="Confirm New Password",
        label_suffix="",
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "class": "form-control-lg",
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
        raise ValidationError('Passwords do not match')

