from django.shortcuts import render, get_object_or_404
from .forms import MessageForm
import json


from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import logging
logger = logging.getLogger('simple_chat.messages')

import itertools
from .models import MessagesPoll, Message

from django.contrib.auth.decorators import login_required


def index(request):
    form = MessageForm()
    if request.user.is_authenticated():
        form.fields['name'].initial = request.user.username
    return render(request, 'simple_chat/index.html', {'form': form})


@login_required
@csrf_exempt
def send_message(request):
    response = {}
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message(**form.cleaned_data)
            logger.info(message)
            MessagesPoll.appendleft(message)
            response['success'] = True

    return HttpResponse(json.dumps(response), content_type='application/json')


def get_messages(request, last_message_id):
    last_message_id = int(last_message_id)
    new_last_id = 0
    if last_message_id:
        res = []
        for message in MessagesPoll:
            if message.id > last_message_id:
                res.append(message.to_json())
                new_last_id = new_last_id or message.id
            else:
                break
    else:
        res = [message.to_json() for message in itertools.islice(MessagesPoll, 0, 10)]
        if res:
            new_last_id = res[0]['id']

    return HttpResponse(json.dumps({'messages': list(reversed(res)), 'last_message_id': new_last_id}),
                        content_type='application/json')