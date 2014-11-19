__author__ = 'tivvit'

from protorpc import messages

class Quest_input_m(messages.Message):
    name = messages.StringField(1)
    faction = messages.IntegerField(2)
    points = messages.IntegerField(3)
    num = messages.IntegerField(4)
    id = messages.IntegerField(5)

class Quest_m(messages.Message):
    name = messages.StringField(1)
    faction = messages.StringField(2)
    points = messages.IntegerField(3)
    num = messages.IntegerField(4)
    id = messages.IntegerField(5)
    # inserted = messages.DateTimeField(5)

class QuestsCollection_m(messages.Message):
    quest = messages.MessageField(Quest_m, 1, repeated=True)