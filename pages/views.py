from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from logs.models import Topic
from .forms import ContactForm


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'home.html', context)

class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'form':form}
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']

            subject = 'Contact form received'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [settings.DEFAULT_FROM_EMAIL]
            contact_message = f'Hi Jokotoye Ademola, a contact form has been received from "{name}". There mesaage is "{message}".You can reply to "{email}".'

            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
            form.save()
            messages.info(request, 'Contact message received.')
        return redirect('pages:home')
