from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Quest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    point_value = models.FloatField()
    image = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class CompleteQuest(models.Model):
    user = models.ForeignKey(User)
    quest = models.ForeignKey(Quest)
    completed = models.DateTimeField(auto_now_add=True)


