#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    setup_requires=[
        'pbr',
        'maven-artifact',
        'six', 'future'
    ],
    dependency_links=[
        'git+https://github.com/hamnis/maven-artifact.git@0.1.4#egg=maven-artifact-0.1.4'
    ],
    pbr=True,
)
