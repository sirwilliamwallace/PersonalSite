from django.contrib import messages
from django.views.generic.base import TemplateView, View
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from user_accounts.models import User
from .forms import EditProfileModelForm


class DashboardView(TemplateView):
    template_name = "user_panel/dashboard.html"


class EditProfileView(SuccessMessageMixin, View):
    def get(self, request):
        this_user_id = request.user.id
        retrieved_user = User.objects.filter(id=this_user_id).first()
        edit_profile_form = EditProfileModelForm(instance=retrieved_user)
        context = {
            "form": edit_profile_form,
            "user": retrieved_user
        }
        return render(request, 'user_panel/edit_info.html', context)

    def post(self, request):
        this_user_id = request.user.id
        retrieved_user = User.objects.filter(id=this_user_id).first()
        edit_profile_form = EditProfileModelForm(request.POST, request.FILES, instance=retrieved_user)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            messages.success(request, 'Your profile was successfully updated.')
            return redirect(f"{self.request.path}#dashboardPartial")
        context = {
            "form": edit_profile_form,
            "user": retrieved_user
        }
        return render(request, 'user_panel/edit_info.html', context)


class DashboardViewPartial(TemplateView):
    template_name = "user_panel/components/dashboard_component.html"
