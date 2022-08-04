from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('<int:post_id>/<slug:slug>', views.post_detail, name='post-detail'),
]
