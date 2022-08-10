from django.urls import path
from .views import RegisterFormView, LoginFormView, LogoutView,ActivateView, ForgetPasswordView, ResetPasswordView


app_name = 'account'
urlpatterns = [
    path('register', RegisterFormView.as_view(), name='register'),
    path('login', LoginFormView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('activate-account/<activation_code>', ActivateView.as_view(), name='activation_code'),
    path('forgot-password', ForgetPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<activation_code>', ResetPasswordView.as_view(), name='reset-password'),

]