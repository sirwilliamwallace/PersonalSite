from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView,CreateView
from .forms import ContactUsModelForm


class ContactFormView(CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactUsModelForm
    success_url = '/#contact'

