from json import JSONEncoder
from datetime import datetime


class Encoder(JSONEncoder):

    def default(self, obj: object):
        if isinstance(obj, datetime):
            return {'__datetime__': obj.replace(microsecond=0).isoformat()}
        return {f'__{obj.__class__.__name__}__': obj.__dict__}
