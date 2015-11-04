from collections import deque
from datetime import datetime


class Message:
    """
    Instances of this class keep info about every message from chat.
    Class doesn't inherit django.db.models, because we do not need to save them to db.
    Instances keep the data in slots, it saves a bit memory.
    Class property last_id saves last message id. It useful for recipients to track messages, that they already received
    """
    __slots__ = ('id', 'name', 'message', 'time')
    last_id = 0

    @staticmethod
    def get_id():
        """
        Method returns incremented message_id
        Return: int: next message id
        """
        Message.last_id += 1
        return Message.last_id

    def to_json(self):
        """
        Method that returns the message data in format suited for json.dumps function
        Return: dict: message data that will be send to chat message recipients
        """
        return {'id': self.id, 'name': self.name, 'message': self.message, 'time': self.time.strftime('%-d %b %Y %H:%M:%S')}

    def __init__(self, **kwargs):
        self.id = self.get_id()
        self.name = kwargs['name']
        self.message = kwargs['message']
        self.time = datetime.now()

    def __repr__(self):
        return u"[{}] #{} {}: <{}>".format(self.time, self.id, self.name, self.message)


MessagesPoll = deque(maxlen=500) #messages queue

