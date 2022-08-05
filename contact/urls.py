from django.urls import path
from . import views

app_name = 'contact-me'
urlpatterns = [
    path('', views.ContactFormView.as_view(), name="contact-form"),
]