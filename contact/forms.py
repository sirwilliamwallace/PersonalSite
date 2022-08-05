from django import forms
from contact.models import ContactModel

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ('createDate', 'isRead', 'response',)
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
            )
        }
        labels = {
            "full_name": "Full Name",
            "email": "Email Address",
            "title": "Subject",
            "message": "Your Message",
        }


