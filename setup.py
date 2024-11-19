from setuptools import setup, find_packages

setup(
    name='mygoogleAuth',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-login',
        'oauthlib',
        'request',
    ],
    url='https://github.com/lupin-oomura/mygoogleAuth.git',
    author='Shin Oomura',
    author_email='shin.oomura@gmail.com',
    description='google認証用の便利クラス',
)
