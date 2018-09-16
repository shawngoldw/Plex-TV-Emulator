_channels = []


def init():
    pass


def get_all():
    return _channels

def get(key):
    if key in _channels:
        return _channels[key]
    else:
        return None


def create():
    pass