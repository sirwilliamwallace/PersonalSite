from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from user_accounts.forms import RegisterForm


class RegisterFormView(CreateView):
    template_name = 'user_accounts/register_form.html'
    form_class = RegisterForm
    success_url = 'home:index_page'
