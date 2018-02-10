from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Notification
import datetime


def index(request):
    if request.method == 'POST':
        # save new post
        data = request.POST
        sender = data['sender']
        content = data['content']
        if 'request_moderation' in data:
            request_moderation = data['request_moderation']
        else:
            request_moderation = False
        post = Notification(sender=sender)
        post.created_at = datetime.datetime.now()
        post.content = content
        post.active = True
        post.request_moderation
        post.save()

        # Get all posts from DB
        posts = Notification.objects
        return render_to_response('index.html', {'Posts': posts},
                                  context_instance=RequestContext(request))
