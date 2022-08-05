from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm, ContactUsModelForm


def contact_form(request):
    # contactForm = ContactForm(request.POST or None)
    contactForm = ContactUsModelForm(request.POST or None)
    if request.method == "POST":
        if contactForm.is_valid():
            print(contactForm.cleaned_data)
            contactForm.save()
            # contactForm = ContactForm()
            contactForm = ContactUsModelForm()
            return render(request, 'contact/contact.html', {"contact_form": contactForm})
    return render(request, 'contact/contact.html', {"contact_form": contactForm})
