from quests.models import Quest, CompleteQuest
from django.contrib import admin
from django.contrib.admin.models import LogEntry

class QuestAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'description', 'point_value', 'image')

class CompleteQuestAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'quest', 'completed')

admin.site.register(LogEntry)
admin.site.register(Quest, QuestAdmin)
admin.site.register(CompleteQuest, CompleteQuestAdmin)