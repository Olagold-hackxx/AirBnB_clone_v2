#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os
"""Generates a tar archive"""


def do_pack():
    """Generates a .tgz archive"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    time = datetime.now()
    path = "versions/web_static_{}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz"\
        .format(time.year, time.month, time.day, time.hour, time.minute,
                time.second)
    print("Packing web_static to {}".format(path))
    try:
        local("tar -cvzf {} web_static".format(path))
        size = os.stat(path).st_size
        print("web_static packed: {} -> {}Bytes".format(path, size))
    except:
        return None
    return path
