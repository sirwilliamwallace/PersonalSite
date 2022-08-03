from django.urls import path
from . import views

app_name='home'
urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('contact-us', views.contact_page, name='contact_page')
]

