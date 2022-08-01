from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts_list, name='posts'),
    path('<int:post_id>/<slug:slug>', views.post_detail, name='post-detail'),
]

