#!/usr/bin/env python

from distutils.core import setup

setup(name='vechess',
  version='0.0.1',
  description='Very simple chess board automation',
  author='Mikhail Efremov, Ilya Vinnik',
  author_email='meechanic.design@gmail.com',
  url='https://github.com/veprojectslab',
  license="MIT",
  scripts=['bin/vechesscli'],
  packages=['vechess']
)
