#!/usr/bin/env python

from setuptools import setup


setup(
    author='Amol Bhave',
    author_email='ambhave' '@' 'mit.edu',
    description='SQLAlchemy extension for SimQL',
    entry_points="""
    [sqlalchemy.dialects]
    simql = sqlalchemy_simql.dialect:SimqlDialect
    """,
    install_requires=[
        'SQLAlchemy>=0.9.4',
    ],
    long_description=open('README.md', 'rt').read(),
    name='SQLAlchemy-SimQL',
    packages=[
        'sqlalchemy_simql',
        'sqlalchemy_simql.dbapi2',
        'sqlalchemy_simql.dialect',
    ],
    url='https://github.com/ammubhave/sqlalchemy-simql',
    version='0.1.0',
)
