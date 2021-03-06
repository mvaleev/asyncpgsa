#!/usr/bin/env python3
from setuptools import setup, find_packages

version = {}

with open('asyncpgsa/version.py') as f:
    exec(f.read(), version)

setup(
    name='asyncpgsa',
    version=version['__version__'],
    install_requires=[
        'asyncpg==0.18.3',
        'sqlalchemy==1.3.4',
    ],
    packages=['asyncpgsa', 'asyncpgsa.testing'],
    url='https://github.com/canopytax/asyncpgsa',
    license='Apache 2.0',
    author='nhumrich',
    author_email='nick.humrich@canopytax.com',
    description='sqlalchemy support for asyncpg'
)
