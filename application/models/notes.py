from application.models.abc_models import Entity
from application.services.data import Encoder

from datetime import datetime

import json


class SimpleNote(Entity):

    __timestamp: datetime
    __title: str
    __note: str

    def __init__(self, uid: str):
        super().__init__(uid)
        self.timestamp = None

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value: datetime):
        self.__timestamp = value if value else datetime.now().replace(microsecond=0)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    def dumps(self):
        return str(self)

    @staticmethod
    def __decode(obj):
        if SimpleNote.__class_name() in obj:
            restored = SimpleNote("0")
            restored.__dict__.update(obj[SimpleNote.__class_name()])
            return restored
        elif '__datetime__' in obj:
            return datetime.strptime(obj['__datetime__'], '%Y-%m-%dT%H:%M:%S')
        return obj

    @classmethod
    def loads(cls, json_str: str):
        return json.loads(json_str, object_hook=cls.__decode)

    @classmethod
    def __class_name(cls):
        return f"__{cls.__name__}__"

    def __str__(self):
        return json.dumps(self, cls=Encoder)


def tests():
    note = SimpleNote('1')
    note.title = 'My first draft'
    note.note = "It's my awesome draft"

    serialized = note.dumps()
    print(serialized)

    deserialized = SimpleNote.loads(serialized)
    print(deserialized)


if __name__ == '__main__':
    pass
else:
    tests()