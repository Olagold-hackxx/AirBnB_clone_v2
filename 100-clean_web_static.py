#!/usr/bin/python3
from fabric.api import *
import os
"""Generates a tar archive"""

def do_clean(number=0):
    archives = sorted(os.listdir("versions"))
    if number == 0:
        number = 1
    for archive in archives[:-{}.format(number)]:
        with lcd("versions"):
            local("rm ./{}".format(archive))
        with cd("/data/web_static/releases")
            run("rm ./{}".format(archive))
