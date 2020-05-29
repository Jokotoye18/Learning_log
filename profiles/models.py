from django.db import models
from allauth.account.forms import SignupForm 
from django.contrib.auth import get_user_model
from allauth.account.signals import user_signed_up





class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True)
    interest = models.CharField(max_length=240, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} profile"


User = get_user_model()

def user_signed_up_receiver(request, user, **kwargs):
    if user_signed_up:
        Profile.objects.create(user=user)
user_signed_up.connect(user_signed_up_receiver, sender=User)