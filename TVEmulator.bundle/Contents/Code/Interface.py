from library import Library

host = 'http://127.0.0.1'
port = '32400'

# Core Method
def query(target):
    url = host + ":" + port + target
    return XML.ElementFromURL(url)


def get_libraries():
    tree = query('/library/sections')
    lib_list = tree.findall("Directory[@type='show']")
    return [Library(get_library_info(lib.attrib['key'])) for lib in lib_list]


def get_library_info(key):
    return query('/library/sections/' + key + '/all')
