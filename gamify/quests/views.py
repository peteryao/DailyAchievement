# Create your views here.
from quests.models import *
from django.contrib.auth.models import User
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response


def index(request):
    return render_to_response('index.html', {

        }, context_instance=RequestContext(request))


def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    interests = UserInterests.objects.get(user_id=user_id)
    complete_quests = CompleteQuest.objects.filter(user_id=user_id).order_by("-id")[:5]
    trophy = UserTrophy.objects.filter(user_id=user.id)
    additions = user.get_profile()

    return render_to_response('profile.html', {
        "current_user": user,
        "user_interests": interests,
        "complete_quests": complete_quests,
        "trophy": trophy,
        "additions": additions,
        }, context_instance=RequestContext(request))


def quest(request):
    quest = Quest.objects.all()

    return render_to_response('quests.html', {
        "quest": quest,
        }, context_instance=RequestContext(request))
