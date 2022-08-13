from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import View
from django.utils.crypto import get_random_string
from user_accounts.models import User
from user_accounts.forms import RegisterForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from tools.send_email_tool import send_email


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
                send_email(
                    subject="User activation link",
                    to=new_user.email,
                    context={'user': new_user},
                    template_name='mail_templates/account_activation.html'
                )
                messages.info(self.request,
                              f"An email containing the activation link has been sent to {new_user.email}")
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

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(username__iexact=user_name).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('username', 'User not found')
                else:
                    isPassword = user.check_password(password)
                    if isPassword:
                        login(request, user)
                        messages.success(self.request, f"Logged in as {user.username}")
                        return redirect(reverse('home:index_page'))
                    else:
                        login_form.add_error('username', 'User not found')
            else:
                login_form.add_error('username', 'User not found')

        context = {
            'form': login_form
        }

        return render(request, 'user_accounts/login_form.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(self.request, "Successfully logged out")
        return redirect(reverse('home:index_page'))


class ActivateView(View):
    def get(self, request, activation_code):
        user: User = User.objects.filter(email_verification_code__iexact=activation_code).first()
        print(user)
        if user is not None:
            if not user.is_active:
                user.email_verification_code = get_random_string(72)
                user.is_active = True
                user.save()
                messages.add_message(self.request, messages.SUCCESS, f"{user.username} is activated.")
                return redirect(reverse('account:login'))
            else:
                messages.add_message(self.request, messages.WARNING, f"{user.username} is already active")
                return redirect(reverse('account:login'))

        raise Http404('Activation code is invalid.')


class ForgetPasswordView(View):
    def get(self, request):
        form = ForgetPasswordForm()
        context = {"form": form}
        return render(request, 'user_accounts/forgot_password.html', context)

    def post(self, request):
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            user: User = User.objects.filter(username__iexact=user_name).first()
            if user is not None:
                user_email = user.email
                print(user_email)
                send_email('Password Recovery', user_email, context={'user': user},
                           template_name='mail_templates/forget_password.html')
                messages.info(self.request, "PLease check your email")
        context = {"form": form}
        return render(request, 'user_accounts/forgot_password.html', context)


class ResetPasswordView(View):
    def get(self, request, activation_code):
        user: User = User.objects.filter(email_verification_code__iexact=activation_code).first()
        # print(activation_code)
        if user is None:
            return redirect(reverse('account:login'))
        form = ResetPasswordForm()
        context = {
            "user": user,
            "form": form
        }
        return render(request, 'user_accounts/reset_password.html', context)

    def post(self, request, activation_code):
        form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_verification_code__iexact=activation_code).first()
        if user is None:
            messages.warning(self.request, "User not found")
            return redirect(reverse('account:login'))
        if form.is_valid():
            new_password = form.cleaned_data.get('confirm_password')
            user.set_password(new_password)
            user.email_verification_code = get_random_string(72)
            user.is_active = True
            user.save()
            messages.success(self.request, "Password successfully changed.")
            return redirect(reverse('account:login'))
        context = {"form": form}
        return render(request, 'user_accounts/reset_password.html', context)
