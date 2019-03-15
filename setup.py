#!/usr/bin/env python

import sys

# from distutils.core import setup
from setuptools import setup
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "EyesLibrary"))

execfile("EyesLibrary/version.py")

# execfile(join(dirname(__file__), 'EyesLibrary', 'version.py'))

# version_file = open("EyesLibrary/version.py")
# VERSION = version_file.read().strip()

DESCRIPTION = """
EyesLibrary is a visual verification library for Robot Framework
that leverages the Eyes-Selenium and Selenium/Appium libraries.
"""[
    1:-1
]

setup(
    name="EyesLibrary",
    version=VERSION,
    description="Visual Verification testing library for Robot Framework",
    long_description=DESCRIPTION,
    author="Thomas Armstrong, Simon McMorran, Gareth Nixon, Adam Simmons",
    author_email="<tarmstrong@navinet.net>, <smcmorran@navinet.net>, <gnixon@navinet.net>, <asimmons@navinet.net>",
    url="https://github.com/joel-oliveira/EyesLibrary",
    license="Apache License 2.0",
    keywords="robotframework testing testautomation eyes-selenium selenium appium visual-verification",
    platforms="any",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7.14",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
    ],
    install_requires=["robotframework >= 3.1.1", "eyes-selenium >= 3.15.2"],
    packages=["EyesLibrary"],
    data_files=[
        (
            "tests/acceptance",
            [
                "tests/acceptance/mobile_app.robot",
                "tests/acceptance/mobile_browser.robot",
                "tests/acceptance/mobile_hybrid_app.robot",
                "tests/acceptance/web.robot",
            ],
        ),
        ("doc", ["doc/ChangeLog.txt", "doc/EyesLibrary-KeywordDocumentation.html"]),
    ],
)
