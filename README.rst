================================================================================
pyecharts-javascripthon
================================================================================

.. image:: https://api.travis-ci.org/pyecharts/pyecharts-javascripthon.svg?branch=master
   :target: http://travis-ci.org/pyecharts/pyecharts-javascripthon

.. image:: https://codecov.io/gh/pyecharts/pyecharts-javascripthon/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/pyecharts/pyecharts-javascripthon

.. image:: https://readthedocs.org/projects/pyecharts-javascripthon/badge/?version=latest
   :target: http://pyecharts-javascripthon.readthedocs.org/en/latest/


Introduction
================
pyecharts-javascripthon helps translate Python functions into javascript ones. It uses `javascripthon`_ and `dukpy`_
to blend Python codes into javascript runtime. It supports python 2.7, 3.4, 3.5 and 3.6. It works
on Linux, MacOS and Windows platforms.


Sample python function:

.. code-block:: python

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


Compiled python functions:

.. code-block:: javascript

   function renderItem(params, api) {
       var coord, size, values;
       values = [api.value(0), api.value(1)];
       coord = api.coord(values);
       size = api.size([1, 1], values);
       return {"type": "sector", "shape": {"cx": params["coordSys"]["cx"], "startAngle": (coord[3] - (size[1] / 2))}};
   }


From Python 2.7 to Python 3.4
-------------------------------

Internet access is required because it uses javascripthon api as a free service. Down the line,
community sponsorship will be required to cover the running cost of the service.

Because the service is still under development, the default api key and api host are subjected
to change. When it does happen please declare these environment variables to continue:

for unix alike systems:

.. code-block:: shell

   export SCRIPTHON_HOST=new_ip_address_or_domain_name
   export SCRIPTION_API_TOKEN=new_api_key


for windows systems:

.. code-block:: shell

   set SCRIPTHON_HOST=new_ip_address_or_domain_name
   set SCRIPTION_API_TOKEN=new_api_key


Python 3.5 - 3.6
-------------------

No internet access is required.

Usage
==================

1. Only Python 3.5+ code can be transcompiled. If you use python 2.7 or 3.4, you are obliged
to use generic Python codes so that python 2.7 and 3.4 interpreter do not complain.

2. For browsers DOM object, please include some of these statements so as to 'blind' python interpreter:


.. code-block:: python

   from pyecharts_javascripthon.dom.objects import window    # for window object
   from pyecharts_javascripthon.dom.objects import Document  # for Document object
   from pyecharts_javascripthon.dom.objects import Date      # for Date object


Credits
=============

javascripthon: `Alberto Berti <https://github.com/azazel75>`_

Dukpy: `Alessandro Molina <https://github.com/amol->`_ and `Sviatoslav Sydorenko <https://github.com/webknjaz`


.. _javascripthon: https://github.com/metapensiero/metapensiero.pj
.. _dukpy: https://github.com/amol-/dukpy



Installation
================================================================================


You can install pyecharts-javascripthon via pip:

.. code-block:: bash

    $ pip install pyecharts-javascripthon


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyecharts/pyecharts-javascripthon.git
    $ cd pyecharts-javascripthon
    $ python setup.py install
