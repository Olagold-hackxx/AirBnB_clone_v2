#!/usr/bin/python3
"""Deploy archive with fabric"""
from fabric.api import *
import os

env.hosts = ['18.233.67.176', '35.175.135.215']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        return False
    path = "{}".format(archive_path[9:-4])
    path_tgz = "{}".format(archive_path[9:])
    try:
        put("{}".format(archive_path), "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(path))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(path_tgz, path))
        sudo("rm -rf /tmp/{}".format(path_tgz))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(path, path))
        sudo("rm -rf /data/web_static/releases/{}/web_static".format(path))
        sudo("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(path))
        print("New version deployed!")
        return True
    except Exception:
        return False
