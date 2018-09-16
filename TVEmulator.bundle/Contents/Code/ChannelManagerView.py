import Channel

def get_main_view():
    objs = [_new_channel()]
    return ObjectContainer(objects=objs)


def _new_channel():
    return DirectoryObject(
        key=Callback(_create_channel),
        title="Create New Channel"
    )


def _channels():
    return [_channel(c) for c in Channel.channels]

def _channel(channel):
    return None


def _create_channel():
    Channel.create()
    return get_main_view()




