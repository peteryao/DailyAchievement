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


class Interest(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class UserInterests(models.Model):
    user = models.ForeignKey(User)
    interest = models.ForeignKey(Interest)


class UserAdditions(models.Model):
    user = models.OneToOneField(User)
    exp = models.FloatField()
    occupation = models.CharField(max_length=200)
    avatar = models.CharField(max_length=200)
    location = models.CharField(max_length=200)


class Rank(models.Model):
    name = models.CharField(max_length=200)
    experience_required = models.FloatField()
