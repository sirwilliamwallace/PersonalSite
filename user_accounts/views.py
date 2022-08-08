from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import View
from django.utils.crypto import get_random_string
from user_accounts.models import User
from user_accounts.forms import RegisterForm, LoginForm


class RegisterFormView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'form': register_form
        }
        return render(request, 'user_accounts/register_form.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            print(register_form.cleaned_data)

            user_name = register_form.cleaned_data.get('username')
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            exist_email_user: bool = User.objects.filter(email__iexact=user_email).exists()
            exist_username_user: bool = User.objects.filter(username__iexact=user_name).exists()
            if exist_email_user:
                register_form.add_error('email', f'{user_email} is already taken.')
            elif exist_username_user:
                register_form.add_error('username', f'{user_name} is already taken.')
            else:
                new_user = User(username=user_name, email=user_email, email_verification_code=get_random_string(72),
                                is_active=False)
                new_user.set_password(user_password)
                new_user.save()
                # TODO: Send activation code

                return redirect(reverse('account:login'))
        context = {
            "form": register_form
        }
        return render(request, 'user_accounts/register_form.html', context)


class LoginFormView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'form': login_form
        }
        return render(request, 'user_accounts/login_form.html', context)

    def post(self, request):
        pass
