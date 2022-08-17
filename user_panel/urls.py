from django.urls import path
from .views import DashboardView, EditProfileView

app_name = "user_panel"
urlpatterns = [
    path('dashbord', DashboardView.as_view(), name="dashboard"),
    path('edit-info', EditProfileView.as_view(), name="edit-info"),
]
