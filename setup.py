#!/usr/bin/env python

#  Copyright 2013-2014 NaviNet Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys
#from distutils.core import setup
from setuptools import setup
from os.path import join, dirname

sys.path.append(join(dirname(__file__), 'EyesLibrary'))

execfile("EyesLibrary/version.py")

# execfile(join(dirname(__file__), 'EyesLibrary', 'version.py'))

# version_file = open("EyesLibrary/version.py")
# VERSION = version_file.read().strip()

DESCRIPTION = """
EyesLibrary is a visual verification library for Robot Framework
that leverages the Eyes-Selenium and Selenium/Appium libraries.
"""[1:-1]

setup(name='EyesLibrary',
      version=VERSION,
      description='Visual Verification testing library for Robot Framework',
      long_description=DESCRIPTION,
      url='https://github.com/joel-oliveira/EyesLibrary',
      license='Apache License 2.0',
      keywords='robotframework testing testautomation eyes-selenium selenium appium visual-verification',
      platforms='any',
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 2.7.14",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Testing",
          "Topic :: Software Development :: Quality Assurance"
      ],
      install_requires=[
          'robotframework >= 3.1.1',
          'eyes-selenium >= 3.15.2'
      ],
      packages=['EyesLibrary'],
      data_files=[
          ('tests/acceptance', ['tests/acceptance/mobile_app.robot',
                                'tests/acceptance/mobile_browser.robot',
                                'tests/acceptance/mobile_hybrid_app.robot',
                                'tests/acceptance/web.robot']),
          ('doc', ['doc/ChangeLog.txt',
                   "doc/EyesLibrary-KeywordDocumentation.html"])
      ]
      )
