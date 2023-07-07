#!/usr/bin/python3
from fabric.api import *
import os
"""Clean up servers"""

env.hosts = ['18.233.67.176', '35.175.135.215']
env.user = 'ubuntu'


def do_clean(number=0):
    """Delete old versions of archives"""
    local_archives = sorted(os.listdir("versions"))
    remote_archives = run("ls /data/web_static/releases/*web_static*").split()
    if int(number) == 0:
        number = 1
    for i in range(int(number)):
        local_archives.pop()
        remote_archives.pop()
    for archive in local_archives:
        with lcd("versions"):
            local("rm {}".format(archive))
    for archive in remote_archives:
        with cd("/data/web_static/releases/"):
            sudo("rm -rf {}".format(archive))
