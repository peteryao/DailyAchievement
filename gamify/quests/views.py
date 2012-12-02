# Create your views here.
from quests.models import *
from django.db.models import Q
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

    user_battles = Competition.objects.filter(Q(user_one=user_id) | Q(user_two=user_id))

    foes = []
    for battle in user_battles:
        if(battle.user_one == float(user_id)):
            foes.append(UserAdditions.objects.get(user_id=battle.user_two))
        else:
            foes.append(UserAdditions.objects.get(user_id=battle.user_one))

    return render_to_response('profile.html', {
        "current_user": user,
        "user_interests": interests,
        "complete_quests": complete_quests,
        "trophy": trophy,
        "additions": additions,
        "exp_remain": float(((100 - additions.exp) / 100) * 100),
        "battles": foes,
        }, context_instance=RequestContext(request))


def quest(request):
    quest = Quest.objects.all()

    return render_to_response('quests.html', {
        "quest": quest,
        }, context_instance=RequestContext(request))


def group(request, group_id):
    group = Group.objects.get(pk=group_id)
    members = []
    for member in UserGroup.objects.filter(group_id=group_id):
        members.append(member.user)

    total_points = 0
    total_quests = 0
    average_points = 0
    for member in members:
        total_points += member.get_profile().points

    average_points = (total_points / len(members))

    for member in members:
        total_quests += len(CompleteQuest.objects.filter(user_id=member.id))

    data = sorted(members, key=lambda user: -user.get_profile().points)
    print data
    sort = []
    for i in data:
        sort.append(UserAdditions.objects.get(user_id=i.id))

    return render_to_response('group.html', {
        "group": group,
        "members": sort,
        "total_points": total_points,
        "total_quests": total_quests,
        "average_points": average_points,
        }, context_instance=RequestContext(request))


def leaderboard(request):
    board = UserAdditions.objects.order_by('-points')[0:20]
    quests = Quest.objects.all()[0:5]

    return render_to_response('leaderboard.html', {
        "board": board,
        "quests": quests,
        }, context_instance=RequestContext(request))


def quest_page(request, quest_id):
    quest = Quest.objects.get(pk=quest_id)
    completed = CompleteQuest.objects.filter(quest_id=quest.id).order_by('-completed')
    complete_append = []
    for person in completed:
        complete_append.append(UserAdditions.objects.get(user_id=person.id))

    return render_to_response('quest_page.html', {
        'current_user': request.user,
        'quest': quest,
        'completed': zip(completed, complete_append),
        }, context_instance=RequestContext(request))
