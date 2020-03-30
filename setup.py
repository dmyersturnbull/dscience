#!/usr/bin/env python3
# coding=utf-8

from pathlib import Path
from distutils.core import setup
from dscience.core import Dscience

readme = Path('README.md').read_text(encoding='utf8')

setup(
	name=Dscience.name,
	version=Dscience.version,
	description='A collection of Python snippets for the Kokel Lab',
	long_description=readme,
	long_description_content_type='text/markdown',
	author='Douglas Myers-Turnbull',
	maintainer='Douglas Myers-Turnbull',
	url='https://github.com/kokellab/dscience',
	packages=['dscience',  'dscience.core', 'dscience.tools', 'dscience.support', 'dscience.biochem', 'dscience.analysis', 'dscience.ml'],
	test_suite='tests',
	python_requires='>=3.7',
	zip_safe=False,
	classifiers=[
		"Development Status :: 3 - Alpha",
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: Apache Software License',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Scientific/Engineering :: Bio-Informatics',
		'Topic :: Scientific/Engineering :: Chemistry',
		'Topic :: Scientific/Engineering :: Information Analysis',
		'Topic :: Scientific/Engineering :: Artificial Intelligence',
		'Topic :: Scientific/Engineering :: Visualization',
		'Operating System :: OS Independent',
		'Typing :: Typed'
	],
)
