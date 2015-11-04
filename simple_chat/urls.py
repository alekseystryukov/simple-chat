from django.conf.urls import patterns, url
from simple_chat.views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^get_messages/(?P<last_message_id>\d+)/', get_messages, name='get_messages'),
    url(r'^send_message/', send_message, name='send_message')
)
