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
