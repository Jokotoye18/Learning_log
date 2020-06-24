from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from.models import Profile
from allauth.account.forms import SignupForm
from django.urls import reverse

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email = 'test@gmail.com',
            username = 'testname'
        )

        self.profile = Profile.objects.create(
            user = self.user,
            location = 'ilorin',
            interest = 'sport',
            about = 'test about'
        )
    
    def test_profile_model_text_representation(self):
        self.assertEqual(f'{self.profile}', f'{self.user.username} profile')

    def test_profile_content(self):
        self.assertEqual(f'{self.profile.user}', f'{self.user}')
        self.assertEqual(f'{self.profile.location}', 'ilorin')
        self.assertEqual(f'{self.profile.interest}', 'sport')
        self.assertEqual(f'{self.profile.about}', 'test about')



class ProfileViewTest():
    c = Client()
    resp = c.get(reverse('profiles:profile'))
    