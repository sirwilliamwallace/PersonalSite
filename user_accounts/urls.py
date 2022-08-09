from django.urls import path
from .views import RegisterFormView, LoginFormView, LogoutView,ActivateView


app_name = 'account'
urlpatterns = [
    path('register', RegisterFormView.as_view(), name='register'),
    path('login', LoginFormView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('activate-account/<activation_code>', ActivateView.as_view(), name='activation_code'),
]