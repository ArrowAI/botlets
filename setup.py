from __future__ import print_function
from setuptools import setup, find_packages
import os


AUTHOR = 'Arrow AI'
AUTHOR_EMAIL = 'utkarsh@arrowai.com'
DOWNLOAD_URL = 'https://github.com/ArrowAI/botlets.git'
LICENSE = 'MIT'
DESCRIPTION = 'Create Botlets for quick and easy Bot Development'

INSTALL_REQUIRES = ['numpy', 'tensorflow', 'easydict']

    setup(name='botlets',
          version=0.1,
          description=DESCRIPTION,
          long_description=DESCRIPTION,
          download_url=DOWNLOAD_URL,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          license=LICENSE,
          packages=find_packages(exclude=['tests',
                                          'tests.*',
                                          '*.tests',
                                          '*.tests.*']),
          install_requires=INSTALL_REQUIRES,
          zip_safe=False)
