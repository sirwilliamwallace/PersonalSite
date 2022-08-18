from django.contrib import messages
from django.views.generic.base import TemplateView, View
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, reverse,render
from user_accounts.models import User
from .forms import EditProfileModelForm, ChangePasswordForm
from django.contrib.auth import logout
from tools.send_email_tool import send_email

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

class ChangePasswordView(View):
    
    def get(self, request):
        change_password_form = ChangePasswordForm()
        context = {
            "form":  change_password_form
        }
        return render(request, 'user_panel/change_password.html', context)
    
    def post(self, request):
        change_password_form = ChangePasswordForm(request.POST)
        if change_password_form.is_valid():
            user = User.objects.filter(id=request.user.id).first()
            current_password = change_password_form.cleaned_data.get('current_password')
            password = change_password_form.cleaned_data.get('password')
            confirm_password = change_password_form.cleaned_data.get('confirm_password')
            if user.check_password(current_password):
                user.set_password(password)
                logout(request)
                messages.success(request, 'Your password was successfully updated.')
                send_mail()
                return redirect(reverse('user_panel:change-password'))
            else:
                change_password_form.add_error('password', 'Password is not correct')
        context = {
            "form": edit_profile_form
        }        
        return render(request, 'user_panel/change_password.html', context)

class DashboardViewPartial(TemplateView):
    template_name = "user_panel/components/dashboard_component.html"
