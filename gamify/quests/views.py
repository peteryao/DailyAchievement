# Create your views here.
from quests.models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout


def index(request):
    user_groups = UserGroup.objects.filter(user_id=request.user.id)

    return render_to_response('index.html', {
        'current_user': request.user,
        'groups': user_groups,
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

    user_groups = UserGroup.objects.filter(user_id=request.user.id)
    return render_to_response('profile.html', {
        "current_user": request.user,
        'groups': user_groups,
        'profile_user': user,
        "user_interests": interests,
        "complete_quests": complete_quests,
        "trophy": trophy,
        "additions": additions,
        "exp_remain": float(((100 - additions.exp) / 100) * 100),
        "battles": foes,
        }, context_instance=RequestContext(request))


def quest(request):
    quest = Quest.objects.all()
    user_quests = []
    for active_quest in ActiveQuest.objects.filter(user_id=request.user.id):
        user_quests.append(active_quest.quest.id)

    print user_quests
    user_groups = UserGroup.objects.filter(user_id=request.user.id)
    return render_to_response('quests.html', {
        'current_user': request.user,
        'user_quests': user_quests,
        'groups': user_groups,
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

    user_groups = UserGroup.objects.filter(user_id=request.user.id)
    return render_to_response('group.html', {
        'current_user': request.user,
        'groups': user_groups,
        "group": group,
        "members": sort,
        "total_points": total_points,
        "total_quests": total_quests,
        "average_points": average_points,
        }, context_instance=RequestContext(request))


def leaderboard(request):
    board = UserAdditions.objects.order_by('-points')[0:20]
    quests = Quest.objects.all()[0:5]

    user_groups = UserGroup.objects.filter(user_id=request.user.id)
    return render_to_response('leaderboard.html', {
        'current_user': request.user,
        'groups': user_groups,
        "board": board,
        "quests": quests,
        }, context_instance=RequestContext(request))


def quest_page(request, quest_id):
    quest = Quest.objects.get(pk=quest_id)
    completed = CompleteQuest.objects.filter(quest_id=quest.id).order_by('-completed')
    complete_append = []
    for person in completed:
        complete_append.append(UserAdditions.objects.get(user_id=person.id))

    user_groups = UserGroup.objects.filter(user_id=request.user.id)
    return render_to_response('quest_page.html', {
        'current_user': request.user,
        'groups': user_groups,
        'quest': quest,
        'completed': zip(completed, complete_append),
        }, context_instance=RequestContext(request))


def auth_login(request):
    email = request.POST['inputName']
    password = request.POST['inputPass']
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            print "loged"
        else:
            pass
        return HttpResponseRedirect('/quests/')
    else:
        return HttpResponseRedirect('/quests/')
    return HttpResponseRedirect('/quests/')


def signout(request):
    logout(request)
    return HttpResponseRedirect('/quests/')


def about(request):

    user_groups = UserGroup.objects.filter(user_id=request.user.id)
    return render_to_response('about.html', {
        'current_user': request.user,
        'groups': user_groups,
        }, context_instance=RequestContext(request))


def current_quest(request):
    user = request.user
    active_quest = ActiveQuest.objects.filter(user_id=user.id)
    additions = UserAdditions(user_id=user.id)
    interests = UserInterests.objects.get(user_id=user.id)
    complete_quests = CompleteQuest.objects.filter(user_id=user.id).order_by("-id")[:5]
    trophy = UserTrophy.objects.filter(user_id=user.id)
    additions = user.get_profile()

    user_battles = Competition.objects.filter(Q(user_one=user.id) | Q(user_two=user.id))

    foes = []
    for battle in user_battles:
        if(battle.user_one == float(user.id)):
            foes.append(UserAdditions.objects.get(user_id=battle.user_two))
        else:
            foes.append(UserAdditions.objects.get(user_id=battle.user_one))

    print additions.exp
    print additions.rank.experience_required
    blue_bar = additions.exp

    blue_percent = blue_bar / (additions.rank.experience_required) * 100
    yellow_percent = 100 - blue_percent

    # next_rank = Rank.objects.get(pk=(additions.rank.id + 1)).experience_required

    user_groups = UserGroup.objects.filter(user_id=request.user.id)
    return render_to_response('current_quest.html', {
        'current_user': user,
        'active_quests': active_quest,
        'additions': additions,
        'profile_user': user,
        "user_interests": interests,
        "complete_quests": complete_quests,
        "trophy": trophy,
        "additions": additions,
        "exp_remain": float(((additions.exp - additions.rank.experience_required) / 100) * 100),
        "battles": foes,
        'groups': user_groups,
        # 'next_rank': next_rank,
        'blue_percent': blue_percent,
        'yellow_percent': yellow_percent,
        }, context_instance=RequestContext(request))


def add_quest(request, quest_id):
    quest = Quest.objects.get(pk=quest_id)
    user = request.user

    print quest_id
    print quest.id
    print user.id
    accept = ActiveQuest(quest_id=quest.id, user_id=user.id)
    accept.save()
    return HttpResponseRedirect('/quests/user/current/')


def add_group(request):
    user = request.user
    user_groups = UserGroup.objects.filter(user_id=request.user.id)

    all_groups = Group.objects.all()
    members = []
    for group in all_groups:
        members.append(len(UserGroup.objects.filter(group_id=group.id)))

    return render_to_response('add_group.html', {
        "current_user": user,
        'groups': user_groups,
        'all_groups': zip(all_groups, members),
        }, context_instance=RequestContext(request))


def new_group(request):
    name = request.POST['inputName']
    description = request.POST['inputDescription']
    avatar = request.POST['inputPicture']

    group = Group(name=name, description=description, avatar=avatar)
    group.save()

    return HttpResponseRedirect('/quests/group/')


def finish_quest(request, quest_id):
    quest = Quest.objects.get(pk=quest_id)
    user = request.user

    completed = CompleteQuest(user_id=user.id, quest_id=quest.id, image="")
    active = ActiveQuest.objects.filter(user_id=user.id).get(quest_id=quest.id)
    additions = UserAdditions.objects.get(user_id=user.id)

    completed.save()
    active.delete()
    additions.exp += quest.point_value
    additions.points += quest.point_value
    additions.completed += 1

    if(Rank.objects.get(pk=(additions.rank.id+1)).experience_required<additions.exp):
        additions.rank = Rank.objects.get(pk=(additions.rank.id + 1))

    additions.save()
    return HttpResponseRedirect('/quests/user/current')

def join_group(request, group_id):
    user = request.user
    group = Group.objects.get(pk=group_id)

    data = UserGroup(user_id=user.id, group_id=group.id)
    data.save()

    return HttpResponseRedirect('/quests/group/' + group_id + '/')


def cancel_quest(request, quest_id):
    quest = Quest.objects.get(pk=quest_id)
    user = request.user

    active = ActiveQuest.objects.filter(user_id=user.id).get(quest_id=quest.id)
    active.delete()

    return HttpResponseRedirect('/quests/user/current/')