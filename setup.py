#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup
os.environ.update(SKIP_GENERATE_AUTHORS='1',
                  SKIP_WRITE_GIT_CHANGELOG='1')

setup(
    setup_requires=['pbr', #>=1.9', #'setuptools>=17.1',
                    'six', 'future',
                    'maven-artifact>=0.1.4'],
    pbr=True,
    dependency_links = [
        'git+https://github.com/hamnis/maven-artifact.git@0.1.4#egg=maven-artifact-0.1.4'
    ]
)
