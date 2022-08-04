from django.urls import path
from . import views

app_name = 'contact-me'
urlpatterns = [
    path('', views.contact_form, name="contact-form"),
]