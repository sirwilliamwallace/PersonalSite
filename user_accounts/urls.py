from django.urls import path
from .views import RegisterFormView


app_name = 'account'
urlpatterns = [
    path('register', RegisterFormView.as_view(), name='register'),
    path('login', RegisterFormView.as_view(), name='login'),
]