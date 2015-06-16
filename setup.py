#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

root = os.path.abspath(os.path.dirname(__file__))

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

with open(os.path.join(root, "requirements.txt")) as reqs:
    requirements = [r.strip() for r in reqs.readlines()]

with open(os.path.join(root, "requirements-dev.txt")) as reqs:
    test_requirements = [r.strip() for r in reqs.readlines()]

setup(
    name='luh3417',
    version='0.1.0',
    description="LUH3417 is a reddit crawling NLP framework.",
    long_description=readme + '\n\n' + history,
    author="James Kyle",
    author_email='james@jameskyle.org',
    url='https://github.com/jameskyle/luh3417',
    packages=[
        'luh3417',
    ],
    package_dir={'luh3417':
                 'luh3417'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache",
    zip_safe=False,
    keywords='luh3417',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
