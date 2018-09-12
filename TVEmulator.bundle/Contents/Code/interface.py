import urllib
import urllib2

import xml.etree.ElementTree as ElementTree

from library import Library



TOKEN_VAL = 'mAqzPzwNDgEkd4VzxKZo'

# Core Method
def query(target, get=None):
    # TEMPORARY - need to figure out host/port and token on local box
    host = 'http://192.168.0.165:32400'
    if get == None:
        get = {}
    get['X-Plex-Token'] = TOKEN_VAL

    get_str = ''
    if len(get) > 0:
        get_str = '?' + urllib.urlencode(get)

    request = host + target + get_str
    contents = urllib2.urlopen(request).read()
    return ElementTree.ElementTree(ElementTree.fromstring(contents))


# Core Method
def print_xml(tree):
    print ElementTree.tostring(tree, encoding='utf8', method='xml')


def get_libraries():
    tree = query('/library/sections')
    lib_list = tree.findall("Directory[@type='show']")
    return [Library(get_library_info(lib.attrib['key'])) for lib in lib_list]


def get_library_info(key):
    return query('/library/sections/' + key + '/all')


libs = get_libraries()
for l in libs:
    for s in l.show:
        print s.title
