from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from home.models import GetInTouch
from .forms import ContactUsModelForm


class ContactFormView(SuccessMessageMixin, CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactUsModelForm
    success_url = '/#contact'
    success_message = "Your form was successfully uploaded."

    def get_context_data(self, **kwargs):
        base = super(ContactFormView, self).get_context_data()
        get_in_touch: GetInTouch = GetInTouch.objects.filter(isActive=True).first()
        get_in_touch_platforms = get_in_touch.social_media.model
        base['object'] = get_in_touch
        base['social_media'] = get_in_touch_platforms.objects.all()
        return base
