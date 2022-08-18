from django.urls import path
from .views import DashboardView, EditProfileView, ChangePasswordView

app_name = "user_panel"
urlpatterns = [
    path('dashbord', DashboardView.as_view(), name="dashboard"),
    path('change-password', ChangePasswordView.as_view(), name="change-password"),
    path('edit-info', EditProfileView.as_view(), name="edit-info"),
]
