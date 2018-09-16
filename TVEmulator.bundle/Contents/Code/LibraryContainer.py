from show import Show


class LibraryContainer:
    def __init__(self, el):
        self.key = el.get('librarySectionID')
        self.rating_key = el.get('ratingKey')
        self.title = el.get('librarySectionTitle')
        self.thumb = el.get('thumb')
        self.size = el.get('size')

        self.shows = [Show(d) for d in el.finall('Directory')]
