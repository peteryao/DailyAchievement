from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from quests.models import *

urlpatterns = patterns('quests.views',
    url(r'^$', 'index'),
    )

urlpatterns += patterns('quests.views',
    url(r'^user/(?P<user_id>\d+)/$', 'profile'),
    url(r'^open/$', 'quest'),
    url(r'^group/(?P<group_id>\d+)/$', 'group'),
    url(r'^group/$', 'add_group'),
    url(r'^leaderboard/$', 'leaderboard'),
    url(r'^quest/(?P<quest_id>\d+)/$', 'quest_page'),
    url(r'^about/$', 'about'),
    # url(r'', ''), 
    )

urlpatterns += patterns('quests.views',
    url(r'^user/auth_login/$', 'auth_login'),
    url(r'^user/logout/$', 'signout'),
    url(r'^user/current/$', 'current_quest'),
    url(r'^user/quest/accept/(?P<quest_id>\d+)/$', 'add_quest'),
    )

urlpatterns += patterns('quests.views', 
    url(r'^group/add_group/$', 'new_group'),
    )