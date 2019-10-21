taichigdb
========

This is a pretty printer for taichi types (with some support for stan-math
types). Much of the logic comes from upstream taichi. Formatting is handled
by `numpy`.

Motivation
----------

Your debugging output shouldn't look like this:

.. code-block::


But rather like this!

.. code-block::



Installation
------------

It is important to use the python/pip version which corresponds to your GDB
installation. You can find out more information using the :code:`python` command in
GDB. For example, from GDB repl, you can find where GDB python will search for
packages.

.. code-block:: bash

   (gdb) python
   >import sys
   >print(sys.path)
   >end
   [..., '/path/to/site-packages', ...]

Then install using a corresponding python/pip (usually system pip).


From Source
~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/dmillard/taichigdb
   cd taichigdb
   python setup.py install # Make sure to use system python which matches GDB
   python bin/taichigdb_register_printers

Test
----

There is an example program you can play with in the :code:`examples/` directory.

.. code-block:: bash

   cd examples
   make
   make debug

License
-------

taichigdb is licensed under MPL2.0.
