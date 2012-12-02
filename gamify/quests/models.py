from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class Flair(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)


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
    image = models.CharField(max_length=200)
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
    points = models.FloatField()
    occupation = models.CharField(max_length=200)
    avatar = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    flair = models.ForeignKey(Flair)


class Rank(models.Model):
    name = models.CharField(max_length=200)
    experience_required = models.FloatField()


class Achievement(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    requirements = models.CharField(max_length=200)


class UserAchievement(models.Model):
    user = models.ForeignKey(User)
    achievement = models.ForeignKey(Achievement)
    date = models.DateTimeField(auto_now_add=True)


class Trophy(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    achievement = models.ForeignKey(Achievement)


class UserTrophy(models.Model):
    user = models.ForeignKey(User)
    trophy = models.ForeignKey(Trophy)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserAdditions.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
