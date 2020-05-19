from django.urls import path
from .views import ProfileView, ProfileUpdateView

app_name = "profiles"

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile" ),
    path("profile/update/", ProfileUpdateView.as_view(), name="profile_update" )

]