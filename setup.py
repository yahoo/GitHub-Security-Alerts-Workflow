#!/usr/bin/env python
# Copyright 2019, Oath Inc.
# Licensed under the terms of the Apache 2.0 license. See LICENSE file in project root for terms.
import sys
import setuptools


def setuptools_version_supported():
    major, minor, patch = setuptools.__version__.split('.')
    if int(major) > 31:
        return True
    return False
        

if __name__ == '__main__':
    if not setuptools_version_supported():
        print('Setuptools version 31.0.0 or higher is needed to install this package')
        sys.exit(1)

    # We're being run from the command line so call setup with our arguments
    setuptools.setup()
