from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import reverse, redirect

from user_accounts.models import User
from .forms import EditProfileModelForm


class DashboardView(TemplateView):
    template_name = "user_panel/dashboard.html"


class EditProfileView(SuccessMessageMixin, CreateView):
    template_name = 'user_panel/edit_info.html'
    form_class = EditProfileModelForm
    #TODO: complete user panel
    success_url = 'user_panel:edit-info'
    success_message = "Profile updated successfully."

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong. Please try again later.")
        return redirect('user_panel:edit-info')


class DashboardViewPartial(TemplateView):
    template_name = "user_panel/components/dashboard_component.html"
