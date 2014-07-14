#!/usr/bin/env python

from distutils.core import setup


setup(
    author='Amol Bhave',
    author_email='ambhave' '@' 'mit.edu',
    description='SQLAlchemy extension for SimQL',
    install_requires=[
        'SQLAlchemy>=0.9.4',
    ],
    long_description=open('README.md', 'rt').read(),
    name='SQLAlchemy-SimQL',
    packages=[
        'sqlalchemy_simql',
    ],
    url='https://github.com/ammubhave/sqlalchemy-simql',
    version='0.1.0',
)
