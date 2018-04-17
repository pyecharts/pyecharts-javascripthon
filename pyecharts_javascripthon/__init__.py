# flake8: noqa
import sys
from pyecharts_javascripthon._version import __version__
from pyecharts_javascripthon._version import __author__

PY35_ABOVE = sys.version_info[:2] >= (3, 5)

if PY35_ABOVE:
    from pyecharts_javascripthon.compiler import Python2Javascript
else:
    from pyecharts_javascripthon.client import Python2Javascript

# Dummy functions to make python compiler blind
def Date(*_):
    pass


class Document:
    pass


class window:
    pass
