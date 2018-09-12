from show import Show


class Library:
    def __init__(self, el):
        el = el.getroot()
        self.key = el.attrib['librarySectionID']
        self.title = el.attrib['librarySectionTitle']
        self.thumb = el.attrib['thumb']
        self.size = el.attrib['size']

        dirs = el.findall("Directory")
        self.show = []
        for dir in dirs:
            self.show.append(Show(dir))