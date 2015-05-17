# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url,include
from .views import ListEventView, CreateEventView

urlpatterns = patterns('',
	url(r'^events/$', ListEventView.as_view(), name = 'event_list',),
	url(r'^create/event/$', CreateEventView.as_view(), name = 'create_event',),
)