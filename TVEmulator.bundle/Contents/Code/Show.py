from Interface import get_libraries

_shows = []


def init():
    for l in get_libraries():
        for s in l.shows:
            _shows[s.rating_key] = s


def get(key):
    if key in _shows:
        return _shows[key]
    else:
        return None