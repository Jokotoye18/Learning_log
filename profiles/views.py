from django.shortcuts import render
from django.views.generic import DetailView, View,UpdateView
from django.contrib.auth import get_user_model
from .models import Profile
from .forms import ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ProfileView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        user = get_user_model().objects.get(username=self.request.user.username)
        context = {"user":user}
        return render(self.request, "profiles/profile.html", context)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profiles/profile_update.html'

    def get_object(self):
        return self.request.user
