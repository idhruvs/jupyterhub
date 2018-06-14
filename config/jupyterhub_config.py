#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Github based Application configuration
#-----------------------------------------------------------------------------------------------------------------------------------------------------
import os
import logging

def create_dir_hook(spawner):
    username = spawner.user.name
    volume_path = os.path.join('/home', username)
    logging.info('UserDirectory Creation hook')
    logging.info(username)
    if not os.path.exists(volume_path):
        os.mkdir(volume_path, 0o755)
        notebook_path = os.path.join(volume_path, 'notebooks')
        os.mkdir(notebook_path, 0o755)

c.Spawner.pre_spawn_hook = create_dir_hook

# Use the DockerSpawner to serve your users' notebooks
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]
c.DockerSpawner.hub_ip_connect = public_ips()[0]
c.DockerSpawner.container_ip = "0.0.0.0"
c.DockerSpawner.volumes = {'/volumes/jupyterhub/{username}': '/home/'}

# This is an application.
c.JupyterHub.authenticator_class = 'oauthenticator.GitHubOAuthenticator'
c.GitHubOAuthenticator.oauth_callback_url = 'http://127.0.0.1:8000/hub/oauth_callback'
c.GitHubOAuthenticator.client_id = 'c828ac8087559fc77d31'
c.GitHubOAuthenticator.client_secret = 'd00acd14a9769bdbd0dfe996bff2c86a2ee0ecee'
# This is an application.
# create system users that don't exist yet
c.LocalAuthenticator.create_system_users = True
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'
c.JupyterHub.proxy_cmd = ['/opt/conda/bin/configurable-http-proxy']
