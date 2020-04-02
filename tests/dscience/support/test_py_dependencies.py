import pytest
from pathlib import Path
from dscience.support.py_dependencies import *

class TestPyDependencies:
	# TODO
	def test(self):
		path = Path(__file__).parent.parent.parent.parent / 'requirements.txt'
		deps = Deps.read_req_file(path)
		#with open(Path(__file__).parent.parent.parent.parent / 'setup.py', 'a') as f:
		#	for line in deps.to_setup():
		#		f.write(line+'\n')
		#with open(Path(__file__).parent.parent.parent.parent / 'environment.yml', 'w') as f:
		#	for line in deps.to_env('dscience', 'conda-forge'):
		#		f.write(line+'\n')
		for dep in deps.to_requirements():
			print(dep)
		for dep in deps.to_setup():
			print(dep)


if __name__ == '__main__':
	pytest.main()

