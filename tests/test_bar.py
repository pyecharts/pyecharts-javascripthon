import codecs
from pyecharts import Bar


def formatter(obj):
    return obj.name + 'abc'


def test_bar():
    attr = ["Jan", "Feb"]
    v1 = [2.0, 4.9]
    bar = Bar("Bar chart", "precipitation and evaporation one year")
    bar.add("precipitation", attr, v1, mark_line=["average"],
            mark_point=["max", "min"], label_formatter=formatter)
    bar.render()
    content = get_default_rendering_file_content()
    assert 'function formatter(obj)' in content
    assert 'obj.name + \"abc\"' in content
    assert '"formatter": formatter' in content


def get_default_rendering_file_content(file_name='render.html'):
    """
    Simply returns the content render.html
    """
    with codecs.open(file_name, 'r', 'utf-8') as f:
        return f.read()
