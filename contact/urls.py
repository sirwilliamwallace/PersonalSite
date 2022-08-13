from django.urls import path, re_path
from .views import ContactFormView

app_name = 'contact-me'
urlpatterns = [
    path('contact-form', ContactFormView.as_view(), name="contact-form"),
]
