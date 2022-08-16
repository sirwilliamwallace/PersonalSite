from django.urls import path
from .views import PostDetailView

app_name = 'post'
urlpatterns = [
    path('<int:post_id>/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
]
