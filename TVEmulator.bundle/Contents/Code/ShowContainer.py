
class ShowContainer:
    def __init__(self, el):
        self.key = el.get('key')
        self.rating_key = el.get('ratingKey')
        self.title = el.get('title')
        self.thumb = el.get('thumb')
        self.episode_count = el.get('leafCount')