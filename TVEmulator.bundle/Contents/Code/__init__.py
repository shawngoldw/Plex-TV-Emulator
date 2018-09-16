import Show
import ChannelSelector

TITLE    = 'TV Emulator'
PREFIX   = '/video/tvemulator'

ART      = 'art-default.jpg'
ICON     = 'icon-default.png'


def Start():
  ObjectContainer.title1 = TITLE
  ObjectContainer.art = R(ART)

  Show.init()


@handler(PREFIX, TITLE, art=ART, thumb=ICON)
def MainMenu():
  return ObjectContainer(objects=ChannelSelector.GetContainer())




def GetShows(channel_id):
    objs = []
    for s in Show.shows:
        objs.append(
            TVShowObject(
                key = Callback(ToggleShow, rating_key=s.rating_key, channel_id=channel_id),
                rating_key = s.rating_key,
                title = s.title,
                thumb = s.thumb
            )
        )
  return ObjectContainer(objects=objs)



def NewChannel():
  Log.Debug("NEW")
  channel_id = 1
  return GetShows(channel_id)


def ToggleShow(channel_id, rating_key):
  Log.Debug(rating_key)
  return GetShows(channel_id)
