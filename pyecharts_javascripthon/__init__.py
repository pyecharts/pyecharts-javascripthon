# flake8: noqa
from pyecharts_javascripthon._version import __version__
from pyecharts_javascripthon._version import __author__

from pyecharts_javascripthon.compiler import Python2Javascript

# Dummy functions to make python compiler blind
def Date(*_):
    pass


class Document:
    pass


class window:
    pass
