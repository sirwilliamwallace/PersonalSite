from django.core import validators
from django import forms
from user_accounts.models import User

extensions = [x.lower() for x in validators.get_available_image_extensions()]


class EditProfileModelForm(forms.ModelForm):
    avatar = forms.ImageField(
        label="Avatar",
        label_suffix="",
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
            }
        ),
        validators=[
            validators.FileExtensionValidator(allowed_extensions=extensions)
        ]
    )
    """
    <div class="input-group has-validation">
  <span class="input-group-text">@</span>
  <div class="form-floating is-invalid">
    <input type="text" class="form-control is-invalid" id="floatingInputGroup2" placeholder="Username" required>
    <label for="floatingInputGroup2">Username</label>
  </div>
  <div class="invalid-feedback">
    Please choose a username.
  </div>
</div>"""
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
            validators.ProhibitNullCharactersValidator
                    ]
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
                    validators.ProhibitNullCharactersValidator
                    ]

    )
    last_name = forms.CharField(
        label="Last name",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "First Name",
            }
        ),
        validators=[validators.MaxLengthValidator(100),
                    validators.ProhibitNullCharactersValidator
                    ]
    )
    """
    <img src="https://mdbcdn.b-cdn.net/img/new/avatars/1.webp" class="rounded-circle shadow-4"
  style="width: 150px;" alt="Avatar" />
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar',)
