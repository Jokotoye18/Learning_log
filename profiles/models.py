from django.db import models
from allauth.account.forms import SignupForm 
from django.contrib.auth import get_user_model
from allauth.account.signals import user_signed_up, user_logged_out, user_logged_in
from imagekit.models import	ImageSpecField	
from pilkit.processors import ResizeToFill




class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics", default="index.jpg")
    location = models.CharField(max_length=50, blank=True)
    interest = models.CharField(max_length=240, blank=True)
    about = models.TextField(blank=True)
    image_thumbnail	=ImageSpecField(source='image', processors=[ResizeToFill(300,300)], format='JPEG', options={'quality':	80})

    def __str__(self):
        return f"{self.user.username} profile"





User = get_user_model()

def user_logged_out_receiver(request, user, **kwargs):
    print(f'{user} just logged out!')
    print(user)
user_logged_out.connect(user_logged_out_receiver, sender=User)

def user_signed_up_receiver(request, user, **kwargs):
    if user_signed_up:
        Profile.objects.create(user=user)
user_signed_up.connect(user_signed_up_receiver, sender=User)