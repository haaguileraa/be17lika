#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from distutils.core import setup
from setuptools import find_packages
setup(name='be17lika',
version='0.1',
author='Shirin Heidarikahkesh',
author_email='shirin.heidarikahkesh@fau.de',
packages=find_packages(),
install_requires=['numpy', 'Pillow', 'ipywidgets'])

