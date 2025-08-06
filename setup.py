from setuptools import setup

setup(
    name='jupyterhub-jwtauthenticator-v2',
    version='2.0.3',
    description='JSONWebToken Authenticator for JupyterHub',
    url='https://github.com/I-GUIDE/iguide-jupyterhub/jwtauthenticator_v2',
    author='nosolls',
    author_email='noahsoller@gmail.com',
    license='Apache 2.0',
    packages=['jwtauthenticator'],
    install_requires=[
        'jupyterhub',
        'pyjwt',
    ]
)
