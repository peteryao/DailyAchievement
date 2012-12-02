from quests.models import Quest, CompleteQuest, Interest, UserInterests, UserAdditions, Rank, Flair, Achievement, Trophy, UserAchievement, UserTrophy, ActiveQuest, Competition, Group, UserGroup
from django.contrib import admin
from django.contrib.admin.models import LogEntry


class QuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'point_value', 'image')


class CompleteQuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quest', 'image', 'completed')


class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserInterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'interest')


class UserAdditionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'exp', 'points', 'occupation', 'avatar', 'location', 'flair')


class RankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'experience_required')


class FlairAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'requirements')


class TrophyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'achievement')


class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'achievement', 'date')


class UserTrophyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'trophy')


class ActiveQuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'quest', 'user')


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_one', 'user_two')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'name')

admin.site.register(LogEntry)
admin.site.register(Quest, QuestAdmin)
admin.site.register(CompleteQuest, CompleteQuestAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(UserInterests, UserInterestAdmin)
admin.site.register(UserAdditions, UserAdditionsAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Flair, FlairAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Trophy, TrophyAdmin)
admin.site.register(UserAchievement, UserAchievementAdmin)
admin.site.register(UserTrophy, UserTrophyAdmin)
admin.site.register(ActiveQuest, ActiveQuestAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.reqister(Group, GroupAdmin)
admin.site.register(UserGroup, UserGroupAdmin)
