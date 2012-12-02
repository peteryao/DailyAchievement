from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from quests.models import *

urlpatterns = patterns('quests.views',
    url(r'^$', 'index'),
    url(r'^reservation/$', 'view_reservation'), 
    url(r'^make_reservation/$', 'make_reservation'),
    url(r'^login/$', 'auth_login'),
    url(r'^contact/$', 'contact'),
    url(r'^settings/$', 'settings'), 
    url(r'^signout/$', 'signout'),
    url(r'^register/$', 'register'),
    url(r'^signin/$', 'test'),
  	)