#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    setup_requires=[
        'pbr>=1.9', 'setuptools>=17.1',
        'maven-artifact>=0.1.4',
        'six', 'future'
    ],
    dependency_links=[
        'git+https://github.com/hamnis/maven-artifact.git@0.1.4#egg=maven-artifact-0.1.4'
    ],
    pbr=True,
)
