from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .forms import ContactUsModelForm


class ContactFormView(View):
    def get(self, request):
        contactForm = ContactUsModelForm()
        return render(request, 'contact/contact.html', {"contact_form": contactForm})

    def post(self, request):
        contactForm = ContactUsModelForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
            contactForm = ContactUsModelForm()
            return redirect('home:contact-form-view')


