import os
from nose.tools import eq_
from pyecharts_javascripthon import Python2Javascript


def renderItem(params, api):
    values = [api.value(0), api.value(1)]
    coord = api.coord(values)
    size = api.size([1, 1], values)
    return {
        "type": 'sector',
        "shape": {
            "cx": params['coordSys']['cx'],
            "startAngle": coord[3] - size[1] / 2
            }
        }


def test_translation():
    result = Python2Javascript.translate(renderItem)
    with open(get_fixture('renderItem.js'), 'r') as f:
        expected = f.read()
        eq_(result, expected)


def get_fixture(afile):
    return os.path.join('tests', 'fixtures', afile)
