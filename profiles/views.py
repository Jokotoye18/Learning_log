from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View,UpdateView
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Profile
from .forms import ProfileUpdateForm, UserForm, ProfileImageForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProfileUpdateView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        form1 = UserForm(instance=request.user)
        form2 = ProfileUpdateForm(instance=request.user.profile)
        form3 = ProfileImageForm(instance=request.user.profile)
        context = {'form1':form1, 'form2':form2, 'form3':form3}
        return render(request, 'profiles/profile_update.html', context)

    def post(self, request, *args, **kwargs):
        form1 = UserForm(request.POST, instance=request.user)
        form2 = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        form3 = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        if form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
            messages.success(self.request, 'Your account has been updated successfully.')
        return redirect("profiles:profile_update")


        


