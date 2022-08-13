from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from contact.models import ContactModel


class ContactUsModelForm(forms.ModelForm):
    attached_file = forms.ImageField(required=False)

    class Meta:
        model = ContactModel
        widgets = {
            'full_name': forms.TextInput(attrs={"type": "text", "class": "form-control", "name": "name", "id": "name",
                                                "placeholder": "Your Name"}),
            'email': forms.EmailInput(
                attrs={"type": "email",
                       "class": "form-control",
                       "name": "email",
                       "id": "email",
                       "placeholder": "Your Email",
                       },
            ),
            'title': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "name": "subject",
                    "id": "subject",
                    "placeholder": "Subject",
                }
            ),
            'message': forms.Textarea(
                attrs={
                    "class": "form-control",
                    "name": "message",
                    "rows": "5",
                    "placeholder": "Message"
                }
            ),
            'attached_file': forms.FileInput(attrs={
                "class": "form-control",
                "name": "file",
                "id": "file",
                "multiple": True,
            })
        }
        labels = {
            "full_name": "Full Name",
            "email": "Email Address",
            "title": "Subject",
            "message": "Your Message",
            "attached_file": "Attached File",
        }
        exclude = ('createDate', 'isRead', 'response',)
