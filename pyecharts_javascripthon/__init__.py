# flake8: noqa
import sys
from pyecharts_javascripthon._version import __version__
from pyecharts_javascripthon._version import __author__

if PY35 = sys.version_info[:2] >= (3, 5):
    from pyecharts_javascripthon.compiler import Python2Javascript
else:
    from pyecharts_javascripthon.complier_client import Python2Javascript

# Dummy functions to make python compiler blind
def Date(*_):
    pass


class Document:
    pass


class window:
    pass
