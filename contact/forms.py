from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label_suffix="",
        label="Name",
        max_length=50,
        error_messages={
            "required": "Please fill the form"
        },
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "name": "name",
            "id": "name",
            "placeholder": "Your Name",
        })
    )
    email = forms.EmailField(
        label_suffix="",
        label="Email Address",
        widget=forms.EmailInput(attrs={
            "type": "email",
            "class": "form-control",
            "name": "email",
            "id": "email",
            "placeholder": "Your Email",
        })
    )
    subject = forms.CharField(
        label_suffix="",
        label="Subject",
        max_length=150,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "name": "subject",
            "id": "subject",
            "placeholder": "Subject",
        })
    )
    message = forms.CharField(
        label_suffix="",
        label="Message",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "name": "message",
                "rows": "5",
                "placeholder": "Message"
            }
        ),
    )
