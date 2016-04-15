#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

cmd = sys.argv[-1]
if (cmd.startswith('install') or cmd.startswith('bdist') or cmd.startswith('test')
    or cmd == 'develop'):
    os.system("python setup.py download_jar")

setup(
    setup_requires=[
        'pbr>=1.9',
        'setuptools>=17.1',
        'maven-artifact>=0.1.3'
    ],
    pbr=True,
)
