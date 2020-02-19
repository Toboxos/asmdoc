#!/usr/bin/env python

from setuptools import setup

setup(  name="asmdoc",
        version="1.1",
        packages=["asmdoc"],
        scripts=["asmdoc/asmdoc"],
        package_data = {"asmdoc": ["templates/*"]},
        )
