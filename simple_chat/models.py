from django.db import models

from collections import namedtuple, deque
from datetime import datetime

class Message():
    __slots__ = ('id', 'name', 'message', 'time')
    last_id = 0

    @staticmethod
    def get_id():
        Message.last_id += 1
        return Message.last_id

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'message': self.message, 'time': self.time.strftime('%-d %b %Y %H:%M:%S')}

    def __init__(self, **kwargs):
        self.id = self.get_id()
        self.name = kwargs['name']
        self.message = kwargs['message']
        self.time = datetime.now()

    def __repr__(self):
        return u"[{}] #{} {}: <{}>".format(self.time, self.id, self.name, self.message)


MessagesPoll = deque(maxlen=500)

