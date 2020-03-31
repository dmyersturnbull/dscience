import pytest
from functools import partial
from dscience.core.exceptions import IllegalPathError
from dscience.tools.path_tools import *
raises = pytest.raises


class TestPathTools:

	def test_sanitize_path_node_root(self):
		x = PathTools.sanitize_path_node
		for file in [None, False]:
			for root in [None, True]:
				assert x('C:', is_file=file, is_root_or_drive=root) == 'C:\\'
				assert x('C:\\', is_file=file, is_root_or_drive=root) == 'C:\\'
				assert x('/', is_file=file, is_root_or_drive=root) == '/'

	def test_sanitize_path_node_nonroot(self):
		x = PathTools.sanitize_path_node
		assert x('C:', is_root_or_drive=False) == 'C_'
		assert x(' C: ', is_root_or_drive=False) == 'C_'
		assert x('C:\\', is_root_or_drive=False) == 'C__'
		assert x('C:/', is_root_or_drive=False) == 'C__'
		assert x('.', is_root_or_drive=False) == '.'
		assert x('..', is_root_or_drive=False) == '..'

	def test_sanitize_path_abs(self):
		x = partial(PathTools.sanitize_path, show_warnings=False)
		assert str(x('abc\\./22')).replace('\\', '/') == 'abc/22'
		assert str(x('C:\\abc\\./22')).replace('\\', '/') == 'C:/abc/22'
		assert str(x('/abc\\./22')).replace('\\', '/') == '/abc/22'
		assert str(x('./abc\\./22')).replace('\\', '/') == 'abc/22'
		assert str(x('C:\\abc\\\\22')) == 'C:\\abc\\22'

	def test_sanitize_path(self):
		x = partial(PathTools.sanitize_path, show_warnings=False)
		assert str(x('abc|xyz', False)) == 'abc_xyz'
		assert str(x('abc\\xyz.', False)) == 'abc\\xyz'
		assert str(x('..\\5')) == '..\\5'
		assert str(x('xyz...', False)) == 'xyz'
		assert str(x('abc\\.\\xyz\\n.', False)) == 'abc\\xyz\\n'
		with raises(IllegalPathError):
			x('x' * 255)
		assert str(x('NUL')) == '_NUL_'
		assert str(x('nul')) == '_nul_'
		assert str(x('nul.txt')) == '_nul_.txt'
		assert str(x('abc\\NUL')) == 'abc\\_NUL_'
		assert str(x('NUL\\abc')) == '_NUL_\\abc'


if __name__ == '__main__':
	pytest.main()
