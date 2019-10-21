taichigdb
========

This is a pretty printer for taichi types. This is largely based on https://github.com/dmillard/eigengdb. Formatting 
is handled by `numpy`.

Motivation
----------

Your debugging output shouldn't look like this:

.. code-block::

    (gdb) p p.C
    $1 = {static dim = 2, d = {{<taichi::VectorNDBase<2, float, (taichi::InstSetExt)0, void>> = {static simd
     = <optimized out>, static storage_elements = <optimized out>, {d = {0, 0}, {x = 0, y = 0}}}, static dim
     = 2, static ise = <optimized out>, static storage_elements = <optimized out>}, {<taichi::VectorNDBase<2
    , float, (taichi::InstSetExt)0, void>> = {static simd = <optimized out>, static storage_elements = <opti
    mized out>, {d = {0, 0}, {x = 0, y = 0}}}, static dim = 2, static ise = <optimized out>, static storage_
    elements = <optimized out>}}, static ise = <optimized out>}

But rather like this!

.. code-block::

    (gdb) p p.C
    $1 = taichi::MatrixND<2,float>
    [[0. 0.]
     [0. 0.]]


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
