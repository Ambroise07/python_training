#!/usr/bin/env python
from setuptools import setup
from Cython.Build import cythonize

setup(
    name = "HACK",
    ext_modules=cythonize('main.py')
)
