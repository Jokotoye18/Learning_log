from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import View, CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth import get_user_model
from .models import Topic, Entry
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils import timezone
from .forms import NewLogForm, NewEntryForm

class LogListView(LoginRequiredMixin, ListView):
    model = Topic
    template_name = 'logs/log_list.html'
    context_object_name = 'topics'
    login_url = 'account_login'
    

    def get_queryset(self):
        queryset = Topic.objects.filter(author=self.request.user).order_by('-id')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['logs_count'] = Topic.objects.filter(author=self.request.user).count()
        return context
    

class LogDetailView(LoginRequiredMixin, DetailView):
    model = Topic
    template_name = 'logs/log_detail.html'
    context_object_name = 'topic'
    login_url = 'account_login' 
    query_pk_and_slug = True
    slug_url_kwarg = 'topic_slug'
    pk_url_kwarg = 'topic_pk'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['entries'] = get_object_or_404(Topic, slug=self.kwargs['topic_slug'], pk=self.kwargs['topic_pk']).entries.order_by('-id')
        return context
        

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class NewLogView(LoginRequiredMixin, CreateView):
    model = Topic
    form_class = NewLogForm
    template_name = 'logs/new_log.html'
    login_url = 'account_login'


    def form_valid(self, form):
        topic = form.save(commit=False)
        topic.author = self.request.user
        topic.save()
        entry = Entry.objects.create(topic=topic, entry= self.request.POST['entry'])
        messages.info(self.request, 'Log created successfully.')
        return redirect(reverse('logs:log_detail', kwargs={'topic_slug': topic.slug, 'topic_pk': topic.pk}))

       
class NewEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = NewEntryForm
    template_name = 'logs/new_entry.html'
    query_pk_and_slug = True
    slug_url_kwarg = 'topic_slug'
    pk_url_kwarg = 'topic_pk'
    login_url = 'account_login'


    def form_valid(self, form):
        topic = get_object_or_404(Topic, slug=self.kwargs['topic_slug'], pk=self.kwargs['topic_pk'])
        entry = form.save(commit=False)
        entry.topic = topic
        entry.save()
        messages.info(self.request, 'Entry created successfully.')
        return redirect(reverse('logs:log_detail', kwargs={'topic_slug': topic.slug, 'topic_pk': topic.pk}))


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['topic'] = get_object_or_404(Topic, slug=self.kwargs.get('topic_slug'), pk=self.kwargs.get('topic_pk'))
        return context


class EditEntryView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model =  Entry
    form_class = NewEntryForm
    template_name = 'logs/edit_entry.html'
    query_pk_and_slug = True
    
    
    def form_valid(self, form):
        topic = get_object_or_404(Entry, slug=self.kwargs['slug'], pk=self.kwargs['pk']).topic
        entry = form.save(commit=False)
        entry.last_updated = timezone.now()
        entry.topic = topic
        entry.save()
        messages.info(self.request, 'Entry updated successfully.')
        return redirect(reverse('logs:log_detail', kwargs={'topic_slug': topic.slug, 'topic_pk': topic.pk}))


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.topic.author != self.request.user:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class DeleteTopicView(LoginRequiredMixin, SuccessMessageMixin,  DeleteView):
    model = Topic
    template_name =  'logs/delete_topic.html'
    success_url = reverse_lazy('logs:log_list')
    query_pk_and_slug = True
    slug_url_kwarg = 'topic_slug'
    pk_url_kwarg = 'topic_pk'

    def get_success_url(self):
        messages.success(self.request, 'Topic deleted successfully.')
        return reverse_lazy('logs:log_list')


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class DeleteEntryView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Entry
    template_name =  'logs/delete_entry.html'
    query_pk_and_slug = True
    slug_url_kwarg = 'entry_slug'
    pk_url_kwarg = 'entry_pk'
    success_message = 'Entry deleted successfully.'

    def get_success_url(self):
        entry_object = get_object_or_404(Entry, slug=self.kwargs['entry_slug'], pk=self.kwargs['entry_pk'])
        topic = entry_object.topic
        messages.success(self.request, 'Entry deleted successfully.')
        return reverse_lazy('logs:log_detail', kwargs={'topic_slug': topic.slug, 'topic_pk': topic.pk})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.topic.author != self.request.user:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


   
