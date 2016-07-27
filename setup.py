#!/usr/bin/env python
import sys
import os
from setuptools.command.install import install
from distutils.core import setup
from os.path import abspath, dirname, join
from setuptools import setup

class MyInstall(install):
   def run(self):
       install.run(self)
       cmd = "pip install mysql-connector --egg pyenv"
       print os.popen(cmd).read()

    

execfile(join(dirname(abspath(__file__)), 'src', 'InterfaceLibrary', 'version.py'))

setup(name         = 'robotframework-interfacelibrary',
      version      = VERSION,
      description  = 'Interface test library for Robot Framework Based on requests/mysql modules',
      long_description = open(join(dirname(__file__), 'README.rst')).read(),
      author       = 'WuQi,WeiYaTing',
      author_email = '<wuqi@yixin.im>',
      url          = 'https://g.hz.netease.com/yixinplusQA/RFUI_Framework/tree/master/Third-Party-Module/YX_RFIT_Framework',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework interface testing test automation http client requests',
      platforms    = 'any',
      classifiers  = [
                        "Development Status :: 5 - Production/Stable",
                        "License :: OSI Approved :: Apache Software License",
                        "Operating System :: OS Independent",
                        "Programming Language :: Python",
                        "Topic :: Software Development :: Testing"
                     ],
      package_dir  = {'' : 'src'},
      packages     = ['InterfaceLibrary'],
      package_data = {'InterfaceLibrary': ['version.py']},
      install_requires = [
          'robotframework',
          'requests',
          'httplib2'],
      include_package_data = True,
      cmdclass = {'install':MyInstall}
      )
