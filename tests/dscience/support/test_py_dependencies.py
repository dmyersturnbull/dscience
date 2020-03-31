import pytest
from pathlib import Path
from dscience.support.py_dependencies import *

class TestPyDependencies:
	# TODO
	def test(self):
		path = Path(__file__).parent.parent.parent.parent / 'requirements.txt'
		deps = Deps.read_req_file(path)
		for dep in deps.to_requirements():
			print(dep)
		for dep in deps.to_setup():
			print(dep)


if __name__ == '__main__':
	pytest.main()

