from django.urls import path
from logs.views import   LogListView, LogDetailView, NewLogView,NewEntryView,EditEntryView, DeleteTopicView, DeleteEntryView

app_name = 'logs'

urlpatterns = [
    path('logs/', LogListView.as_view(), name='log_list'),
    path('logs/<slug:topic_slug>-<int:topic_pk>/',LogDetailView.as_view(), name='log_detail' ),
    path('logs/new/', NewLogView.as_view(), name='new_log'),
    path('logs/<slug:topic_slug>-<int:topic_pk>/new/', NewEntryView.as_view(), name='new_entry'),
    path('logs/<slug:slug>-<int:pk>/update/', EditEntryView.as_view(), name='edit_entry'),
    path('logs/<slug:slug>-<int:pk>/entry/delete/', DeleteEntryView.as_view(), name='delete_entry'),
    path('log/<slug:topic_slug>-<int:topic_pk>/topic/delete/', DeleteTopicView.as_view(), name='delete_topic'),
]
