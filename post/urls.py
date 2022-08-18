from django.urls import path
from .views import PostDetailView, SearchPostsView

app_name = 'post'
urlpatterns = [
    path('<int:post_id>/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
    path('', SearchPostsView.as_view(), name='search'),
]
