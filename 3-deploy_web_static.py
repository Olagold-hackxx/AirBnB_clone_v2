#!/usr/bin/python3
from fabric.api import *
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
    try:
        print("Packing web_static to {}".format(path))
        local("tar -cvzf {} web_static".format(path))
        size = os.stat(path).st_size
        print("web_static packed: {} -> {}Bytes".format(path, size))
    except Exception:
        return None
    return path


env.hosts = ['18.233.67.176', '35.175.135.215']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Deploy archive with fabric to server"""
    if not os.path.exists(archive_path):
        return False
    path = "{}".format(archive_path[9:-4])
    path_tgz = "{}".format(archive_path[9:])
    try:
        put("{}".format(archive_path), "/tmp/")
        sudo("mkdir -p /data/web_static/releases/{}".format(path))
        sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(path_tgz, path))
        sudo("rm -rf /tmp/{}".format(path_tgz))
        sudo("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(path, path))
        sudo("rm -rf /data/web_static/releases/{}/web_static".format(path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(path))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """Deploy to server"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
