#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='pcpd',
    version='0.0.0',
    description='demo/comparison of different python cli argument parsing libraries',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='cli',
    author='jitakirin',
    author_email='jitakirin@gmail.com',
    url='https://github.com/jitakirin/python-cli-parsers',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'click ~= 6.6',
        'clize ~= 3.1',
        'defopt ~= 2.0',
        'argh ~= 0.26',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
