from django.contrib import messages
from django.core import validators
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from home.models import GetInTouch
from .forms import ContactUsModelForm


class ContactFormView(SuccessMessageMixin, CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactUsModelForm
    success_url = '/#contact'
    success_message = "Your form was successfully uploaded."

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid data received, Please fill the form carefully')
        return redirect(reverse('home:index_page') + '#contact')

    def get_context_data(self, **kwargs):
        base = super(ContactFormView, self).get_context_data()
        get_in_touch: GetInTouch = GetInTouch.objects.filter(isActive=True).first()
        get_in_touch_platforms = get_in_touch.social_media.model
        base['object'] = get_in_touch
        base['social_media'] = get_in_touch_platforms.objects.all()
        return base
