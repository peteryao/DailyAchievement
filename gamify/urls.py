from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from gamify.models import *

urlpatterns = patterns('gamify.views',
    url(r'^$', 'index'),
    )

urlpatterns += patterns('gamify.views',
    url(r'^user/(?P<user_id>\d+)/$', 'profile'),
    url(r'^open/$', 'quest'),
    url(r'^group/(?P<group_id>\d+)/$', 'group'),
    url(r'^group/$', 'add_group'),
    url(r'^leaderboard/$', 'leaderboard'),
    url(r'^quest/(?P<quest_id>\d+)/$', 'quest_page'),
    url(r'^about/$', 'about'),
    # url(r'', ''), 
    )

urlpatterns += patterns('gamify.views',
    url(r'^user/auth_login/$', 'auth_login'),
    url(r'^user/logout/$', 'signout'),
    url(r'^user/current/$', 'current_quest'),
    url(r'^user/quest/accept/(?P<quest_id>\d+)/$', 'add_quest'),
    url(r'^user/quest/finish/(?P<quest_id>\d+)/$', 'finish_quest'),
    url(r'^user/quest/cancel/(?P<quest_id>\d+)/$', 'cancel_quest'),
    url(r'^user/group/join/(?P<group_id>\d+)/$', 'join_group'),

    )

urlpatterns += patterns('gamify.views', 
    url(r'^group/add_group/$', 'new_group'),
    )