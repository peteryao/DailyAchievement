# Create your views here.
from django.contrib.auth.models import User
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response


def index(request):
    return render_to_response('index.html', {

        }, context_instance=RequestContext(request))


def profile(request, user_id):
    user = User.objects.get(pk=user_id)

    return render_to_response('profile.html', {
        "current_user": user,
        }, context_instance=RequestContext(request))
