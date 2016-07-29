#!/usr/bin/env python
# coding: utf-8
import setuptools
import os
print os.popen("pip install http://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.0.4.zip#md5=3df394d89300db95163f17c843ef49df").read()
setuptools.setup(setup_requires=['pbr'], pbr=True,package_dir = {'': 'src'},packages=["InterfaceLibrary"])
