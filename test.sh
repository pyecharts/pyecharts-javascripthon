pip freeze
nosetests --with-coverage --cover-package pyecharts_javascripthon --cover-package tests  tests docs/source pyecharts_javascripthon && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
