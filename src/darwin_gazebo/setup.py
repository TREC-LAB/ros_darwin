#!/usr/bin/env python

# DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD
# This file add the folders in the PYTHONPATH, thus indentified as python package. 
# catkin provides a cmake macro that get this information from this file (setup.py)

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
# all we additionally have to provide is the information that is not in the package.xml
#     - the name of the scripts you want to have installed
#     - the name of the python packages
#     - where to find those packages
#     - python package dependencies
# (Those can have different names than what we use in the package.xml, so we need a separate list)

setup_args = generate_distutils_setup(
    packages = ['darwin_def_pkg'],
    package_dir = {'': 'src'},
)

setup(**setup_args)
