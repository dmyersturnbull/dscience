#!/usr/bin/env python3
# coding=utf-8

import shutil
from pathlib import Path
from setuptools import setup, find_packages
from dscience import ProjectInfo as X

# copy the readme
readme_path = Path(X.name, 'resources', X.readme_filename)
shutil.copy(X.readme_filename, str(readme_path))
print(readme_path)

# generated from requirements.txt using Deps.write_setup_file_partial()
install_requires=[
	'dill          >=0.3,<1.0',
	'jsonpickle    >=1.3,<2.0',
	'natsort       >=7.0,<8.0',
	'numpy         >=1.18,<2.0',
	'pytables      >=3.6,<4.0',
	'pandas        >=1.0,<2.0',
	'requests      >=2.23,<3.0'
]
extras_require= {'extra': [
	'colorama      >=0.4.3,<1.0',
	'deprecated    >=1.2,<2.0',
	'overrides     >=2.8,<3.0',
	'psutil        >=5.7,<6.0',
	'toml          >=0.10,<1.0'
], 'db': [
	'PyMySQL       >=0.9,<1.0',
	'peewee        >=3.13,<4.0',
	'sshtunnel     >=0.1.5,<1.0'
], 'numeric': [
	'joblib        >=0.14,<1.0',
	'matplotlib    >=3.2,<4.0',
	'scikit-image  >=0.16,<1.0',
	'scikit-learn  >=0.22,<1.0',
	'scipy         >=1.4,<2.0'
], 'jupyter': [
	'ipython       >=7.13,<8.0'
], 'test': [
	'hypothesis    >=5.8,<6.0',
	'pytest        >=5.4,<6.0'
], 'biochem': [
	'goatools      >=1.0,<2.0',
	'uniprot       >=1.3,<2.0'
], 'all': []}

# make an 'all' for easy installation
for x in extras_require.values():
	extras_require['all'].extend(x)

setup(
	name=X.name,
	version=X.version,
	download_url = X.download_url,
	description=X.description,
	long_description=readme_path.read_text(encoding='utf8'),
	long_description_content_type=X.readme_format,
	author=X.author,
	license=X.license,
	maintainer=X.maintainer,
	url=X.url,
	project_urls=X.project_urls,
	packages=find_packages(),
	test_suite='tests',
	python_requires='>={}'.format(X.min_py_version),
	install_requires=install_requires,
	extras_require=extras_require,
	zip_safe=False,
	include_package_data=True,
	classifiers=X.classifiers,
	keywords=X.keywords
)
