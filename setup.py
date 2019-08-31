"""
setup.py file.

May 01, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    README = f.read()

with open(os.path.join(here, 'HISTORY.rst'), encoding='utf-8') as f:
    HISTORY = f.read()

setup(name='typed-tree',
      version='1.0.1',  # Bump version NUMBER *after* starting (git flow) release.
      description='TypedTree provides a tree structure that allows adding type information to its nodes and relations, respectively.',
      long_description=README + '\n\n' + HISTORY,
      keywords='typed tree, data structure, hierarchy, tree, visualization',
      url='https://github.com/brettkromkamp/typed-tree',
      author='Brett Alistair Kromkamp',
      author_email='brett.kromkamp@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['docs', 'tests*', 'scripts']),
      package_data={'': ['LICENSE']},
      include_package_data=True,
      zip_safe=False,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ])
