from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import MessagesPoll, Message
from .forms import MessageForm

from itertools import islice
import json
import logging

logger = logging.getLogger('simple_chat.messages')


def index(request):
    """
    basic view, that render chat page
    :return: html
    """
    form = MessageForm()
    if request.user.is_authenticated():
        form.fields['name'].initial = request.user.username
    return render(request, 'simple_chat/index.html', {'form': form})


@login_required
@csrf_exempt
def send_message(request):
    """
    this view receive message form chat user and put it to messages queue
    """
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
    """
    every few seconds users pull messages from messages queue by sending request to this view
    :return json: list of new messages
    """
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
        res = [message.to_json() for message in islice(MessagesPoll, 0, 10)]
        if res:
            new_last_id = res[0]['id']

    return HttpResponse(json.dumps({'messages': list(reversed(res)), 'last_message_id': new_last_id}),
                        content_type='application/json')