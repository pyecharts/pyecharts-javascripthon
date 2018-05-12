# -*- coding: utf-8 -*-
DESCRIPTION = (
    'Embeded Python functions in pyecharts' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'pyecharts-javascripthon'
copyright = u'2018 pyecharts dev team'
version = '0.0.6'
release = '0.0.6'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'pyecharts-javascripthondoc'
latex_elements = {}
latex_documents = [
    ('index', 'pyecharts-javascripthon.tex',
     'pyecharts-javascripthon Documentation',
     'pyecharts dev team', 'manual'),
]
man_pages = [
    ('index', 'pyecharts-javascripthon',
     'pyecharts-javascripthon Documentation',
     [u'pyecharts dev team'], 1)
]
texinfo_documents = [
    ('index', 'pyecharts-javascripthon',
     'pyecharts-javascripthon Documentation',
     'pyecharts dev team', 'pyecharts-javascripthon',
     DESCRIPTION,
     'Miscellaneous'),
]
