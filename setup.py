# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

from distutils.core import setup

ext_modules = []
cmdclass = {}

with open("requirements.txt", "r") as handle:
    install_requires = handle.read().splitlines()

setup(
    name="compert",
    version="1.0.0",
    description="",
    url="http://github.com/facebookresearch/CPA",
    author="See README.md",
    author_email="dlp@fb.com",
    license="MIT",
    packages=["compert"],
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    install_requires=install_requires,
)
