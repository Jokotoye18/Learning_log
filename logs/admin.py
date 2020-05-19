from django.contrib import admin
from .models import Topic, Entry


class TopicAdmin(admin.ModelAdmin): 
    prepopulated_fields = {"slug": ("topic",)}

admin.site.register(Topic, TopicAdmin)


class EntryAdmin(admin.ModelAdmin): 
    prepopulated_fields = {"slug": ("topic",)}
    
admin.site.register(Entry, EntryAdmin)
