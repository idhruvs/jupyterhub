#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Application configuration
#-----------------------------------------------------------------------------------------------------------------------------------------------------

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

# Let the Systemctl aware of all the environment path
import os
for var in os.environ:
    c.Spawner.env_keep.append(var)

