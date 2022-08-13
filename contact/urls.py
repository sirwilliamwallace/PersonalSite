from django.urls import path
from .views import ContactFormView

app_name = 'contact-me'
urlpatterns = [
    path('#contact', ContactFormView.as_view(), name="contact-form"),
]