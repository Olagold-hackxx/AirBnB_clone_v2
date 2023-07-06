#!/usr/bin/python3
"""Deploy archive with fabric"""
from fabric.api import *
import os

env.hosts = ['18.233.67.176', '35.175.135.215']
env.user = 'ubuntu'


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    path = "{}".format(archive_path[9:-4])
    path_tgz = "{}".format(archive_path[9:])
    try:
        put("{}".format(archive_path), "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(path))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(path_tgz, path))
        run("rm -rf /tmp/{}".format(path_tgz))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(path, path))
        run("rm -rf /data/web_static/releases/{}/web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(path))
    except Exception:
        return False
    print("New version deployed!")
    return True
