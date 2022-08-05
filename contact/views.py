from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView
from .forms import ContactUsModelForm


class ContactFormView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactUsModelForm
    success_url = '/#contact'

    def form_valid(self, form):
        form.save()
        return super(ContactFormView, self).form_valid(form)