from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

class Topic(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='topics',on_delete=models.CASCADE)
    topic = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(blank=True, max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['author']


    def __str__(self):
        return self.topic


    def get_absolute_url(self):
        return reverse('logs:log_topic_entries', kwargs={
            'topic_slug': self.slug,
            'topic_pk': self.pk
        } )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic)
        return super().save(*args, **kwargs)


class Entry(models.Model):
    topic = models.ForeignKey(Topic, related_name='entries', on_delete=models.CASCADE)
    entry = models.TextField()
    slug = models.SlugField(blank=True, max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.entry
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic)
        return super().save(*args, **kwargs)



