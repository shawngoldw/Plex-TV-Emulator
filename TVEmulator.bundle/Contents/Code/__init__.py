TITLE    = 'Channel Title'
PREFIX   = '/video/TVEmulator'

ART      = 'art-default.jpg'
ICON     = 'icon-default.png'


def Start():
  ObjectContainer.title1 = TITLE
  ObjectContainer.art = R(ART)


@handler(PREFIX, TITLE, art=ART, thumb=ICON)
def MainMenu():
  oc = ObjectContainer()
  return oc