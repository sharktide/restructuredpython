<OPTIMIZE> Directives
=====================

reStructuredPython allows you to apply runtime optimizations using special 
compiler directives and decorators. These directives can be applied to both
loops and functions to enhance performance, enable diagnostics,
and optionally parallelize execution.

Loop Optimization
-----------------

Use ``<OPTIMIZE ...>`` before a ``for`` or ``while`` loop to apply runtime enhancements:

.. code-block:: python

<OPTIMIZE gct=True, parallel=True, profile=True, cache=True>
for i in range(10_000_000) {
    temp = str(i) * 10
}

.. versionadded:: 
   Added the cache option in 2.6.0

.. versionchanged::
   Changed the parallel functionality in 2.6.0 

Arguments for <OPTIMIZE ...> on loops include:

- ``gct=False``: Trigger garbage collection before loop execution.

- ``profile=False``: Log execution time of the loop.

- ``parallel=Flase``: Attempts **multithreading** using ``concurrent.futures.ThreadPoolExecutor``

- ``cache=False``: Enable memoization for loop-returning functions.

- ``unroll=N``: Unrolls loops to preserve preformance

.. warning::
   **<OPTIMIZE parallel=True> on loops uses multithreading only.** 
   For true multiprocessing, use python's multiprocessing module with
   top-level functions and ensure your script includes freeze_support
   due to limitations of python's multiprocessing setup.

   .. code-block:: python
      if __name__ == "__main__":
         from multiprocessing import freeze_support
         freeze_support()
         main()


Function Optimization
---------------------

You can also apply ``<OPTIMIZE ...>`` before a function definition 
to enable diagnostics and performance enhancements:

.. code-block:: python

   <OPTIMIZE profile=True, trace=True, cache=True>
   def compute(x) {
      return x ** 2
   }

.. versionadded::

   Note: Function optimization now includes caching 
   as well profiling and tracing, starting from version 2.6.0

Arguments for <OPTIMIZE ...> on functions include

- ``cache=False``: Uses LRU cahching for function memoization
- ``profile=False``: Log execution time of the function.
- ``trace=True``: Trace events for the function

This will generate a python file that imports the
optimization decorators from this ( the ``restructuredpython`` package ),
so you will need to have this package installed via pip on systems
running your compiled, optimized program.

.. note::
   However, as of 2.6.0, you could technically open the generated python file, remove the imports from ``restructuredpython``, and instead use ``include 'subinterpreter.optimize'``. However, this is expictily NOT recommended as it will break in future versions of reStructuredPython and will include an annoying copyright header in the generated file.

.. note::
   We recommend running this with ``repycl`` the restructuredpython interpreter & launcher.
