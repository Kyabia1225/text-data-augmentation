#! -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='tda',
    version='1.0',
    author='kyabia',
    packages=find_packages(),
    install_requires=['synonyms', 'tqdm', 'nltk'],
    package_data={
        '': ['*.txt']
    }
)
