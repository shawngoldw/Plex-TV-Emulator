
class Show:
    def __init__(self, el):
        self.key = el.attrib['key']
        self.title = el.attrib['title']
        self.thumb = el.attrib['thumb']
        self.episode_count = el.attrib['leafCount']