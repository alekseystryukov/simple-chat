from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^chat/', include('simple_chat.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', 'simple_chat.views.index', name='index'),

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
