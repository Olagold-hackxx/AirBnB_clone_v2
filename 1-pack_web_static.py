#!/usr/bin/python3
"""Generates a .tgz archive"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Generates a .tgz archive"""
    local("mkdir -p versions")
    time = datetime.now()
    path = "versions/web_static_{}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz"\
        .format(time.year, time.month, time.day, time.hour, time.minute,
                time.second)
    result = local("tar -cvzf {} web_static".format(path))
    if result.failed:
        return None
    return path
