from quests.models import Quest, CompleteQuest, Interest, UserInterests, UserAdditions, Rank
from django.contrib import admin
from django.contrib.admin.models import LogEntry


class QuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'point_value', 'image')


class CompleteQuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quest', 'completed')


class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserInterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'interest')


class UserAdditionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'exp', 'occupation', 'avatar', 'location')


class RankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'experience_required')

admin.site.register(LogEntry)
admin.site.register(Quest, QuestAdmin)
admin.site.register(CompleteQuest, CompleteQuestAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(UserInterests, UserInterestAdmin)
admin.site.register(UserAdditions, UserAdditionsAdmin)
admin.site.register(Rank, RankAdmin)
