#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers
"""

from fabric.api import env, local, run, put
from datetime import datetime
from os import path

env.hosts = ['54.146.62.81', '54.173.110.138']
env.user = 'ubuntu'  
env.key_filename = '~/.ssh/id_rsa'  


def do_pack():
    """Creates a compressed archive of the web_static folder"""
    try:
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = 'versions/web_static_{}.tgz'.format(current_time)
        local('mkdir -p versions')
        local('tar -czvf {} web_static'.format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        remote_path = "/data/web_static/releases/{}/".format(no_ext)
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(remote_path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, remote_path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}web_static/* {}'.format(remote_path, remote_path))
        run('rm -rf {}web_static'.format(remote_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(remote_path))
        return True
    except:
        return False


def deploy():
    """Deploys the web_static folder to the web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
