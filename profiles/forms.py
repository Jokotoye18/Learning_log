from django import forms
from .models import Profile
from django.contrib.auth import get_user_model


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'location', 'interest', 'about']
        


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']



class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email']
        