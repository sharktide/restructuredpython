<OPTIMIZE> Directives
=====================

reStructuredPython allows you to apply runtime optimizations using special compiler directives and decorators.

.. code-block:: python

   <OPTIMIZE gct=True, parallel=True, profile=True>
   for i in range(10_000_000) {
       temp = str(i) * 10
   }


.. note::
   Optimizations currently support loops only. The function implementation currently **does not** have actual optimizations, only profiling and tracing.

Arguments for <OPTIMIZE ...> on loops include:

- ``gct=True``: Enable garbage collection tracking.
- ``profile=True``: Enable execution time logging.
- ``parallel=True``: Enables multiprocessing pool

Arguments for <OPTIMIZE ...> on functions include:

- ``profile=False`` Enable execution time logging
- ``trace=False`` Enable event tracing

This will generate a python file that imports the optimization decorators from this ( the ``restructuredpython`` package ), so you will need to have this package installed via pip on systems running your compiled, optimized program.

However, as of 2.5.0, you could technically open the generated python file, remove the imports from ``restructuredpython``, and instead use ``include 'subinterpreter.optimize'``. However, this is expictily NOT recommended as it will break in future versions of reStructuredPython and will include an annoying copyright header in the generated file.

We recommend running this with ``repycl`` the restructuredpython interpreter & launcher.
