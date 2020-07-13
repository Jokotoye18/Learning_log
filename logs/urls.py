from django.urls import path
from logs.views import  LogTopicListView, LogTopicEntriesView, NewLogTopicView, NewLogTopicEntryView, EditEntryView, DeleteTopicView, DeleteEntryView 

app_name = 'logs'

urlpatterns = [
    path('logs/', LogTopicListView.as_view(), name='log_topic_list'),
    path('logs/<slug:topic_slug>-<int:topic_pk>/', LogTopicEntriesView.as_view(), name='log_topic_entries' ),
    path('logs/new/', NewLogTopicView.as_view(), name='new_log'),
    path('logs/<slug:topic_slug>-<int:topic_pk>/new/', NewLogTopicEntryView.as_view(), name='new_entry'),
    path('logs/<slug:topic_slug>/<slug:slug>-<int:pk>/update/', EditEntryView.as_view(), name='edit_entry'),
    path('logs/<slug:topic_slug>/<slug:entry_slug>-<int:entry_pk>/entry/delete/', DeleteEntryView.as_view(), name='delete_entry'),
    path('log/<slug:topic_slug>-<int:topic_pk>/topic/delete/', DeleteTopicView.as_view(), name='delete_topic'),
]
