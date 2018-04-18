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
