#!/usr/bin/python3
"""Generates a .tgz archive"""
from fabric.api import *
from datetime import datetime

def do_pack():
    """Generates a .tgz archive"""
    local("mkdir -p versions")
    time = datetime.now()
    path = "versions/web_static_{}{}{}{}{}{}".format(time.year,
                                                     time.month, time.day,
                                                     time.hour, time.minute,
                                                     time.second)
    return_value = local("tar -cvzf {}.tgz web_static".format(path))
    if return_value != 0:
        return None
    return path
