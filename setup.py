#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    setup_requires=[
        'pbr',
        'maven-artifact>=0.1.4'
    ],
    dependency_links=[
        'git+https://github.com/hamnis/maven-artifact.git@0.1.3#egg=maven-artifact-0.1.4'
    ],
    pbr=True,
)
