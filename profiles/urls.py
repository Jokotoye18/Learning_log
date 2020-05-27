from django.urls import path
from .views import  ProfileUpdateView

app_name = "profiles"

urlpatterns = [
    path("profile/update/", ProfileUpdateView.as_view(), name="profile_update" )
]