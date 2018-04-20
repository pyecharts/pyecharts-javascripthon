import datetime
from nose.tools import eq_, raises
from textwrap import dedent

from pyecharts_javascripthon.api import TRANSLATOR


def test_basic_usage():

    def my_fmt(x):
        return x + 5

    def my_fmt2(x, z, y):
        return '{x},{y},{z}'.format(x=x, y=y, z=z)

    source = {'a': '23', 'b': my_fmt, 'c': my_fmt2, 'd': '-=>test<=-'}
    snippet = TRANSLATOR.translate(source)
    assert 'function my_fmt' in snippet.function_snippet
    assert 'function my_fmt2' in snippet.function_snippet
    assert 'function test' not in snippet.function_snippet
    assert '"my_fmt"' not in snippet.option_snippet
    assert '"my_fmt2"' not in snippet.option_snippet
    assert '"-=>test<=-"' in snippet.option_snippet

    source2 = {'e': my_fmt}
    snippet = TRANSLATOR.translate(source2)
    assert 'function my_fmt' in snippet.function_snippet
    assert '"my_fmt"' not in snippet.option_snippet


def test_datetime():
    a_date_time = datetime.datetime(2018, 4, 20, 19, 2, 30)
    option = {
        'datetime': a_date_time
    }
    expected = """
    {
        "datetime": "2018-04-20T19:02:30"
    }
    """

    actual = TRANSLATOR.translate(option)
    eq_(actual.option_snippet, dedent(expected).strip())


def test_date():
    a_date = datetime.date(2018, 4, 20)
    option = {
        'date': a_date
    }
    expected = """
    {
        "date": "2018-04-20"
    }
    """

    actual = TRANSLATOR.translate(option)
    eq_(actual.option_snippet, dedent(expected).strip())


@raises(Exception)
def test_time():
    a_time = datetime.time(19, 2, 30)
    option = {'time': a_time}
    TRANSLATOR.translate(option)
