#!/usr/bin/python3
from fabric.api import *
import os
"""Clean up servers"""

env.hosts = ['18.233.67.176', '35.175.135.215']
env.user = 'ubuntu'


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    local_archives = sorted(os.listdir("versions"))
    remote_archives = run("ls -1tr /data/web_static/releases/*web_static*")\
        .split("\n")
    if int(number) == 0:
        number = 1
    for i in range(int(number)):
        local_archives.pop()
        remote_archives.pop()
    with lcd("versions"):
        for archive in local_archives:
            local("rm ./{}".format(archive))
    with cd("/data/web_static/releases/"):
        for archive in remote_archives:
            run("rm -rf ./{}".format(archive))
