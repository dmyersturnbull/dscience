#!/usr/bin/env python3
# coding=utf-8

from pathlib import Path
from distutils.core import setup

VERSION = '0.1.1'


readme = Path('README.md').read_text(encoding='utf8')
def github_links(org: str, repo: str, readthedocs: bool = False):
	return {
		'docs': 'https://{}.readthedocs.io'.format(repo) if readthedocs else 'https://github.com/{}/{}/docs'.format(org, repo),
		'source': 'https://github.com/{}/{}'.format(org, repo),
		'issues': 'https://github.com/{}/{}/issues'.format(org, repo),
	}


setup(
	name='dscience',
	version=VERSION,
	description='A collection of Python snippets for the Kokel Lab',
	long_description=readme,
	long_description_content_type='text/markdown',
	author='Douglas Myers-Turnbull',
	maintainer='Douglas Myers-Turnbull',
	url='https://github.com/kokellab/dscience',
	project_urls=github_links('kokellab', 'dscience', False),
	packages=['dscience',  'dscience.core', 'dscience.tools', 'dscience.support', 'dscience.biochem', 'dscience.analysis', 'dscience.ml'],
	test_suite='tests',
	python_requires='>=3.7',
	zip_safe=False,
	include_package_data=True,
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
		'Topic :: Software Development :: Build Tools',
		'Operating System :: OS Independent',
		'Typing :: Typed'
	],
)
