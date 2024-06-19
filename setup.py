#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='getkeys',
    version='1.0.2',
    description='Micro-package to get keys from a list of paths',
    author='Michael Shepanski',
    author_email='michael.shepanski@gmail.com',
    url='https://github.com/pkkid/python-getkeys',
    packages=['getkeys'],
    python_requires='>=3.5',
    long_description=open('README.md', 'r').read(),
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
    ]
)
