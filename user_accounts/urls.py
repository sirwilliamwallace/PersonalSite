from django.urls import path
from .views import RegisterFormView, LoginFormView


app_name = 'account'
urlpatterns = [
    path('register', RegisterFormView.as_view(), name='register'),
    path('login', LoginFormView.as_view(), name='login'),
]