# `dscience`


A lightweight Python 3 library for everyday coding, data science, and bioinformatics.
Integrated with Numpy and Pandas 1.0+, with few other dependencies.

Provides:
- Many utility functions, data types, and decorators
- Exceptions that store useful attributes to help calling code recover
- Pandas DataFrames with required columns / enforced structure and extra methods
- Simple utilities for Jupyter notebooks
- Algorithms, bioinformatics resources, and machine learning support


The following documentation is not comprehensive. Search the code for additional classes.

[![CircleCI](https://circleci.com/gh/kokellab/dscience.svg?style=shield)](https://circleci.com/gh/kokellab/dscience)

### getting started

```bash
pip install git+https://github.com/kokellab/klgists.git@0.1.0#egg=dscience
pip install "dscience[numeric] @ git+ssh://git@github.com/kokellab/dscience.git@0.1.0#egg=dscience"
```

Dependencies are organized into strict requirements, `numeric`, `db`, `extra`, `jupyter`, `extra`, and `test`.

```python
from dscience.full import *
print(Tools)
```
This will load `Tools`, `Chars`, `abcd`, and a few others.


### `Tools` and `Chars`

The `Tools` class has various small utility functions:

```python
def fn_to_try():
    raise ValueError('')
from dscience.full import *
Tools.git_description('.').tag                # the tag, or None
Tools.ms_to_minsec(7512000)                   # '02:05:12'
Tools.fix_greek('beta,eta and Gamma')         # 'β,η and Γ'
Tools.pretty_function(lambda s: 55)           # '<λ(1)>'
Tools.pretty_function(list)                   # '<list>'
Tools.strip_paired_brackets('(ab[cd)')   # 'ab[cd'
Tools.iceilopt(None), Tools.iceilopt(5.3)     # None, 6
Tools.succeeds(fn_to_try)                     # True or False
Tools.or_null(fn_to_try)                      # None if it failed
Tools.only([1]), Tools.only([1, 2])           # 1, MultipleMatchesError
Tools.is_probable_null(np.nan)                # True
Tools.read_properties_file('abc.properties')  # returns a dict
important_info = Tools.get_env_info()         # a dict of info like memory usage, cpu, host name, etc.
```

`Chars` contains useful Unicode characters that are annoying to type, plus some related functions:
```python
from dscience.full import *
print(Chars.hairspace)             # hair space
print(Chars.range(1, 2))           # '1–2' (with en dash)
```

### decorators with `abcd`


The `abcd` package has useful decorators.
For example, output timing info:
```python
from dscience.full import *
@abcd.takes_seconds
def slow_fn():
    for _ in range(1000000): pass
slow_fn()  # prints 'Done. Took 23s.'
```

Or for an immutable class with nice `str` and `repr`:

```python
from dscience.full import *
@abcd.auto_repr_str()  # can also set 'include' or 'exclude'
@abcd.immutable
class CannotChange:
    def __init__(self, x: str):
        self.x = x
obj = CannotChange('sdf')
print('obj')  # prints 'CannotChange(x='sdf')
obj.x = 5  # breaks!!
``` 

### DataFrame subclasses

See `BaseFrame`, `SimpleFrame`, `FinalFrame`, and `OrganizingFrame`.
These are subclasses of `pd.DataFrame` that provide extra methods and display nicely.

### Exceptions and warnings

Sometimes certain modes of failure are expected (think: checked exceptions).
We want callers to be able to handle and potentially recover from them, but granularity in exception types and relevant values are needed.
For example, if we couldn't load a "resource" file, what was the path?
If something was wrong with a database record, what was its ID?
Examples of exceptions defined here are `LockedError`, `IncompatibleDataError`, `HashValidationFailedError`, `MissingEnvVarError`, `MultipleMatchesError`, `AlreadyUsedError`, and `IllegalPathError`.

```python
import time
from dscience.core.exceptions import *
resource = Path('resources/mydata.dat')
def update_resource():
    if resource.with_suffix('.lockfile').exists():
        raise LockedError('Resource is locked and may be in use.', key=resource)
    # ... do stuff
try:
    update_resource()
except LockedError as e:
    if e.key == resource:
        print('{} is locked. Waiting 5s and trying again.'.format(e.key))
        print(e.info())
        time.sleep(5.0)
        update_resource()
    else:
        raise e
    
```

### other small utilities
A couple of other things were imported, including `DevNull`, `DelegatingWriter`, and `TieredIterator`.

You can also make a Pandas DataFrame with pretty display and convenience functions using `TrivialExtendedDataFrame`.

`LazyWrap` creates lazy classes, extremely useful in some cases:

```python
from datetime import datetime
from dscience.core import LazyWrap
def fetch_datetime(): return datetime.now()
RemoteTime = LazyWrap.new_type('RemoteTime', fetch_datetime)
now = RemoteTime()
# nothing happens until now:
print(now.get())
```

### _a la carte_-style Tools

`Tools` actually subclasses from several Tools-like classes. You can import only the ones you want instead:

```python
from dscience.tools.path_tools import PathTools
print(PathTools.sanitize_file_path('ABC|xyz'))  # logs a warning & returns 'ABC_xyz'
print(PathTools.sanitize_file_path('COM1'))     # complains!! illegal path on Windows.
from dscience.tools.console_tools import ConsoleTools
if ConsoleTools.prompt_yes_no('Delete?'):
    #  Takes 10s, writing Deleting my_dir.......... Done.
    ConsoleTools.slow_delete('my_dir', wait=10)
```

### `J` for Jupyter display

The class `J` has tools for display in Jupyter:

```python
from dscience.j import *
J.red('This is bad.')            # show red text
if J.prompt('Really delete?'):   # ask the user
    J.bold('Deleting.')
```

### project organization

- `dscience.core` contains code used internally in dscience, including some that are useful in their own right
- `dscience.tools` contains the static tool classes like `StringTools`
- `dscience.support` contains data structures and supporting tools, such as `FlexibleLogger`, `TomlData`, and `WB1` (for multiwell plates).
- `dscience.analysis` contains algorithms such as `PeakFinder`
- `dscience.biochem` contains code specific to bioinformatics, cheminformatics, etc., such as `UniprotGoTerms`, `AtcTree`
- `dscience.ml` contains models for machine learning, including `DecisionFrame` and `ConfusionMatrix`


### support package

These classes range from common to very obscure.

`PrettyRecordFactory` makes beautiful aligned log messages.

```python
import logging
from dscience.support.log_format import *
logger = logging.getLogger('myproject')
log_factory = PrettyRecordFactory(7, 13, 5).modifying(logger)
```

Output from an analysis might then be...
```
[20191228:14:20:06] kale>    datasets      :77    INFO    | Downloading QC-DR...
[20191228:14:21:01] kale>    __init__      :185   NOTICE  | Downloaded QC-DR with 8 runs, 85 names, and 768 wells.
[20191229:14:26:04] kale>    __init__      :202   INFO    | Registered new type RandomForestClassifier:n_jobs=4,n_estimators=8000
```

`TomlData` is a wrapper around toml dict data.

`MagicTemplate` can build and register a Jupyter magic function that fills the cell from a template. Ex:

```python
import os
from dscience.support.magic_template import *
def get_current_resource():
    return 'something dynamic'
template_text = '''
# My notebook
<Write a description here>
**Datetime:      ${{datetime}}**
**Hostname:      ${{version}}**
**Resource name: ${{resource}}**
'''
MagicTemplate.from_text(template_text)\
	.add('hostname', os.hostname)\
	.add_datetime()\
	.add('resource', lambda: get_current_resource())\
	.register_magic('mymagic')

```

Now you can type in `%mymagic` to replace with the parsed template.


### biochem package

`WB1` is a multiwell plate with 1-based coordinates (read _well base-1_).

```python
from dscience.biochem.multiwell_plates import WB1
wb1 = WB1(8, 12)               # 96-well plate
print(wb1.index_to_label(13))  # prints 'B01'
for well in wb1.block_range('A01', 'H11'):
    print(well)                # prints 'A01', 'A02', etc.
```

Getting tissue-specific expression data in humans:

```python
from dscience.biochem.tissue_expression import TissueTable
tissues = TissueTable()
# returns a Pandas DataFrame of expression levels per cell type per gene for this tissue.
tissues.tissue('MKNK2')
```


### ml package

```python
from dscience.ml.confusion_matrix import ConfusionMatrix
mx = ConfusionMatrix.read_csv('mx.csv')                         # just a subclass of pd.DataFrame
print(mx.sum_diagonal() - mx.sum_off_diagonal())
mx = mx.sort(cooling_factor=0.98).symmetrize().triagonalize()   # sort to show block-diagonal structure, plus more
```


## contributing

This project is under active development. [New issues](https://github.com/kokellab/dscience/issues) and pull requests are welcome.
We use tabs for indentation and will eventually use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).

## license

The authors release these contents and documentation files under the terms of the [Apache License, version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
The project was developed to support research at the Kokel Lab, fulfill requirements for [UCSF QBC](http://qbc.ucsf.edu/) PhD programs, and be useful to the public.

Authors and contributors:
- Douglas Myers-Turnbull (primary)
- Chris Ki (contributor)
- Cole Helsell (contributor)