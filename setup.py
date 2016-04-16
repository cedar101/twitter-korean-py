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
        'pbr',
        #'setuptools>=17.1',
        'maven-artifact>=0.1.4'
    ],
    dependency_links=['git+https://github.com/hamnis/maven-artifact.git@0.1.3#egg=maven-artifact-0.1.4'],
    pbr=True,
)