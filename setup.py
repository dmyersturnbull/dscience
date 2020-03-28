#!/usr/bin/env python3
# coding=utf-8

from distutils.core import setup
from dscience.core import Dscience

setup(
	name=Dscience.name,
	version=Dscience.version,
	description=Dscience.description,
	author='Douglas Myers-Turnbull',
	url='https://github.com/kokellab/dscience',
	packages=['dscience',  'dscience.core', 'dscience.tools', 'dscience.support', 'dscience.biochem', 'dscience.analysis', 'dscience.ml', 'dscience.tests'],
	package_dir='',
	test_suite='dscience.tests',
	classifiers=[
		"Development Status :: 3 - Alpha",
		'Intended Audience :: Science/Research',
		'Natural Language :: English'
		'Operating System :: POSIX',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.7',
		'Topic :: Scientific/Engineering :: Bio-Informatics'
	],
)
