from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View,UpdateView
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Profile
from .forms import ProfileUpdateForm, UserForm
from django.contrib.auth.mixins import LoginRequiredMixin



class ProfileUpdateView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        form1 = UserForm(instance=request.user)
        form2 = ProfileUpdateForm(instance=request.user.profile)
        context = {'form1':form1, 'form2':form2}
        return render(request, 'profiles/profile.html', context)

    def post(self, request, *args, **kwargs):
        form1 = UserForm(request.POST, instance=request.user)
        form2 = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(self.request, 'Your account has been updated successfully.')
        return redirect("pages:home")




        


