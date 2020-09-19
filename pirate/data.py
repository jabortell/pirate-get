import json
import pkgutil
import os
import sys

def get_resource(filename):
    return pkgutil.get_data(__package__, 'data/' + filename)

def get_path(filename):
    return os.path.join(os.path.dirname(sys.modules[__package__].__file__), 'data', filename)

def write_resource(data, filename):
    path = get_path(filename)
    with open(path, 'w') as fp:
        fp.write(data)

def update_mru_mirror(mirror):
    write_resource(mirror, 'mru_mirror.txt')

version = '0.4.0'

categories = json.loads(get_resource('categories.json').decode())
sorts = json.loads(get_resource('sorts.json').decode())
blacklist = set(json.loads(get_resource('blacklist.json').decode()))
mru_mirror = get_resource('mru_mirror.txt').decode()

default_headers = {'User-Agent': 'pirate get'}
default_timeout = 10

default_mirror = 'https://apibay.org'
mirror_list = 'https://proxybay.bz/list.txt'
