#!/usr/bin/env python3
# encoding: utf-8
import argparse
import json
import os
from base64 import b64decode
from getpass import getpass

DEFAULT_PATHS = ['~/.config/keys.json']
CONFIG = os.path.expanduser('~/.config/getkeys.json')
if os.path.exists(CONFIG):
    with open(CONFIG, 'r') as handle:
        DEFAULT_PATHS = json.load(handle).get('paths')


def getkey(attrstr, paths=None, prompt=True, promptpass=False):
    """ Searches the specified path locations for the specified key. """
    paths = paths or DEFAULT_PATHS
    for path in paths:
        filepath = os.path.expanduser(path)
        if not os.path.exists(filepath):
            continue
        with open(filepath, 'r') as handle:
            value = rget(json.load(handle), attrstr)
            if value is None:
                continue
            if isinstance(value, dict):
                raise Exception(f'Ambiguous key: {attrstr}')
            if isinstance(value, list):
                return value
            if not isinstance(value, str):
                return value
            if not value.startswith('b64:'):
                return value
            return b64decode(value[4:]).decode('utf8')
    promptfunc = getpass if promptpass else input
    if prompt:
        return promptfunc(f'Enter {attrstr}: ')
    pathstr = '\n' + '\n'.join(paths)
    raise Exception(f'Key not found: {attrstr}{pathstr}')


def rget(obj, attrstr, default=None, delim='.'):
    """ Searches a nested dict structure for the specified key. """
    try:
        parts = attrstr.split(delim, 1)
        attr = parts[0]
        attrstr = parts[1] if len(parts) == 2 else None
        if isinstance(obj, dict):
            value = obj[attr]
        elif isinstance(obj, list):
            value = obj[int(attr)]
        elif isinstance(obj, tuple):
            value = obj[int(attr)]
        elif isinstance(obj, object):
            value = getattr(obj, attr)
        if attrstr:
            return rget(value, attrstr, default, delim)
        return value
    except Exception:
        return default


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Searches config paths for the specified key.')
    parser.add_argument('attrstr', help='Lookup of key to find.')
    opts = parser.parse_args()
    print(getkey(opts.attrstr, prompt=False))
